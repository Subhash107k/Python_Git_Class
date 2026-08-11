# Day 6 — Lists, Tuples & Git Remote Management

## Overview

Day 6 focused on Python sequence data types—**lists and tuples**—and basic Git remote synchronization.

All Python hands-on practice was completed in `day6.ipynb`.

---

## Learning Objectives

* Understand lists and tuples.
* Work with mutable and immutable sequences.
* Use common list methods.
* Sort lists using custom `key` functions.
* Understand tuple packing and unpacking.
* Use nested sequence indexing.
* Understand `git fetch` vs `git pull`.
* Synchronize local work with GitHub.

---

## Topics Covered

### Python

* Lists `[]`
* Tuples `()`
* Indexing and slicing
* List mutability
* Tuple immutability
* `.append()`
* `.insert()`
* `.remove()`
* `.pop()`
* `.extend()`
* `.sort()`
* `.reverse()`
* Custom sorting with `key=`
* Tuple packing and unpacking
* Extended unpacking
* Nested lists and tuples

### Git

* `git fetch`
* `git pull`
* `git add`
* `git commit`
* `git push`

---

## Theory

### Lists vs Tuples

| List                              | Tuple                             |
| --------------------------------- | --------------------------------- |
| Mutable                           | Immutable                         |
| Uses `[]`                         | Uses `()`                         |
| Can be modified                   | Cannot be modified after creation |
| Suitable for changing collections | Suitable for fixed data           |

Example concept:

```text id="x7x0g2"
List  → [1, 2, 3] → Can change
Tuple → (1, 2, 3) → Cannot change
```

---

## Tuple Unpacking

Tuple values can be assigned to multiple variables:

```text id="o7l5p8"
coordinates = (x, y, z)

x, y, z = coordinates
```

Python also supports extended unpacking:

```text id="9ry6is"
first, *middle, last = values
```

---

## Custom Sorting

Python's `sort()` and `sorted()` support custom sorting logic using the `key` parameter.

This allows lists to be sorted based on:

* Length
* Numeric distance
* Scores
* Names
* Object attributes
* Other calculated values

---

## Python Practice

All exercises are available in:

```text id="o3y5ha"
day6.ipynb
```

Practice included:

* List operations
* Custom sorting
* Tuple operations
* Tuple unpacking
* Extended unpacking
* Nested sequence indexing
* Student data sorting

---

# Git Remote Management

## `git fetch`

Downloads changes and history from a remote repository **without automatically merging them**.

```bash id="9s0y5f"
git fetch origin
```

Think of it as:

```text id="q0w4gn"
GitHub → Local Remote Tracking Data
```

---

## `git pull`

Fetches remote changes and integrates them into the current branch.

```bash id="m8e8bw"
git pull origin main
```

Think of it as:

```text id="y0k7sl"
GitHub
  ↓
Fetch
  ↓
Merge / Integrate
  ↓
Current Branch
```

### Key Difference

```text id="bjxv72"
git fetch → Download updates only

git pull  → Download + integrate updates
```

---

## Git Practice

After completing the Day 6 work:

```bash id="1q2g8n"
git fetch origin
git pull origin main
```

Then commit and push:

```bash id="p2ph6f"
git add .
git commit -m "feat: add list and tuple practice"
git push origin main
```

---

# Mini Task — Student Roster

Create a student roster using a list of `(name, score)` tuples.

Requirements:

* Store student names and scores.
* Sort students by score in descending order.
* Display the sorted results clearly.
* Commit the completed work.
* Push it to GitHub.

The implementation was completed in `day6.ipynb`.

---

## Day 6 Deliverables

```text id="f0zv4p"
class/
└── day6/
    └── day6.ipynb
```

* [x] Lists
* [x] Tuples
* [x] List methods
* [x] Custom sorting
* [x] Tuple unpacking
* [x] Nested sequences
* [x] `git fetch`
* [x] `git pull`
* [x] GitHub synchronization

---

## Expected Outcome

By the end of Day 6, the learner can work with Python lists and tuples, organize sequence data using sorting and unpacking, and synchronize a local Git repository with GitHub using `fetch`, `pull`, and `push`.
