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

The gap between raw biological data and actionable clinical insight is vast — and mostly unautomated.

My work sits precisely in that gap. I build across the full stack of this problem: multi-agent AI pipelines that reason over clinical trial criteria, spatial and single-cell transcriptomics analyses that map tumor microenvironments at cellular resolution, regulatory-grade clinical data pipelines built to CDISC standards, and full-stack applications that surface these insights to the people who need them. The goal is always the same: **make the biology computable and the computation trustworthy**.

---

## Currently Building

| Status | Project | Focus |
|---|---|---|
| 🛠 Ongoing | **SpatioCore-Flow** | Gated multi-agent orchestrator for single-cell and spatial transcriptomics with Code-in-the-Loop hallucination prevention |
| 🟢 Active | **ClinPilot** | Expanding the Guardrail agent with real-time ClinicalTrials.gov API integration |
| 🟢 Active | **LabTasker** | Token persistence, email deadline reminders, analytics view, and time tracking per task |
| 🟢 Active | **CargoURL AI** | Supabase integration and live frontend connection to replace mock data with real API responses |

---

## Featured Projects

### ClinPilot — Multi-Agent Clinical Trial Orchestrator

> *How do you reliably match a real patient to the right clinical trial when the eligibility criteria span 40+ pages of regulatory language?*

**Problem**
Clinical trial eligibility verification is time-intensive, error-prone, and bottlenecked by human reviewers who must reconcile unstructured patient records against complex inclusion/exclusion criteria. A single missed criterion can disqualify a patient or expose a site to compliance risk.

**Solution**
A 5-agent LLM pipeline where each agent owns a distinct epistemic role, running in sequence with structured handoffs:

| Agent | Role |
|---|---|
| **Analyst** | Parses and structures patient records against trial criteria |
| **Researcher** | Retrieves and synthesizes relevant trial criteria via RAG over ChromaDB |
| **Advocate** | Constructs the case *for* patient eligibility |
| **Auditor** | Reconciles agent outputs into a structured eligibility verdict |
| **Guardrail** | Final pass for regulatory compliance and citation integrity |

**Tech Stack**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![OpenAI](https://img.shields.io/badge/OpenAI-412991?style=flat-square&logo=openai&logoColor=white)
![CrewAI](https://img.shields.io/badge/CrewAI-000000?style=flat-square&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6B35?style=flat-square&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)

```
Framework:  CrewAI multi-agent orchestration
Pipeline:   Patient intake → RAG retrieval → Sequential agent deliberation → Guardrail verdict
Models:     OpenAI gpt-4o / gpt-4o-mini
Storage:    ChromaDB (vector store) · SQLite (session cache)
```

---

### SpatioCore-Flow — Gated Multi-Agent Biological Orchestrator

> *What if an AI system could analyze a tumor's spatial architecture without hallucinating biology it never actually saw in the data?*

**Problem**
LLM-based bioinformatics tools fail silently — they reason over biological data but have no mechanism to verify their own inferences against the underlying genomics. In a clinical or research context, an undetected hallucination in a spatial deconvolution or cell-type annotation is not a minor error.

**Solution**
A production-grade multi-agent framework for autonomous Single-Cell Genomics and Spatial Transcriptomics analysis built on a Verification-First architecture. Every AI-generated inference is programmatically validated against raw AnnData/Squidpy objects through a **Code-in-the-Loop** gate before propagation — if the Biological Consistency Score drops below 0.8, the inference is rejected and the agent reruns with constraint adjustments.

| Agent | Role |
|---|---|
| **Curator** | Maps raw input to the correct biological coordinate system (dissociated vs. in-situ) |
| **Analyst** | Executes foundation models (scGPT, Geneformer, Tangram, cell2location) for deconvolution and ST prediction |
| **Validator** | Code-driven verification of Analyst claims against source data |
| **Synthesizer** | Merges "What" (RNA) with "Where" (Spatial) into a tumor microenvironment graph |
| **Auditor** | Source-to-bit traceability linking every claim to a gene index or pixel coordinate |
| **Guardrail** | Evaluates outputs against FDA/SaMD risk frameworks and clinical literature |

**Tech Stack**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![CrewAI](https://img.shields.io/badge/CrewAI-000000?style=flat-square&logoColor=white)
![LiteLLM](https://img.shields.io/badge/LiteLLM-1C3C3C?style=flat-square&logoColor=white)
![Scanpy](https://img.shields.io/badge/Scanpy-3B4CC0?style=flat-square&logoColor=white)
![Squidpy](https://img.shields.io/badge/Squidpy-FF9B00?style=flat-square&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat-square&logo=streamlit&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![ChromaDB](https://img.shields.io/badge/ChromaDB-FF6B35?style=flat-square&logoColor=white)

```
Architecture:  Hybrid DAG orchestration · Sandbox-Gate pattern
Validation:    Code-in-the-Loop · Biological Consistency Score (BCS ≥ 0.8)
Models:        scGPT · Geneformer · Tangram · cell2location · StarDist
Storage:       PostgreSQL (audit trail) · ChromaDB (RAG) · Redis (cache)
```

---

### Bioinformatics Research Portfolio

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

#### Spatial Transcriptomics — Breast Cancer Tumor Microenvironment (Xenium)

**Problem**
Standard scRNA-seq dissolves tissue architecture — you lose the spatial organization of tumor, immune, and stromal compartments that determines how cancer progresses and resists treatment.

**Solution**
End-to-end spatial transcriptomics pipeline on a 10x Xenium in situ dataset from a human breast cancer FFPE section: cell type mapping, spatially-resolved gene expression patterns, and tissue architecture characterization at single-cell resolution.

**Tech Stack**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Squidpy](https://img.shields.io/badge/Squidpy-FF9B00?style=flat-square&logoColor=white)
![Scanpy](https://img.shields.io/badge/Scanpy-3B4CC0?style=flat-square&logoColor=white)

---

#### SDTM/ADaM Clinical Data Pipeline

**Problem**
Regulatory submissions to the FDA and EMA require clinical trial data in CDISC-standard formats. Transforming raw trial datasets into analysis-ready ADaM structures — and from there into auditable TLF outputs — demands both statistical rigor and deep familiarity with submission standards.

**Solution**
End-to-end clinical data pipeline from SDTM source datasets (DM, AE, LB) through ADaM derivation (ADSL subject-level, ADAE adverse events) to regulatory-grade tables, listings, and figures. Fully automated via a single `run_all.R` entry point.

**Tech Stack**

![R](https://img.shields.io/badge/R-276DC3?style=flat-square&logo=r&logoColor=white)
![admiral](https://img.shields.io/badge/admiral-2C2D72?style=flat-square&logoColor=white)
![Bioconductor](https://img.shields.io/badge/Bioconductor-2A6EBB?style=flat-square&logoColor=white)

```
Standards:  CDISC SDTM → ADaM (ADSL, ADAE)
Outputs:    AE summary tables, demographics TLFs, treatment-emergent AE flags
Pipeline:   Modular R scripts · run_all.R single-command execution
```

---

### LabTasker — Research Lab Task Manager

> *Research workflows don't fit generic project managers — they need Kanban boards that understand experiments, not sprints.*

**Problem**
Lab teams lose track of experiments, deadlines, and task ownership across spreadsheets and email threads. Generic project tools lack the domain-specific structure that research workflows require.

**Solution**
Full-stack research task management application with a drag-and-drop Kanban board (To Do / In Progress / Done), per-project progress tracking, and JWT-authenticated user accounts. Frontend deployed on Render with a live demo.

**Frontend**

![React](https://img.shields.io/badge/React_18-61DAFB?style=flat-square&logo=react&logoColor=black)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![Tailwind CSS](https://img.shields.io/badge/Tailwind_CSS-06B6D4?style=flat-square&logo=tailwindcss&logoColor=white)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=flat-square&logo=vite&logoColor=white)

**Backend**

![Node.js](https://img.shields.io/badge/Node.js-339933?style=flat-square&logo=node.js&logoColor=white)
![Express](https://img.shields.io/badge/Express_5-000000?style=flat-square&logo=express&logoColor=white)
![MongoDB](https://img.shields.io/badge/MongoDB_Atlas-47A248?style=flat-square&logo=mongodb&logoColor=white)

```
Auth:       JWT · bcrypt · protected routes
Features:   Drag-and-drop reorder, due dates, progress bars, per-user scoping
Live demo:  https://labtasker-frontend.onrender.com
```

---

### CargoURL AI — Click Analytics & Optimization API

> *A link management platform needs more than redirect counts — it needs to tell you when to post, who's clicking, and whether the numbers are moving.*

**Problem**
Raw click data from a URL shortener is noise without context. Posting time, audience composition, and CTR deltas require time-series forecasting and segmentation — not just counting.

**Solution**
A Flask REST API that turns raw click event streams into optimization signals: high-engagement posting window prediction via Prophet, audience segmentation via KMeans clustering, and CTR delta reporting. Built as the analytics and AI backend for [CargoURL](https://cargourl.com).

**Tech Stack**

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![Prophet](https://img.shields.io/badge/Prophet-0467DF?style=flat-square&logo=meta&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikit-learn&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white)

```
Pipeline:   Click events → Prophet forecasting → KMeans segmentation → CTR delta
Deployment: Railway / Render (Nixpacks)
Status:     API functional and deployed; frontend integration in progress
```

---

## Skills Matrix

### Bioinformatics & Data Science

| Domain | Tools & Methods |
|---|---|
| Single-Cell Genomics | Scanpy, Seurat, scRNA-seq clustering, trajectory inference |
| Spatial Transcriptomics | 10x Xenium (in situ), Squidpy, spatial gene expression analysis |
| Clinical Data Standards | CDISC SDTM/ADaM, TLF generation, admiral (R), regulatory pipelines |
| Statistical Analysis | R/Bioconductor, differential expression, survival analysis |
| Data Engineering | Pandas, NumPy, high-performance Python, HPC/SLURM |

### AI & LLM Orchestration

| Domain | Tools & Methods |
|---|---|
| Multi-Agent Systems | CrewAI, custom agent graphs, deliberation frameworks |
| Retrieval-Augmented Generation | ChromaDB, vector embeddings, semantic search |
| LLM Integration | OpenAI API (gpt-4o, gpt-4o-mini), prompt engineering |
| Caching & Optimization | SQLite semantic cache, inference cost reduction |
| Regulatory AI | FDA-aware guardrail agents, citation integrity, audit trails |

### Full-Stack Engineering

| Domain | Tools & Methods |
|---|---|
| Frontend | React 18, TypeScript, Tailwind CSS, shadcn/ui, Vite |
| Backend | Node.js, Express, Flask, RESTful API design |
| Database | MongoDB Atlas, SQLite, data modeling |
| Auth & Security | JWT, bcrypt, role-based access control |
| DevOps | Git, GitHub Actions, Linux/Bash, Render, Railway |

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
