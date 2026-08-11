# Day 13 — Exception Handling & Git Merge Conflicts

## Overview

Day 13 focused on handling runtime errors safely in Python and learning how to identify and resolve Git merge conflicts.

**Milestone:** Complete the automated data file processor and report generator exercise.

All Python hands-on practice was completed in `day13.ipynb`.

---

## Learning Objectives

- Handle runtime errors using `try`, `except`, `else`, and `finally`.
- Catch specific exceptions.
- Raise exceptions when necessary.
- Understand Git merge conflicts.
- Resolve conflicts manually.
- Complete the data file processor exercise.

---

## Topics Covered

### Python

- `try`
- `except`
- `else`
- `finally`
- `raise`
- `FileNotFoundError`
- `ValueError`
- `KeyError`
- `ZeroDivisionError`
- Custom error handling

### Git

- Merge conflicts
- Conflict markers
- Manual conflict resolution
- `git add`
- Merge commits

---

## Theory

### Exception Handling

Exception handling prevents unexpected runtime errors from stopping a program.

```text id="p4m8xs"
try
 ↓
Error?
 ├── Yes → except
 └── No  → else
        ↓
     finally
```

Use **specific exceptions** whenever possible instead of catching every error with a generic `Exception`.

---

## Raising Exceptions

The `raise` statement allows a program to intentionally report invalid data or conditions.

```text id="z7q3nb"
Invalid Condition
       ↓
     raise
       ↓
Exception Handler
```

---

# Git Merge Conflicts

A conflict can occur when different branches modify the same part of a file.

Git may insert:

```text id="m5v2kc"
<<<<<<< HEAD
Current Branch
=======
Other Branch
>>>>>>> feature
```

### Conflict Resolution

```text id="x8n4qa"
Merge
 ↓
Conflict
 ↓
Open File
 ↓
Choose Correct Code
 ↓
Remove Conflict Markers
 ↓
git add
 ↓
git commit
```

---

# Python Practice

All exercises are available in:

```text id="c9r6tw"
day13.ipynb
```

Practice included:

- Exception handling
- File errors
- JSON errors
- Validation
- `raise`
- `try/except/else/finally`

---

# Data File Processor Exercise

Build an automated processor that:

1. Reads transaction data from JSON.
2. Validates records.
3. Handles invalid or missing data.
4. Calculates transaction totals.
5. Exports processed data to CSV.
6. Reports errors safely.

The implementation was completed in `day13.ipynb`.

---

# Git Practice

Simulate a conflict using two branches, modify the same section of a file, and merge them.

After resolving the conflict:

```bash id="k3w7pf"
git add .
git commit -m "fix: resolve merge conflict"
git push
```

---

## Day 13 Deliverables

```text id="v6q2ym"
class/
└── day13/
    └── day13.ipynb
```

- [x] Exception handling
- [x] Specific exceptions
- [x] `raise`
- [x] JSON/CSV processing
- [x] Data file processor practice
- [x] Git merge conflicts
- [x] Manual conflict resolution

---

## Expected Outcome

By the end of Day 13, the learner can build fault-tolerant Python programs, process invalid data safely, complete the data file processor exercise, and resolve Git merge conflicts confidently.
