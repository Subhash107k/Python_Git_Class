# Day 11 — Modules, Packages, Virtual Environments & Git

## Overview

Day 11 focused on organizing Python code into **modules and packages**, managing project dependencies with virtual environments, and preventing Git merge conflicts.

All Python hands-on practice was completed in `day11.ipynb`.

---

## Learning Objectives

* Create and import custom Python modules.
* Understand Python packages.
* Use `if __name__ == "__main__":`.
* Create and manage virtual environments.
* Install Python packages with `pip`.
* Generate `requirements.txt`.
* Keep virtual environments out of Git.
* Sync branches before merging to reduce conflicts.

---

## Topics Covered

### Python

* Custom modules
* `import`
* `from ... import ...`
* Python packages
* `__init__.py`
* `__name__`
* Entry-point guards
* Virtual environments
* `venv`
* `pip`
* `requirements.txt`

### Git

* Merge conflict prevention
* Keeping feature branches updated
* `.gitignore`
* Dependency files
* Commit and push workflow

---

## Theory

### Modules & Packages

A **module** is a Python file containing reusable code.

A **package** is a directory used to organize related modules.

```text id="x3p8vk"
Package
 ├── module_a.py
 ├── module_b.py
 └── __init__.py
```

This makes larger projects easier to organize and maintain.

---

## Entry Point Guard

The following pattern allows code to run only when the file is executed directly:

```text id="h6q2mr"
if __name__ == "__main__":
    ...
```

This prevents self-test or execution code from running automatically when the module is imported.

---

# Virtual Environments

A virtual environment isolates project dependencies from the global Python installation.

Create one with:

```bash id="w8f4cz"
python -m venv .venv
```

Activate on Windows PowerShell:

```bash id="p3k7nd"
.venv\Scripts\Activate.ps1
```

Install packages:

```bash id="v5m2qa"
pip install requests
```

Save dependencies:

```bash id="r6x9bt"
pip freeze > requirements.txt
```

---

## Why Use `.venv`?

```text id="n4y7cx"
Project A
 └── .venv
     └── Dependencies A

Project B
 └── .venv
     └── Dependencies B
```

Each project can maintain its own package versions without affecting other projects.

---

# Git Practice

Make sure `.venv/` is included in `.gitignore`.

Typical Python entry:

```text id="e8w3qp"
.venv/
```

Commit the project files:

```bash id="j2m5vr"
git add .
git commit -m "feat: add Python modules and virtual environment setup"
git push
```

---

# Git Conflict Prevention

Before merging a feature branch, synchronize it with the latest `main` branch.

```text id="u5q9ka"
Updated main
     ↓
Sync Feature Branch
     ↓
Resolve Conflicts Early
     ↓
Merge
```

Keeping branches updated reduces the chance of large merge conflicts.

---

# Python Practice

All exercises are available in:

```text id="b7n3qx"
day11.ipynb
```

Practice included:

* Creating modules
* Importing functions
* Entry-point guards
* Package structure
* Virtual environments
* Installing packages
* Creating `requirements.txt`

---

# Mini Task — String Helpers

Create a reusable module containing:

* `reverse_string()`
* `count_vowels()`

Add a self-test using an entry-point guard and import the module from a separate main script.

Run the project inside the active `.venv` and commit the changes.

---

## Day 11 Deliverables

```text id="c8m4yp"
class/
└── day11/
    └── day11.ipynb

.venv/
requirements.txt
.gitignore
```

* [x] Modules
* [x] Packages
* [x] Imports
* [x] Entry-point guard
* [x] Virtual environments
* [x] `pip`
* [x] `requirements.txt`
* [x] Git conflict prevention

---

## Expected Outcome

By the end of Day 11, the learner can organize Python code into reusable modules, isolate dependencies with virtual environments, manage requirements, and prepare Git branches for safer merging.
