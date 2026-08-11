# Day 8 — Comprehensions, Benchmarking & GitHub Collaboration

## Overview

Day 8 focused on Python **comprehensions, basic performance benchmarking, and repository documentation**.

All Python hands-on practice was completed in `day8.ipynb`.

---

## Learning Objectives

* Understand list and dictionary comprehensions.
* Create collections using concise Python syntax.
* Compare list and tuple memory usage.
* Measure basic execution performance.
* Create and maintain a professional `README.md`.
* Configure `.gitignore`.
* Keep repositories clean and organized.

---

## Topics Covered

### Python

* List comprehensions
* Dictionary comprehensions
* Conditional comprehensions
* `sys.getsizeof()`
* Basic timing with `time`
* List vs tuple memory usage

### Git & GitHub

* GitHub Markdown
* `README.md`
* `.gitignore`
* Ignoring Python-generated files
* Commit and push workflow

---

## Theory

### Comprehensions

Comprehensions provide a concise way to create collections.

```text id="7w3p8n"
Traditional Loop
      ↓
Multiple Lines

Comprehension
      ↓
Compact Expression
```

Common forms:

```text id="2z9n5b"
List       → [expression for item in iterable]
Dictionary → {key: value for item in iterable}
```

---

## Performance Benchmarking

Python provides tools for basic performance and memory measurements.

### Memory

```text id="y2w8qk"
sys.getsizeof()
       ↓
Object Memory Size
```

### Execution Time

```text id="j6c4rm"
time
 ↓
Measure Start
 ↓
Run Code
 ↓
Measure End
 ↓
Calculate Duration
```

Benchmarking helps understand the practical differences between data structures.

---

# Repository Documentation

## `.gitignore`

A `.gitignore` file prevents unnecessary files from being tracked by Git.

Common Python entries:

```text id="0n4m2w"
__pycache__/
*.pyc
.venv/
.vscode/
.DS_Store
```

This keeps generated files, virtual environments, and local configuration out of the repository.

---

## README.md

Day 8 introduced structured GitHub documentation using Markdown.

A good README can contain:

* Project description
* Learning objectives
* Repository structure
* Technologies used
* Projects
* Learning progress
* Setup instructions

---

# Python Practice

All exercises are available in:

```text id="9u6m1x"
day8.ipynb
```

Practice included:

* List comprehensions
* Dictionary comprehensions
* Conditional comprehensions
* List vs tuple memory comparison
* Basic performance measurement

---

# GitHub Practice

Create `.gitignore` and update the repository README.

Check changes:

```bash id="8z1f3c"
git status
```

Stage the files:

```bash id="5y4x2v"
git add .
```

Commit:

```bash id="m8r7qp"
git commit -m "docs: improve README and add Python gitignore"
```

Push:

```bash id="c9v2kd"
git push
```

---

# Mini Task — Comprehension Challenge

Create a program that:

1. Generates cubes of odd numbers from 1–20 using dictionary comprehension.
2. Filters product prices above 20.
3. Applies a 10% tax using list comprehension.

The implementation was completed in `day8.ipynb`.

---

## Day 8 Deliverables

```text id="p3w7ka"
class/
└── day8/
    └── day8.ipynb

.gitignore
README.md
```

* [x] List comprehensions
* [x] Dictionary comprehensions
* [x] Performance benchmarking
* [x] README documentation
* [x] `.gitignore`
* [x] Git commit and push

---

## Expected Outcome

By the end of Day 8, the learner can use Python comprehensions, perform basic memory benchmarking, and maintain a clean, documented GitHub repository.
