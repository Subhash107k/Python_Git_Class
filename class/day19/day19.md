# Day 19 — Project Architecture, Packaging & Production Workflow

## Learning Objectives

* Understand professional Python project structure.
* Organize code using modules and packages.
* Separate models, services, utilities, and CLI logic.
* Manage project dependencies and package configuration.
* Begin the final portfolio project architecture.

---

## Topics Covered

### 1. Project Architecture

Learn how to organize a larger Python application using **separation of concerns**.

```text
paams_app/
├── README.md
├── requirements.txt
├── setup.py
├── data/
├── src/
│   ├── models/
│   ├── services/
│   └── utils/
└── main.py
```

### 2. Modules & Packages

* `__init__.py`
* Models — application data and objects.
* Services — business logic.
* Utilities — reusable helpers.
* CLI — user interaction.

### 3. Project Configuration

Understand the purpose of:

* `setup.py` — package configuration.
* `requirements.txt` — project dependencies.
* `README.md` — project documentation.
* `.gitignore` — files that should not be tracked.

---

## Capstone Project — PAAMS

Begin scaffolding the **Personal Asset & Analytics Management System (PAAMS)**.

The project will eventually manage:

* Users
* Assets
* Transactions
* Analytics
* Reports
* CLI operations

At this stage, focus only on **project structure and organization**, not full implementation.

---

## Git / GitHub Practice

Create a dedicated feature branch:

```bash
git switch -c feature/portfolio-setup
```

Stage and commit the project structure:

```bash
git add .
git commit -m "chore: scaffold PAAMS project architecture"
git push -u origin feature/portfolio-setup
```

---

## Mini Task

Create the PAAMS folder structure with:

* `models/`
* `services/`
* `utils/`
* `data/`
* `main.py`
* `README.md`
* `requirements.txt`
* `.gitignore`

Add the required `__init__.py` files and push the architecture to GitHub.

---

## Expected Outcome

Student understands professional Python project organization and creates a clean, modular foundation for the **PAAMS portfolio project**.
