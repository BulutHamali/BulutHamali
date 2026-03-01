<img src="https://capsule-render.vercel.app/api?type=waving&color=0:0d1117,100:1f6feb&height=180&section=header" width="100%"/>

<div align="center">
<h1>Bulut Hamali</h1>
<h3>Turning Biological Complexity Into Computational Clarity</h3>
<a href="https://git.io/typing-svg"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=16&pause=1000&color=58A6FF&center=true&vCenter=true&width=600&lines=PhD+%C2%B7+Molecular+Biology+%26+Bioinformatics;Multi-Agent+AI+Systems+Architect;Full-Stack+Engineer+%7C+MERN+Stack;Building+AI+that+understands+biology" alt="Typing SVG"/></a>
<br/>
<a href="https://www.linkedin.com/in/bulut-hamali/"><img src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/></a>
<a href="https://buluthamali.com"><img src="https://img.shields.io/badge/Personal_Website-000000?style=for-the-badge"/></a>
<a href="mailto:info@buluthamali.com"><img src="https://img.shields.io/badge/Email-EA4335?style=for-the-badge&logo=gmail&logoColor=white"/></a>
<br/>
<img src="https://komarev.com/ghpvc/?username=BulutHamali&style=for-the-badge&color=0A66C2&label=PROFILE+VIEWS"/>
</div>

---

## The Mission

The gap between raw genomic data and actionable clinical insight is vast — and mostly unautomated.

My work sits precisely in that gap. I design and build AI-driven systems that transform high-dimensional biological data (single-cell transcriptomics, variant calls, clinical trial criteria) into structured, auditable intelligence. Whether that means orchestrating a multi-agent LLM pipeline to verify patient eligibility or engineering a high-performance variant detection tool in Python, the goal is the same: **make the biology computable and the computation trustworthy**.

---

## Currently Building

| Status | Project | Focus |
|---|---|---|
| 🛠 Ongoinge | **ClinPilot** | Expanding the FDA Guardrail agent with real-time ClinicalTrials.gov API integration |
| 🛠 Ongoing | **Spatial Transcriptomics Pipeline** | Adding cell-cell communication inference via CellChat |
| 🛠 Ongoing | **MERN Clinical Dashboard** | Building a patient-facing eligibility interface for ClinPilot |

---

## Featured Projects

---

### ClinPilot — Multi-Agent Clinical Trial Orchestrator

> *How do you reliably match a real patient to the right clinical trial when the eligibility criteria span 40+ pages of regulatory language?*

**Problem**
Clinical trial eligibility verification is time-intensive, error-prone, and bottlenecked by human reviewers who must reconcile unstructured patient records against complex inclusion/exclusion criteria. A single missed criterion can disqualify a patient or expose a site to compliance risk.

**Solution**
A 5-agent LLM pipeline where each agent owns a distinct epistemic role, running in sequence with structured handoffs:

| Agent | Role |
|---|---|
| **Researcher** | Retrieves and parses relevant trial criteria via RAG over ChromaDB |
| **Advocate** | Constructs the case *for* patient eligibility |
| **Critic** | Constructs the case *against*, stress-testing edge cases |
| **Auditor** | Reconciles the Advocate/Critic debate into a structured verdict |
| **FDA Guardrail** | Final pass for regulatory compliance and citation integrity |

The **Granville Strategy** underpins performance: a SQLite-based semantic caching layer intercepts repeated or near-duplicate queries before they reach the LLM, reducing latency and inference cost by short-circuiting redundant reasoning chains.

**Tech Stack**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Llama](https://img.shields.io/badge/Llama_3.3_70B-0467DF?style=flat-square&logo=meta&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6B35?style=flat-square&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat-square&logo=langchain&logoColor=white)

```
Architecture: RAG → Multi-Agent Deliberation → Regulatory Guardrail → Cached Response
Caching:      Granville Strategy (SQLite semantic cache) — reduces redundant LLM calls
Model:        Llama 3.3 70B (instruction-tuned) via local inference
```

---

### Bioinformatics Research Portfolio

#### Spatial Transcriptomics — Colon Cancer Tumor Microenvironment

**Problem**
Bulk RNA-seq averages over all cells in a tissue, obscuring the spatial organization of tumor, immune, and stromal compartments critical to understanding cancer progression.

**Solution**
End-to-end spatial transcriptomics pipeline processing 10x Visium data: spot deconvolution, spatially-variable gene detection, and ligand-receptor interaction mapping to characterize the colon cancer tumor microenvironment at tissue resolution.

**Tech Stack**

![R](https://img.shields.io/badge/R-276DC3?style=flat-square&logo=r&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Seurat](https://img.shields.io/badge/Seurat-2C2D72?style=flat-square&logoColor=white)
![Squidpy](https://img.shields.io/badge/Squidpy-FF9B00?style=flat-square&logoColor=white)

---

#### scRNA-seq Analysis — Gastric Cancer Cell Atlas

**Problem**
Gastric cancer subtypes are clinically heterogeneous, and bulk profiling fails to resolve the malignant, immune, and fibroblast populations driving treatment resistance.

**Solution**
Single-cell RNA-seq pipeline from raw count matrices through clustering, cell-type annotation, differential expression, and trajectory inference — reconstructing the cellular landscape of gastric tumor samples.

**Tech Stack**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Scanpy](https://img.shields.io/badge/Scanpy-3B4CC0?style=flat-square&logoColor=white)
![R](https://img.shields.io/badge/R-276DC3?style=flat-square&logo=r&logoColor=white)

---

#### GATK Variant Calling — INDELseek

**Problem**
Standard short-read variant callers under-perform on insertion/deletion detection in low-coverage or complex genomic regions, producing false-negative calls that matter clinically.

**Solution**
High-performance Python implementation of a targeted INDEL detection pipeline built on GATK best-practices, with custom filtering logic and optimized I/O for large cohort processing.

**Tech Stack**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![GATK](https://img.shields.io/badge/GATK-E63946?style=flat-square&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-4EAA25?style=flat-square&logo=gnubash&logoColor=white)
![Bioconductor](https://img.shields.io/badge/Bioconductor-2A6EBB?style=flat-square&logoColor=white)

---

### Full-Stack Engineering

**Problem**
Biological insights trapped in notebooks and scripts are invisible to clinicians, collaborators, and stakeholders who need them most.

**Solution**
MERN-stack applications that surface genomic and clinical data through accessible, authenticated interfaces — from gene expression visualizers to role-based clinical dashboards with RESTful APIs and JWT-secured endpoints.

**Tech Stack**

![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)
![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=node.js&logoColor=white)
![Express](https://img.shields.io/badge/Express-000000?style=flat-square&logo=express&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=flat-square&logo=mongodb&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)

---

## Skills Matrix

### Bioinformatics & Data Science

| Domain | Tools & Methods |
|---|---|
| Single-Cell Genomics | Scanpy, Seurat, scRNA-seq clustering, trajectory inference |
| Spatial Transcriptomics | 10x Visium, Squidpy, spatially-variable gene analysis |
| Variant Analysis | GATK, INDEL detection, VCF filtering, cohort pipelines |
| Statistical Analysis | R/Bioconductor, differential expression, survival analysis |
| Data Engineering | Pandas, NumPy, high-performance Python, HPC/SLURM |

### AI & LLM Orchestration

| Domain | Tools & Methods |
|---|---|
| Multi-Agent Systems | LangChain, custom agent graphs, deliberation frameworks |
| Retrieval-Augmented Generation | ChromaDB, vector embeddings, semantic search |
| LLM Integration | Llama 3.3 70B, OpenAI API, prompt engineering |
| Caching & Optimization | SQLite semantic cache (Granville Strategy), inference cost reduction |
| Regulatory AI | FDA-aware guardrail agents, citation integrity, audit trails |

### Full-Stack Engineering

| Domain | Tools & Methods |
|---|---|
| Frontend | React, JavaScript (ES6+), responsive UI |
| Backend | Node.js, Express, RESTful API design |
| Database | MongoDB, SQLite, data modeling |
| Auth & Security | JWT, role-based access control |
| DevOps | Git, GitHub Actions, Linux/Bash, Docker |

---

## Coding Activity

<!--START_SECTION:waka-->

```txt
From: 22 February 2026 - To: 01 March 2026

No activity tracked
```

<!--END_SECTION:waka-->

---

## GitHub Stats

<div align="center">

![Profile Summary](https://github-profile-summary-cards.vercel.app/api/cards/profile-details?username=BulutHamali&theme=github_dark)

![Stats](https://github-profile-summary-cards.vercel.app/api/cards/stats?username=BulutHamali&theme=github_dark)
![Top Languages by Commit](https://github-profile-summary-cards.vercel.app/api/cards/most-commit-language?username=BulutHamali&theme=github_dark)
![Top Languages by Repo](https://github-profile-summary-cards.vercel.app/api/cards/repos-per-language?username=BulutHamali&theme=github_dark)

![GitHub Streak](https://streak-stats.demolab.com?user=BulutHamali&theme=github_dark&hide_border=true)

[![Activity Graph](https://github-readme-activity-graph.vercel.app/graph?username=BulutHamali&theme=github-compact&hide_border=true&area=true)](https://github.com/ashutosh00710/github-readme-activity-graph)

![DNA Contribution Animation](https://raw.githubusercontent.com/BulutHamali/BulutHamali/main/dna-sequencing.svg)

</div>

---

<div align="center">

*"The most consequential code running today is the code that interprets biology."*

</div>

<img src="https://capsule-render.vercel.app/api?type=waving&color=0:1f6feb,100:0d1117&height=120&section=footer" width="100%"/>
