# 🐍 Python + Git Zero-to-Hero Program

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Git Version Control](https://img.shields.io/badge/Git-Professional-orange.svg)](https://git-scm.com/)
[![Author: Subhash107k](https://img.shields.io/badge/Author-Subhash107k-brightgreen.svg)](https://github.com/Subhash107k)

Welcome to the **Python + Git Zero-to-Hero Practical Learning Program** repository! This curriculum takes a beginner from **absolute Python fundamentals to practical intermediate/advanced software development**, while teaching **Git and GitHub version control from scratch to professional team workflows**.

---

## 👨‍💻 Author & Maintainer

Developed and curated by **[Subhash107k](https://github.com/Subhash107k)**.

- **GitHub Profile**: [@Subhash107k](https://github.com/Subhash107k)
- **Project Repository**: [Python_Git_Class](https://github.com/Subhash107k/Python_Git_Class)

---

## 📌 Course Highlights

- **Practical Classroom Focus**: Built around real code, actual output, hands-on debugging, and portfolio-grade projects.
- **Integrated Git & GitHub**: Git is taught starting **Day 1** and used daily to stage, commit, branch, merge, and push Python classroom work.
- **Progressive Projects**: Contains 4 milestone projects (CLI Assistant, Data File Processor, OOP Inventory Analytics Engine, and Capstone PAAMS CLI Application).
- **Comprehensive Deliverables**: Available in both Markdown lessons (`day1.md`–`day20.md`) and interactive Jupyter Notebooks (`day1.ipynb`–`day20.ipynb`).

---

## 🗺️ Curriculum Map

| Day | Python Topic | Git / GitHub Topic | Main Deliverables |
| :---: | :--- | :--- | :--- |
| **01** | Python Setup, Interpreter, Syntax, Comments | `git config`, `git init` | [`day1.md`](day1.md) \| [`day1.ipynb`](day1.ipynb) |
| **02** | Variables, Data Types, Casting, `input()` | 3-Stage Model (`add`, `commit`) | [`day2.md`](day2.md) \| [`day2.ipynb`](day2.ipynb) |
| **03** | Operators, Strings, Slicing, Methods | `git status`, `git log`, `git diff` | [`day3.md`](day3.md) \| [`day3.ipynb`](day3.ipynb) |
| **04** | Control Flow (`if`/`elif`/`else`), Logic | Branching Basics (`switch -c`) | [`day4.md`](day4.md) \| [`day4.ipynb`](day4.ipynb) |
| **05** | Loops (`for`/`while`), Control Statements | Remote Setup (`git push`) | 🚀 **PROJECT 1**: CLI Tool |
| **06** | Lists, Tuples, Custom Sort Keys | Remote Syncing (`git pull`) | [`day6.md`](day6.md) \| [`day6.ipynb`](day6.ipynb) |
| **07** | Sets, Dictionaries, Nested Structs | Feature Branch Isolation | [`day7.md`](day7.md) \| [`day7.ipynb`](day7.ipynb) |
| **08** | Comprehensions, Memory Benchmark | `.gitignore` & Repository Docs | [`day8.md`](day8.md) \| [`day8.ipynb`](day8.ipynb) |
| **09** | Functions (`def`), Parameters, Scope | Workspace Management (`git stash`) | [`day9.md`](day9.md) \| [`day9.ipynb`](day9.ipynb) |
| **10** | `*args`, `**kwargs`, Lambdas, `map`/`filter` | Branch Merging (`git merge`) | [`day10.md`](day10.md) \| [`day10.ipynb`](day10.ipynb) |
| **11** | Modules, `if __name__ == '__main__':` | Virtual Envs (`.venv`) | [`day11.md`](day11.md) \| [`day11.ipynb`](day11.ipynb) |
| **12** | File I/O (CSV, JSON), Context Managers | Recovery (`restore`, `revert`) | [`day12.md`](day12.md) \| [`day12.ipynb`](day12.ipynb) |
| **13** | Exception Handling (`try`/`except`/`finally`) | Conflict Resolution Markers | 🚀 **PROJECT 2**: File Processor |
| **14** | OOP Basics: Classes, Objects, `__init__` | Version Tagging (`git tag -a`) | [`day14.md`](day14.md) \| [`day14.ipynb`](day14.ipynb) |
| **15** | Advanced OOP: Inheritance, Encapsulation | GitHub Pull Request Workflows | [`day15.md`](day15.md) \| [`day15.ipynb`](day15.ipynb) |
| **16** | Generators (`yield`), Decorators | Issue Tracking (`Fixes #id`) | [`day16.md`](day16.md) \| [`day16.ipynb`](day16.ipynb) |
| **17** | Standard Library (`pathlib`), Contexts | Advanced Git (`rebase`) | [`day17.md`](day17.md) \| [`day17.ipynb`](day17.ipynb) |
| **18** | NumPy Arrays, Vectorization, Indexing | Binary File Ignore (`*.npy`) | 🚀 **PROJECT 3**: Analytics Engine |
| **19** | Portfolio Architecture & Package Layout | Branch Scaffolding | [`day19.md`](day19.md) \| [`day19.ipynb`](day19.ipynb) |
| **20** | Capstone Completion & Optimization | Production Release Tag (`v3.0`) | 🎓 **FINAL CAPSTONE**: PAAMS CLI |

---

## 🛠️ Progressive Project Milestones

1. **Project 1 (End of Day 5)**: Interactive CLI Calculator & Profile Assistant (Variables, logic, loops, basic remote push).
2. **Project 2 (End of Day 13)**: Automated Data File Processor & Report Generator (Functions, CSV/JSON, exception handling, conflict resolution).
3. **Project 3 (End of Day 18)**: OOP Inventory System + NumPy Analytics Engine (Classes, inheritance, encapsulation, NumPy vectorization, `.npy` binary cache).
4. **Final Capstone (End of Day 20)**: Personal Asset & Analytics Management System (PAAMS CLI) (Multi-module package, OOP domain models, NumPy analytics engine, custom decorators, GitHub Releases).

---

## 📁 Repository Structure

```text
Python_Git_Class/
│── LICENSE                            # MIT Open Source License
│── README.md                          # Project Documentation
│── 20_Day_Python_Git_Curriculum.md    # Master Curriculum Syllabus
│── code_practices_workbook.md         # Hands-on Practice & Debugging Workbook
│── day1.md ... day20.md              # Daily Markdown Lesson Guides
│── day1.ipynb ... day20.ipynb        # Interactive Jupyter Notebooks
└── .gitignore                         # Configured Git Ignore Rules
```

---

## 🚀 Getting Started

### 1. Clone the Repository
```bash
git clone https://github.com/Subhash107k/Python_Git_Class.git
cd Python_Git_Class
```

### 2. Create and Activate Virtual Environment
```bash
# Create virtual environment
python -m venv .venv

# Activate on Windows PowerShell:
.venv\Scripts\Activate.ps1
# Activate on Git Bash / Linux / macOS:
source .venv/bin/activate
```

### 3. Install Dependencies & Launch Jupyter Notebooks
```bash
pip install -r requirements.txt
jupyter notebook
```

---

## 📄 License

This repository is licensed under the **[MIT License](LICENSE)**. Created by **[Subhash107k](https://github.com/Subhash107k)**. Feel free to use, modify, and distribute for personal learning or classroom teaching.
