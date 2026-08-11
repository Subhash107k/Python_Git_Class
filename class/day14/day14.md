# Day 14 — Object-Oriented Programming & Git Tagging

## Overview

Day 14 introduced **Object-Oriented Programming (OOP)** and Git release tagging.

All Python hands-on practice was completed in `day14.ipynb`.

---

## Learning Objectives

* Understand classes and objects.
* Create constructors using `__init__()`.
* Use `self`, instance attributes, and class attributes.
* Create instance methods.
* Customize object output with `__str__()`.
* Create and manage Git release tags.

---

## Topics Covered

### Python OOP

* Classes and objects
* `__init__()`
* `self`
* Instance attributes
* Class attributes
* Instance methods
* `__str__()`
* Basic data validation
* Object state and behavior

### Git

* Git tags
* Annotated tags
* Versioning releases
* Pushing tags to GitHub

---

## Theory

### Classes & Objects

A **class** is a blueprint, while an **object** is an instance created from that blueprint.

```text id="x6m2pk"
Class
  ↓
Blueprint
  ↓
Object 1
Object 2
Object 3
```

### Object Structure

```text id="r8v4qa"
Object
 ├── Attributes → State
 └── Methods    → Behavior
```

`__init__()` initializes an object's attributes, while `self` refers to the current object instance.

---

## String Representation

`__str__()` controls how an object is displayed when converted to a string or printed.

This makes object output easier to read and understand.

---

# Python Practice

All exercises are available in:

```text id="k5n9cz"
day14.ipynb
```

Practice included:

* Creating classes
* Creating objects
* Constructors
* Instance/class attributes
* Methods
* Object validation
* `__str__()`

---

# Git Tagging

Git tags mark important points in repository history, such as releases.

### Create an Annotated Tag

```bash id="m7q3vx"
git tag -a v1.0 -m "Release Version 1.0"
```

### View Tags

```bash id="p4w8na"
git tag
```

### Push Tags to GitHub

```bash id="c9r2yf"
git push origin main
git push origin --tags
```

---

## Release Workflow

```text id="u3k6mp"
Complete Feature
      ↓
Commit
      ↓
Release Milestone
      ↓
Create Git Tag
      ↓
Push Tag to GitHub
```

---

# Mini Task — Bank Account

Create a `BankAccount` class with:

* Account number
* Owner name
* Balance
* Deposit
* Withdrawal
* Balance checking

Test multiple objects, commit the implementation, and create a `v1.1` tag.

The implementation was completed in `day14.ipynb`.

---

## Day 14 Deliverables

```text id="s8v5qt"
class/
└── day14/
    └── day14.ipynb
```

* [x] Classes
* [x] Objects
* [x] Constructors
* [x] Instance/class attributes
* [x] Methods
* [x] `__str__()`
* [x] Git tags
* [x] Release versioning

---

## Expected Outcome

By the end of Day 14, the learner can design basic Python classes, create objects with reusable behavior, manage object state, and mark important project milestones using Git release tags.
