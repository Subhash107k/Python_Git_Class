# Python + Git/GitHub Class

A hands-on **20-Day Python + Git/GitHub learning repository** designed to take beginners from Python fundamentals to practical programming, version control, GitHub workflows, NumPy, and a final multi-module project.

The repository contains daily lesson materials, Jupyter notebooks, practical projects, Git/GitHub references, and supporting documentation created and organized throughout the class.

---

## 📚 Repository Overview

This repository is organized around a progressive **20-day learning path**:

**Python Fundamentals → Problem Solving → Files & OOP → NumPy → Git/GitHub → Projects → Capstone**

### Repository Structure

```text
Python_Git_Class/
│
├── class/
│   ├── day01/
│   ├── day02/
│   ├── day03/
│   ├── ...
│   └── day20/
│
├── notebooks/
│   ├── day01_python_basics.ipynb
│   ├── day02_variables_types.ipynb
│   ├── day03_strings_operators.ipynb
│   ├── day04_control_flow.ipynb
│   ├── day06_lists_tuples.ipynb
│   ├── day07_sets_dictionaries.ipynb
│   ├── day08_comprehensions.ipynb
│   ├── day18_numpy.ipynb
│   └── optional/
│       └── numpy_image_processing_reference.ipynb
│
├── projects/
│   ├── nepal-weather/
│   ├── qr_generator.py
│   └── final-capstone/
│
├── docs/
│   ├── learning-report.md
│   └── git-guide.md
│
├── archive/
│   └── legacy-notebooks/
│
├── requirements.txt
├── test.py
├── LICENSE
└── README.md
```

> **Note:** The exact folder contents may evolve as classroom materials are extracted, refined, and expanded.

---

## 📘 How to Learn from This Repo

This repository is organized as a guided 20-day learning path. To get the most from it:

- Start with Day 1 and follow the lessons in sequence.
- Read each day's markdown notes before running the example code.
- Open the matching notebook when available for hands-on practice.
- Write and run code in your own editor as you learn each topic.
- Use Git commands regularly to track your progress and practice version control.
- Revisit earlier lessons whenever a later topic depends on earlier skills.
- Apply concepts through the practical projects and capstone exercise.

---

# 🎯 Learning Objectives

By completing this repository, students progressively learn to:

- Understand Python syntax and programming fundamentals
- Work with variables, data types, strings, collections, and control flow
- Write reusable functions and modules
- Handle files, CSV, JSON, and exceptions
- Understand object-oriented programming
- Use decorators and generators
- Work with Python's standard library
- Use NumPy for numerical and array-based programming
- Build practical command-line applications
- Use Git for version control
- Work with GitHub repositories and branches
- Understand commits, merges, stashing, rebasing, and recovery
- Organize Python projects professionally
- Apply Python knowledge to practical projects
- Develop a final multi-module Python application

---

# 🗓️ 20-Day Curriculum

|    Day | Python / Programming                             | Git / GitHub                              | Practical Work                  |
| -----: | ------------------------------------------------ | ----------------------------------------- | ------------------------------- |
| **01** | Python setup, interpreter, syntax, comments      | `git config`, `git init`                  | Python & Git environment setup  |
| **02** | Variables, data types, casting, `input()`        | Staging and commits                       | Basic Python programs           |
| **03** | Operators, strings, slicing, string methods      | `git status`, `git log`, `git diff`       | String manipulation             |
| **04** | `if`, `elif`, `else`, logical conditions         | Branching fundamentals                    | Decision-making programs        |
| **05** | Loops and control statements                     | Remote repositories and `git push`        | CLI tool practice               |
| **06** | Lists, tuples, sorting, custom sort keys         | `git pull` and repository synchronization | Collection-based programs       |
| **07** | Sets, dictionaries, nested structures            | Feature branches                          | Structured data exercises       |
| **08** | Comprehensions and memory concepts               | `.gitignore` and repository documentation | Python data transformation      |
| **09** | Functions, parameters, scope                     | `git stash`                               | Reusable functions              |
| **10** | `*args`, `**kwargs`, lambda, `map()`, `filter()` | Branch merging                            | Functional programming practice |
| **11** | Modules and `__main__` guard                     | Virtual environments                      | Modular Python programs         |
| **12** | File I/O, CSV, JSON, context managers            | `restore`, `revert`                       | File-processing programs        |
| **13** | Exception handling                               | Merge-conflict resolution                 | Data file processor practice    |
| **14** | OOP: classes and objects                         | Git tags                                  | Object-oriented programs        |
| **15** | Inheritance and encapsulation                    | GitHub Pull Requests                      | Collaborative workflow          |
| **16** | Generators and decorators                        | GitHub Issues                             | Advanced Python practice        |
| **17** | Standard library and `pathlib`                   | `git rebase`                              | Repository maintenance          |
| **18** | NumPy arrays, indexing, slicing, vectorization   | Binary-file handling / `.gitignore`       | NumPy analytics practice        |
| **19** | Project architecture and package organization    | Branch-based project workflow             | Capstone preparation            |
| **20** | Capstone completion and optimization             | Production release/tagging                | **Final Capstone: PAAMS CLI**   |

---

# 📖 Daily Lessons

Each day contains the corresponding lesson material and practical learning activities.

| Day | Lesson                  | Notebook                                  |
| --: | ----------------------- | ----------------------------------------- |
|  01 | Python Basics           | `notebooks/day01_python_basics.ipynb`     |
|  02 | Variables & Data Types  | `notebooks/day02_variables_types.ipynb`   |
|  03 | Strings & Operators     | `notebooks/day03_strings_operators.ipynb` |
|  04 | Control Flow            | `notebooks/day04_control_flow.ipynb`      |
|  05 | Loops                   | Daily lesson material                     |
|  06 | Lists & Tuples          | `notebooks/day06_lists_tuples.ipynb`      |
|  07 | Sets & Dictionaries     | `notebooks/day07_sets_dictionaries.ipynb` |
|  08 | Comprehensions          | `notebooks/day08_comprehensions.ipynb`    |
|  09 | Functions               | Daily lesson material                     |
|  10 | Advanced Functions      | Daily lesson material                     |
|  11 | Modules                 | Daily lesson material                     |
|  12 | File I/O                | Daily lesson material                     |
|  13 | Exception Handling      | Daily lesson material                     |
|  14 | OOP Basics              | Daily lesson material                     |
|  15 | Advanced OOP            | Daily lesson material                     |
|  16 | Generators & Decorators | Daily lesson material                     |
|  17 | Standard Library        | Daily lesson material                     |
|  18 | NumPy                   | `notebooks/day18_numpy.ipynb`             |
|  19 | Project Architecture    | Daily lesson material                     |
|  20 | Capstone                | Capstone project                          |

---

# 🧪 Practical Projects

The repository contains progressively more challenging projects.

## 🇳🇵 Nepal Weather CLI

A practical Python project that retrieves weather information for locations in Nepal.

The project demonstrates:

- API requests
- JSON response handling
- User input
- Error handling
- CLI output
- Working with external data

Location selection can be extended to Nepal's districts and other supported administrative areas.

---

## 🔳 QR Code Generator

A small practical Python utility for generating QR codes.

Example:

```bash
python projects/qr_generator.py "https://example.com"
```

---

# 🚀 Final Capstone — PAAMS

## Personal Asset & Analytics Management System

**Status:** 🟡 Scaffolded / Partially Implemented

The final project applies concepts from the complete learning path in a multi-module Python application.

The project is designed around:

```text
Python
 ├── Models
 ├── Services
 ├── Utilities
 ├── Data Processing
 ├── Analytics
 └── CLI
```

The capstone provides practical experience with:

- Python modules
- Classes and objects
- File handling
- CSV/JSON data
- Functions
- Decorators
- Analytics
- CLI design
- Project architecture
- Git/GitHub workflow

---

# 🔀 Git & GitHub Learning Path

Git is introduced progressively throughout the 20 days.

### Fundamentals

```bash
git config
git init
git status
git add
git commit
git log
git diff
```

### Remote Repositories

```bash
git clone
git remote
git push
git pull
```

### Branching

```bash
git branch
git switch
git checkout
git merge
```

### Workspace Management

```bash
git stash
git restore
```

### Recovery

```bash
git revert
git reset
```

### Collaboration

```text
Branches
   ↓
Commits
   ↓
Push
   ↓
Pull Request
   ↓
Review
   ↓
Merge
```

### Advanced Git

```bash
git tag
git rebase
git cherry-pick
```

A complete reference is available in:

`docs/git-guide.md`

---

# 📚 Documentation

| Document                  | Purpose                                             |
| ------------------------- | --------------------------------------------------- |
| `README.md`               | Repository overview and learning roadmap            |
| `docs/learning-report.md` | Honest record of completed and remaining work       |
| `docs/git-guide.md`       | Progressive Git/GitHub command reference            |
| Daily README files        | Day-specific learning objectives and practical work |
| Project README files      | Project requirements and implementation guidance    |

---

# 🗂️ Legacy Material

Earlier notebooks and curriculum files that were duplicated, poorly sequenced, or replaced during the repository redesign are kept separately in:

```text
archive/
└── legacy-notebooks/
```

This keeps historical classroom material available without mixing it with the active learning path.

Advanced NumPy image-processing material is treated separately as optional reference material:

```text
notebooks/
└── optional/
    └── numpy_image_processing_reference.ipynb
```

---

# ⚡ Quick Start

## 1. Clone the repository

```bash
git clone <repository-url>
cd Python_Git_Class
```

## 2. Create a virtual environment

### Windows PowerShell

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 4. Open Jupyter

```bash
jupyter notebook
```

or:

```bash
jupyter lab
```

## 5. Run a project

For example:

```bash
python projects/qr_generator.py "https://example.com"
```

For the Nepal Weather CLI:

```bash
python projects/nepal-weather/main.py
```

---

# 🛠️ Recommended Development Workflow

Each practical task should follow a simple Git workflow:

```bash
git status

git add .

git commit -m "Add Python practice"

git push
```

For feature development:

```bash
git switch -c feature/my-feature

# Make changes

git add .
git commit -m "Add my feature"

git push -u origin feature/my-feature
```

---

# 📊 Repository Status

| Area                            | Status                                |
| ------------------------------- | ------------------------------------- |
| 20-Day Python curriculum        | ✅ Completed / Organized              |
| Git/GitHub learning path        | ✅ Completed / Organized              |
| Daily lesson structure          | ✅ Organized                          |
| Core notebooks                  | 🟡 Partially Prepared                 |
| Nepal Weather CLI               | ✅ Practical Project                  |
| QR Generator                    | ✅ Practical Project                  |
| Final Capstone                  | 🟡 Scaffolded / Partially Implemented |
| Advanced NumPy image processing | 🔵 Optional Reference                 |
| Legacy material                 | 📦 Archived                           |

> **Important:** Repository status is intentionally honest. Scaffolded projects and partially prepared materials are not presented as fully completed implementations.

---

# 🧑‍💻 Learning Philosophy

This repository focuses on **learning by doing**.

The progression is:

```text
Learn
  ↓
Practice
  ↓
Commit
  ↓
Build
  ↓
Debug
  ↓
Refactor
  ↓
Push to GitHub
  ↓
Build Projects
  ↓
Complete Capstone
```

Students are encouraged to write the code themselves, experiment with examples, make mistakes, debug errors, and use Git to track their progress.

---

# 📌 Current Repository Focus

The repository is not intended to be only a collection of lecture notes.

It is a **practical classroom workspace** combining:

- 📘 Python lessons
- 💻 Hands-on coding
- 📓 Jupyter notebooks
- 🔀 Git/GitHub practice
- 🧪 Practical projects
- 📊 NumPy exercises
- 🇳🇵 Nepal-focused API practice
- 🏗️ Project architecture
- 🚀 Final capstone development

---

# 📄 License

This project is licensed under the **MIT License**.
