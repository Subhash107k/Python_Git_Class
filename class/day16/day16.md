# Day 16 — Iterators, Generators, Decorators & GitHub Issues

## Overview

Day 16 introduced advanced Python techniques for **efficient data processing and dynamic function behavior**, along with GitHub Issues for task tracking.

All detailed Python practice was completed in `day16.ipynb`.

---

## Learning Objectives

* Understand iterables and iterators.
* Use `iter()` and `next()`.
* Create memory-efficient generators with `yield`.
* Understand and create decorators.
* Track development tasks using GitHub Issues.
* Link commits to GitHub Issues.

---

## Topics Covered

### Python

* Iterables
* Iterators
* `iter()`
* `next()`
* `__iter__()`
* `__next__()`
* Generator functions
* `yield`
* Generator expressions
* Decorators
* Higher-order functions
* Wrapper functions
* `*args` and `**kwargs`

### GitHub

* GitHub Issues
* Issue numbers
* Linking commits to Issues
* `Fixes #number`
* `Closes #number`

---

## Short Examples

### 1. Iterator

An iterator produces values one at a time.

```python id="k5q8wr"
numbers = iter([10, 20, 30])

print(next(numbers))
print(next(numbers))
```

Output:

```text id="v2m6qa"
10
20
```

---

### 2. Generator

A generator uses `yield` to produce values lazily.

```python id="r8x3np"
def count_numbers(limit):
    for number in range(1, limit + 1):
        yield number


for number in count_numbers(3):
    print(number)
```

Generators are useful when working with large datasets because values are produced **on demand**.

---

### 3. Decorator

A decorator adds behavior to an existing function.

```python id="q4n7zc"
def logger(func):
    def wrapper():
        print("Starting...")
        func()
        print("Finished...")
    return wrapper


@logger
def hello():
    print("Hello Python!")


hello()
```

---

# Python Practice

All detailed exercises are available in:

```text id="m6w2pk"
day16.ipynb
```

Practice included:

* Iterators
* `iter()` / `next()`
* Generator functions
* `yield`
* Generator expressions
* Decorators
* Function wrappers

---

# GitHub Issues

GitHub Issues can be used to track bugs, features, and development tasks.

### Example Issue

```text id="n3c9va"
Issue #1
Optimize memory using generator stream
```

After implementing the task, reference the issue in the commit:

```bash id="x7f4qm"
git add .
git commit -m "feat: add generator stream (Fixes #1)"
git push origin main
```

Using `Fixes #1` or `Closes #1` can automatically close the linked issue when the commit reaches the repository's default branch, depending on GitHub's issue-closing behavior.

---

## Workflow

```text id="u8p5rx"
GitHub Issue
     ↓
Create Feature
     ↓
Write Code
     ↓
Commit with Issue ID
     ↓
Push to GitHub
     ↓
Issue Updated / Closed
```

---

# Mini Task — Logging Decorator

Create a decorator that:

* Displays function arguments.
* Executes the function.
* Displays the returned result.

Apply it to a `multiply(a, b)` function and link the work to a GitHub Issue.

The implementation was completed in `day16.ipynb`.

---

## Day 16 Deliverables

```text id="b4k9ws"
class/
└── day16/
    └── day16.ipynb
```

* [x] Iterators
* [x] Generators
* [x] `yield`
* [x] Generator expressions
* [x] Decorators
* [x] GitHub Issues
* [x] Issue-linked commits

---

## Expected Outcome

By the end of Day 16, the learner can process data efficiently with generators, extend functions using decorators, and track development tasks through GitHub Issues.
