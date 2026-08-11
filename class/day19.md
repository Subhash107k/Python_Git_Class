# Day 19 — Portfolio Project Architecture, Packaging & Production Workflows

## Learning Objectives
- Architect a production-grade, multi-module Python application.
- Scaffold package directories with clear single-responsibility modules.
- Create professional project setup manifests (`setup.py`, `requirements.txt`).
- Design repository documentation standards (`README.md`, usage instructions).

---

## Topics Covered
1. **Multi-Module Project Architecture**:
   - Package structure design.
   - Separation of concerns: Models, Services, Utilities, and CLI interfaces.
2. **Package Setup & Configuration**:
   - `setup.py` configuration.
   - Entry point configuration.
   - Dependency manifests (`requirements.txt`).
3. **Capstone Scaffolding**:
   - Scaffolding the Personal Asset & Analytics Management System (PAAMS CLI).

---

## Theory & Classroom Explanation

### Production Multi-Module Package Layout
In professional Python development, applications are divided into focused directories under a `src/` root directory:

```text
paams_app/
│── .gitignore
│── README.md
│── requirements.txt
│── setup.py
├── data/
│   ├── sample_transactions.json
│   └── export_report.csv
├── src/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── asset.py
│   │   └── user.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── file_service.py
│   │   └── analytics_service.py
│   └── utils/
│       ├── __init__.py
│       ├── decorators.py
│       └── exceptions.py
└── main.py
```

---

## Practical Coding Exercises

### Exercise 19.1: Package Setup Scaffolding
Create `setup.py`:

```python
from setuptools import setup, find_packages

setup(
    name="paams_app",
    version="3.0.0",
    author="Your Name",
    description="Personal Asset & Analytics Management System CLI",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy>=1.20.0",
        "requests>=2.25.0"
    ],
    entry_points={
        "console_scripts": [
            "paams=main:main_cli"
        ]
    }
)
```

---

## Git / GitHub Practice

### Step 1: Create Feature Branch for Capstone Architecture
```bash
git switch -c feature/portfolio-setup
```

### Step 2: Commit Scaffolding Files
```bash
git add .
git commit -m "chore: scaffold multi-module portfolio project architecture and setup.py"
git push -u origin feature/portfolio-setup
```

---

## Expected Outcome
Student scaffolds a production-ready, modular Python project structure with dependency configurations.
