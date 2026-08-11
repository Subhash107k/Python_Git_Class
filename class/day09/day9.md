# Day 9 — Functions, Parameters, Return Values & Git Stash

## Overview

Day 9 focused on creating **reusable Python functions** and managing temporary uncommitted changes with Git Stash.

All Python hands-on practice was completed in `day9.ipynb`.

---

## Learning Objectives

* Define reusable functions using `def`.
* Understand parameters and arguments.
* Use positional, keyword, and default arguments.
* Return single and multiple values.
* Understand local and global scope.
* Use `git stash` to temporarily save changes.

---

## Topics Covered

### Python

* Function definition
* Parameters vs arguments
* Positional arguments
* Keyword arguments
* Default parameters
* `return`
* Multiple return values
* Local scope
* Global scope
* Basic type hints
* DRY principle

### Git

* `git stash`
* `git stash list`
* `git stash pop`
* `git stash apply`
* Managing uncommitted changes

---

## Theory

### Functions

Functions organize reusable logic into independent blocks.

```text id="z5f8x1"
Input
  ↓
Function
  ↓
Processing
  ↓
Return Value
```

Functions help make programs:

* Reusable
* Organized
* Easier to test
* Easier to maintain

---

## Parameters & Arguments

```text id="c4k9mv"
Parameter → Variable defined by the function

Argument  → Actual value passed to the function
```

Common argument styles:

* Positional
* Keyword
* Default

---

## Multiple Return Values

Python can return multiple values from a function.

Conceptually:

```text id="r8v3dz"
Function
   ↓
Value 1 + Value 2
   ↓
Tuple
   ↓
Unpacking
```

---

## Variable Scope

### Local Scope

A variable created inside a function normally exists only within that function.

### Global Scope

A variable created outside functions can be accessed from functions.

```text id="q2m6ws"
Global Scope
     ↓
  Function
     ↓
Local Scope
```

The `global` keyword exists but should generally be used carefully.

---

# Python Practice

All exercises are available in:

```text id="x8p1ka"
day9.ipynb
```

Practice included:

* Function creation
* Parameters
* Default arguments
* Keyword arguments
* Return values
* Multiple return values
* Variable scope
* Type hints

---

# Git Stash

`git stash` temporarily saves uncommitted changes so the working directory can be cleaned without committing incomplete work.

### Save Changes

```bash id="v4c7nm"
git stash
```

### View Stashes

```bash id="k6x2qp"
git stash list
```

### Restore Changes

```bash id="d9w5rt"
git stash pop
```

Or apply without removing the stash:

```bash id="j3m8fs"
git stash apply
```

### Workflow

```text id="a7n2cx"
Modified Files
     ↓
git stash
     ↓
Clean Working Directory
     ↓
Switch / Update / Work
     ↓
git stash pop
     ↓
Continue Development
```

---

# Git Practice

After restoring the changes:

```bash id="s5q1vh"
git add .
git commit -m "feat: add reusable Python functions"
git push
```

---

# Mini Task — Geometry Helper

Create functions for:

* Circle area and circumference.
* Rectangle area and perimeter.
* Default function arguments.
* Multiple return values.

Practice `git stash` while making changes, restore the work, then commit it.

The implementation was completed in `day9.ipynb`.

---

## Day 9 Deliverables

```text id="m2r7bk"
class/
└── day9/
    └── day9.ipynb
```

* [x] Functions
* [x] Parameters and arguments
* [x] Default arguments
* [x] Return values
* [x] Multiple returns
* [x] Variable scope
* [x] `git stash`
* [x] Git commit workflow

---

## Expected Outcome

By the end of Day 9, the learner can create reusable Python functions and safely manage temporary uncommitted work using Git Stash.
