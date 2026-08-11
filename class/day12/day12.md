# Day 12 — File Handling & Git Recovery

## Overview

Day 12 focused on working with **TXT, CSV, and JSON files** and understanding Git commands for safely undoing and recovering changes.

All Python hands-on practice was completed in `day12.ipynb`.

---

## Learning Objectives

* Read and write files using Python.
* Use context managers with `with open()`.
* Process CSV data.
* Read and write JSON data.
* Understand Git recovery and undo commands.
* Safely reverse committed changes.

---

## Topics Covered

### Python

* File handling
* `open()`
* File modes: `r`, `w`, `a`
* Context managers
* TXT files
* CSV files
* JSON files
* `csv.reader()`
* `csv.DictReader()`
* `csv.writer()`
* `csv.DictWriter()`
* `json.load()`
* `json.dump()`

### Git

* `git restore`
* `git revert`
* `git reset`
* Safe vs destructive undo operations

---

## Theory

### File Handling

Python uses `open()` to work with files.

The recommended approach is:

```text id="q7m4vx"
with open(...)
      ↓
Read / Write
      ↓
File automatically closes
```

Using a context manager prevents files from remaining open after the operation.

---

## CSV

CSV files store tabular data.

```text id="f3k8pn"
CSV
 ↓
Rows
 ↓
Columns
```

Python's built-in `csv` module provides tools for reading and writing CSV data.

---

## JSON

JSON is commonly used for structured data exchange.

```text id="m5x2qr"
Python Object
     ↓
json.dump()
     ↓
JSON File
     ↓
json.load()
     ↓
Python Object
```

---

# Git Recovery Commands

### `git restore`

Discard changes from a working file:

```bash id="n8c4ya"
git restore <file>
```

### `git revert`

Safely undo a previous commit by creating a **new commit**:

```bash id="v2r6mk"
git revert <commit>
```

Recommended for changes that have already been pushed/shared.

### `git reset`

Moves the current branch to another commit.

Common modes:

```bash id="p9w3tx"
git reset --soft <commit>
git reset --mixed <commit>
git reset --hard <commit>
```

⚠️ `--hard` can permanently discard uncommitted changes. Use it carefully.

---

# Python Practice

All exercises are available in:

```text id="c6y8qs"
day12.ipynb
```

Practice included:

* TXT file operations
* CSV reading and writing
* JSON serialization
* JSON deserialization
* Context managers
* File-based data processing

---

# Git Practice

Practice the recovery workflow:

```bash id="r4m7bz"
git status
git restore <file>

git add .
git commit -m "feat: add file handling exercises"

git revert HEAD
```

Observe how `git revert` creates a new commit instead of deleting existing history.

---

# Mini Task — Log Processor

Create a small log-processing program that:

1. Creates server status data.
2. Saves it to a JSON file.
3. Reads the JSON data.
4. Generates a TXT summary.
5. Commits the project to Git.

The implementation was completed in `day12.ipynb`.

---

## Day 12 Deliverables

```text id="t5n9kc"
class/
└── day12/
    └── day12.ipynb
```

* [x] TXT file handling
* [x] CSV processing
* [x] JSON processing
* [x] Context managers
* [x] `git restore`
* [x] `git revert`
* [x] `git reset`

---

## Expected Outcome

By the end of Day 12, the learner can safely process common file formats with Python and use Git recovery commands to undo or restore changes without unnecessarily damaging repository history.
