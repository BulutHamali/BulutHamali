#!/usr/bin/env python3
"""
scripts/dna_contribution.py

Fetches GitHub contribution data via GraphQL and generates an animated
DNA sequencing SVG. Contribution levels (0-4) are mapped to nucleotides:

    0  → T  (no activity)     dim grey
    1  → A  (low)             light green
    2  → A  (medium-low)      green
    3  → C  (medium)          medium green
    4  → G  (high)            bright green

The SVG renders a sequencing scan effect: a glowing bar sweeps left
to right, revealing each nucleotide as it passes — like a DNA sequencer
reading a strand in real time.

Usage:
    GITHUB_TOKEN=<token> GITHUB_USERNAME=BulutHamali python scripts/dna_contribution.py

Environment variables:
    GITHUB_TOKEN      GitHub token with read:user scope (required)
    GITHUB_USERNAME   Target GitHub username (default: BulutHamali)
    OUTPUT_FILE       Output SVG path     (default: dna-sequencing.svg)
"""

import os
import sys
import requests

# ── Nucleotide mapping ────────────────────────────────────────────────────────
# level → (nucleotide, text_colour, cell_background)
NUCLEOTIDE_MAP = {
    0: ('T', '#484f58', '#0d1117'),   # No activity   → T  dim grey
    1: ('A', '#9be9a8', '#0e4429'),   # Low           → A  light green
    2: ('A', '#40c463', '#006d32'),   # Medium-low    → A  green
    3: ('C', '#30a14e', '#006d32'),   # Medium        → C  medium green
    4: ('G', '#39d353', '#26a641'),   # High          → G  bright green
}

COMPLEMENT = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}

# ── Layout constants ──────────────────────────────────────────────────────────
COLS     = 53
ROWS     = 7
CELL_W   = 14
CELL_H   = 16
GAP_X    = 2
GAP_Y    = 2
PAD_LEFT = 34
PAD_TOP  = 52
PAD_BOT  = 38

# ── Animation constants ───────────────────────────────────────────────────────
LOOP_DUR = 10    # seconds – full loop duration
SCAN_DUR = 7     # seconds – scan sweep duration

# ── GitHub GraphQL ────────────────────────────────────────────────────────────
_GQL = """
query($username: String!) {
  user(login: $username) {
    contributionsCollection {
      contributionCalendar {
        weeks {
          contributionDays {
            contributionCount
            contributionLevel
            date
          }
        }
      }
    }
  }
}
"""

_LEVEL_MAP = {
    'NONE':            0,
    'FIRST_QUARTILE':  1,
    'SECOND_QUARTILE': 2,
    'THIRD_QUARTILE':  3,
    'FOURTH_QUARTILE': 4,
}


def fetch_contributions(username: str, token: str) -> list[dict]:
    """Fetch the last 365 days of contributions via GitHub GraphQL."""
    resp = requests.post(
        'https://api.github.com/graphql',
        json={'query': _GQL, 'variables': {'username': username}},
        headers={'Authorization': f'Bearer {token}', 'Content-Type': 'application/json'},
        timeout=30,
    )
    resp.raise_for_status()
    payload = resp.json()

    if 'errors' in payload:
        print(f'GraphQL errors: {payload["errors"]}', file=sys.stderr)
        sys.exit(1)

    days = []
    weeks = (
        payload['data']['user']
               ['contributionsCollection']
               ['contributionCalendar']
               ['weeks']
    )
    for week in weeks:
        for day in week['contributionDays']:
            days.append({
                'date':  day['date'],
                'count': day['contributionCount'],
                'level': _LEVEL_MAP.get(day['contributionLevel'], 0),
            })

    return days[-365:]


# ── Grid builder ──────────────────────────────────────────────────────────────

def _build_grid(days: list[dict]) -> list[list[dict]]:
    """Arrange days into a (ROWS × COLS) grid, column-major (like GitHub)."""
    total  = COLS * ROWS
    padded = [{'level': 0}] * max(0, total - len(days)) + list(days)
    padded = padded[-total:]

    grid = []
    for row in range(ROWS):
        r = []
        for col in range(COLS):
            lv = padded[col * ROWS + row]['level']
            nucl, fg, bg = NUCLEOTIDE_MAP[lv]
            r.append({
                'nucl': nucl,
                'comp': COMPLEMENT[nucl],
                'fg':   fg,
                'bg':   bg,
                'lv':   lv,
            })
        grid.append(r)
    return grid


# ── SVG generation ────────────────────────────────────────────────────────────

def _kt(delay: float) -> str:
    """Build a 5-stop keyTimes string for a column's fade-in animation."""
    t0 = max(0.0005, delay / LOOP_DUR)
    t1 = min((delay + 0.35) / LOOP_DUR, 0.93)
    t2 = 0.95
    return f'0;{t0:.4f};{t1:.4f};{t2:.4f};1'


def generate_svg(days: list[dict], username: str) -> str:
    grid = _build_grid(days)

    W  = PAD_LEFT + COLS * (CELL_W + GAP_X) + 24
    H  = PAD_TOP  + ROWS * (CELL_H + GAP_Y) + PAD_BOT

    gx1 = PAD_LEFT
    gx2 = PAD_LEFT + COLS * (CELL_W + GAP_X)
    gy1 = PAD_TOP
    gy2 = PAD_TOP  + ROWS * (CELL_H + GAP_Y)

    # Scan bar geometry — bar starts off-screen left, sweeps at constant
    # velocity so it reaches gx2 exactly at SCAN_DUR, then fades out.
    sw          = 30
    scan_start  = gx1 - sw
    # Total x-travel to maintain constant velocity over full LOOP_DUR
    scan_end_x  = int(scan_start + (gx2 - scan_start) * (LOOP_DUR / SCAN_DUR))
    t_scan_fade = SCAN_DUR / LOOP_DUR

    p = []   # SVG parts list

    # ── Root element
    p.append(
        f'<svg viewBox="0 0 {W} {H}" width="{W}" height="{H}" '
        f'xmlns="http://www.w3.org/2000/svg">'
    )

    # ── Defs
    p.append('<defs>')

    p.append('''<style>
  .title { font: bold 10px "Courier New",Courier,monospace; fill: #58a6ff; letter-spacing: 1.5px; }
  .sub   { font: 9px "Courier New",Courier,monospace; fill: #8b949e; }
  .nuc   { font: bold 11px "Courier New",Courier,monospace; text-anchor: middle; dominant-baseline: central; }
  .leg   { font: 9px "Courier New",Courier,monospace; fill: #8b949e; }
</style>''')

    # Glow filter for high-activity nucleotides
    p.append('''<filter id="glow" x="-40%" y="-40%" width="180%" height="180%">
  <feGaussianBlur in="SourceGraphic" stdDeviation="2.5" result="b"/>
  <feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge>
</filter>''')

    # Scan bar gradient (soft glow, transparent at edges)
    p.append('''<linearGradient id="scanGrad" x1="0%" y1="0%" x2="100%" y2="0%">
  <stop offset="0%"   stop-color="#39d353" stop-opacity="0"/>
  <stop offset="35%"  stop-color="#39d353" stop-opacity="0.22"/>
  <stop offset="65%"  stop-color="#39d353" stop-opacity="0.22"/>
  <stop offset="100%" stop-color="#39d353" stop-opacity="0"/>
</linearGradient>''')

    p.append('</defs>')

    # ── Background + border
    p.append(f'<rect width="{W}" height="{H}" fill="#0d1117" rx="6"/>')
    p.append(f'<rect width="{W}" height="{H}" fill="none" stroke="#21262d" stroke-width="1" rx="6"/>')

    # ── Title
    p.append(f'<text x="{gx1}" y="16" class="title">'
             f'&#x2B21; DNA CONTRIBUTION SEQUENCE &#xB7; @{username}'
             f'</text>')

    # ── 5′ ─── 3′ header strand label
    dashes = '&#x2500;' * 86
    p.append(f'<text x="{gx1}" y="32" class="sub">5&#x02B9; {dashes} 3&#x02B9;</text>')

    # ── Backbone lines (phosphate-sugar strands above and below the grid)
    for yb, label_l, label_r in [
        (gy1 - 7,  "5'", "3'"),
        (gy2 + 3,  "3'", "5'"),
    ]:
        p.append(
            f'<line x1="{gx1}" y1="{yb}" x2="{gx2}" y2="{yb}" '
            f'stroke="#39d353" stroke-width="1" stroke-dasharray="3 3" opacity="0.3"/>'
        )
        p.append(f'<text x="{gx1 - 4}" y="{yb + 4}" class="sub" text-anchor="end">{label_l}</text>')
        p.append(f'<text x="{gx2 + 4}" y="{yb + 4}" class="sub">{label_r}</text>')

    # ── Day-of-week labels
    for row, label in [(0, 'Mon'), (2, 'Wed'), (4, 'Fri'), (6, 'Sun')]:
        y = gy1 + row * (CELL_H + GAP_Y) + CELL_H // 2
        p.append(f'<text x="{gx1 - 4}" y="{y}" class="sub" text-anchor="end">{label}</text>')

    # ── Scanning bar
    p.append(
        f'<rect x="{scan_start}" y="{gy1 - 8}" width="{sw}" '
        f'height="{ROWS * (CELL_H + GAP_Y) + 14}" fill="url(#scanGrad)" rx="3">'
        # Constant-velocity x sweep
        f'<animate attributeName="x" from="{scan_start}" to="{scan_end_x}" '
        f'dur="{LOOP_DUR}s" repeatCount="indefinite"/>'
        # Fade out once scan has finished
        f'<animate attributeName="opacity" '
        f'values="1;1;0;0" '
        f'keyTimes="0;{t_scan_fade:.4f};{min(t_scan_fade + 0.01, 0.99):.4f};1" '
        f'dur="{LOOP_DUR}s" repeatCount="indefinite"/>'
        f'</rect>'
    )

    # ── Nucleotide cells (staggered fade-in aligned with scan sweep)
    for col in range(COLS):
        x     = gx1 + col * (CELL_W + GAP_X)
        delay = (col / COLS) * SCAN_DUR
        kt    = _kt(delay)

        for row in range(ROWS):
            cell = grid[row][col]
            y    = gy1 + row * (CELL_H + GAP_Y)
            cx   = x + CELL_W // 2
            cy   = y + CELL_H // 2

            bg_peak = '0.9' if cell['lv'] > 0 else '0.4'

            # Cell background
            p.append(
                f'<rect x="{x}" y="{y}" width="{CELL_W}" height="{CELL_H}" rx="2" '
                f'fill="{cell["bg"]}" opacity="0">'
                f'<animate attributeName="opacity" '
                f'values="0;0;{bg_peak};{bg_peak};0" '
                f'keyTimes="{kt}" dur="{LOOP_DUR}s" repeatCount="indefinite"/>'
                f'</rect>'
            )

            # Nucleotide letter (glow on C and G)
            glow = 'filter="url(#glow)"' if cell['lv'] >= 3 else ''
            p.append(
                f'<text x="{cx}" y="{cy}" class="nuc" fill="{cell["fg"]}" opacity="0" {glow}>'
                f'{cell["nucl"]}'
                f'<animate attributeName="opacity" '
                f'values="0;0;1;1;0" '
                f'keyTimes="{kt}" dur="{LOOP_DUR}s" repeatCount="indefinite"/>'
                f'</text>'
            )

    # ── Legend
    ly = H - 12
    legend = [
        ('T', '#484f58', 'No commits'),
        ('A', '#9be9a8', 'Low  (1-2)'),
        ('C', '#30a14e', 'Medium (3)'),
        ('G', '#39d353', 'High  (4+)'),
    ]
    for i, (nucl, color, label) in enumerate(legend):
        lx = gx1 + i * 120
        p.append(
            f'<text x="{lx}" y="{ly}" class="leg">'
            f'<tspan fill="{color}" font-weight="bold">{nucl}</tspan>'
            f' &#x25A0; {label}'
            f'</text>'
        )

    p.append('</svg>')
    return '\n'.join(p)


# ── Entry point ───────────────────────────────────────────────────────────────

def main() -> None:
    username = os.environ.get('GITHUB_USERNAME', 'BulutHamali')
    token    = os.environ.get('GITHUB_TOKEN', '')
    out_file = os.environ.get('OUTPUT_FILE', 'dna-sequencing.svg')

    if not token:
        print('Error: GITHUB_TOKEN is not set.', file=sys.stderr)
        sys.exit(1)

    print(f'Fetching contributions for @{username}...')
    days = fetch_contributions(username, token)
    print(f'  → {len(days)} days fetched')

    print('Generating DNA sequencing SVG...')
    svg = generate_svg(days, username)

    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(svg)

    print(f'  → Saved to {out_file}')


if __name__ == '__main__':
    main()
