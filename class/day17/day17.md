# Day 17 — Standard Library, Context Managers & Advanced Git

## Learning Objectives

* Use useful Python standard-library modules.
* Understand context managers and `with`.
* Create basic custom context managers.
* Understand `git rebase` and `git cherry-pick`.
* Practice safe Git history management.

---

## Topics Covered

### 1. Python Standard Library

* `pathlib` — filesystem and file paths.
* `datetime` — dates and times.
* `math` — mathematical operations.
* `random` — random values and selections.

### 2. Context Managers

* Using `with` for safe resource management.
* `__enter__()` and `__exit__()`.
* `@contextmanager` from `contextlib`.
* Why context managers are useful for files, connections, and cleanup tasks.

### 3. Advanced Git

* `git rebase` — create a cleaner, linear history.
* `git cherry-pick` — apply a specific commit to another branch.
* Difference between **merge** and **rebase**.
* Safe Git practices when rewriting history.

---

## Theory & Classroom Explanation

### Standard Library

Python provides many built-in modules without requiring external installation.

```python
from pathlib import Path
from datetime import datetime
import math
import random
```

Example:

```python
path = Path(".")
print(datetime.now())
print(math.sqrt(25))
print(random.randint(1, 10))
```

### Context Managers

A context manager handles setup and cleanup automatically.

```python
with open("data.txt", "r") as file:
    data = file.read()
```

Custom context managers can be created using:

```python
__enter__()
__exit__()
```

or:

```python
@contextmanager
```

---

## Git: Rebase vs Merge

### Merge

Combines two branches while preserving their history.

```bash
git switch main
git merge feature/example
```

### Rebase

Moves feature commits on top of the latest `main` history.

```bash
git switch feature/example
git rebase main
```

> **Important:** Avoid rebasing commits that have already been pushed to a shared/public branch.

### Cherry-Pick

Applies one specific commit to the current branch.

```bash
git cherry-pick <commit-hash>
```

---

## Git Practice

```bash
git switch feature/example
git rebase main

git switch main
git cherry-pick <commit-hash>

git push origin main
```

---

## Mini Task

Create `log_cleaner.py` that:

1. Uses `pathlib` to work with `.log` files.
2. Uses a context manager for cleanup logging.
3. Creates and removes sample log files.
4. Commit and push the script to GitHub.

### Commit

```bash
git add log_cleaner.py
git commit -m "feat: add pathlib log cleaner and context manager"
git push origin main
```

---

## Expected Outcome

Student understands Python standard-library utilities, context managers, and advanced Git operations such as **rebase** and **cherry-pick**.
