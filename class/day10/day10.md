# Day 10 — Advanced Functions & Git Branch Merging

## Overview

Day 10 focused on **advanced Python function techniques** and merging feature branches into the main Git branch.

All Python hands-on practice was completed in `day10.ipynb`.

---

## Learning Objectives

* Use `*args` for variable positional arguments.
* Use `**kwargs` for variable keyword arguments.
* Create simple lambda functions.
* Use `map()` and `filter()`.
* Merge feature branches into `main`.
* Delete merged branches and keep the repository clean.

---

## Topics Covered

### Python

* `*args`
* `**kwargs`
* Lambda expressions
* `map()`
* `filter()`
* Higher-order functions
* Dynamic function arguments

### Git

* `git merge`
* Feature branch integration
* `git branch -d`
* Pulling before merging
* Pushing merged changes

---

## Theory

### `*args` and `**kwargs`

```text id="w7f4qx"
*args
  ↓
Multiple positional arguments
  ↓
Tuple

**kwargs
  ↓
Multiple keyword arguments
  ↓
Dictionary
```

They allow functions to accept a flexible number of arguments.

---

## Lambda Functions

A lambda is a small anonymous function.

```text id="q8k2pn"
lambda input: expression
```

They are commonly used with functions such as:

* `map()`
* `filter()`
* `sorted()`

---

## `map()` vs `filter()`

```text id="v2r6hs"
map()
 ↓
Transform each item

filter()
 ↓
Keep items matching a condition
```

---

# Python Practice

All exercises are available in:

```text id="f6x3mv"
day10.ipynb
```

Practice included:

* `*args`
* `**kwargs`
* Lambda functions
* `map()`
* `filter()`
* Dynamic function arguments

---

# Git Branch Merging

Day 10 introduced merging a completed feature branch into `main`.

### Switch to Main

```bash id="n8j4qa"
git switch main
git pull origin main
```

### Merge Feature Branch

```bash id="p5r2kx"
git merge feature/data-structures
```

### Delete Merged Branch

```bash id="c7m3vz"
git branch -d feature/data-structures
```

### Push Main

```bash id="h4w9ls"
git push origin main
```

---

## Git Workflow

```text id="u6q2yb"
Feature Branch
      ↓
Complete Work
      ↓
Commit
      ↓
Switch to main
      ↓
Merge
      ↓
Delete Feature Branch
      ↓
Push main
```

---

# Mini Task — Flexible Formatter

Create a function that:

* Accepts a title.
* Accepts a variable number of items using `*args`.
* Accepts dynamic tax information using `**kwargs`.
* Calculates and formats the final result.

The implementation was completed in `day10.ipynb`.

---

## Day 10 Deliverables

```text id="r9k5cx"
class/
└── day10/
    └── day10.ipynb
```

* [x] `*args`
* [x] `**kwargs`
* [x] Lambda functions
* [x] `map()`
* [x] `filter()`
* [x] Branch merging
* [x] Branch cleanup
* [x] GitHub push

---

## Expected Outcome

By the end of Day 10, the learner can create flexible Python functions using `*args` and `**kwargs`, apply lambdas with `map()` and `filter()`, and safely merge completed feature work into `main`.
