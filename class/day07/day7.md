# Day 7 — Sets, Dictionaries & Nested Data Structures

## Overview

Day 7 focused on Python **sets, dictionaries, and nested data structures**, along with Git feature-branch workflow.

All Python hands-on practice was completed in `day7.ipynb`.

---

## Learning Objectives

* Understand sets and unique collections.
* Perform union, intersection, and difference operations.
* Create and manipulate dictionaries.
* Access dictionary data safely.
* Iterate through dictionary keys, values, and items.
* Work with nested lists and dictionaries.
* Create isolated Git feature branches.

---

## Topics Covered

### Python

#### Sets

* Unique collections
* `.add()`
* `.remove()`
* `.discard()`
* `.pop()`
* Union `|`
* Intersection `&`
* Difference `-`

#### Dictionaries

* Key-value pairs
* Dictionary keys and values
* `.get()`
* `.keys()`
* `.values()`
* `.items()`
* `.pop()`
* `del`
* Dictionary iteration

#### Nested Data

* Lists inside dictionaries
* Dictionaries inside dictionaries
* Accessing deeply nested values
* Iterating over nested structures

---

## Theory

### Sets

A set stores **unique elements**. Duplicate values are automatically removed.

```text id="n9y1pi"
[1, 2, 2, 3, 3]
       ↓
   {1, 2, 3}
```

Common operations:

```text id="l7n8bq"
Union        → All elements
Intersection → Common elements
Difference   → Elements in one set but not another
```

---

## Dictionaries

A dictionary stores data as **key-value pairs**.

```text id="1yq7qf"
Key → Value
```

Example structure:

```text id="6qz3hv"
student
 ├── name
 ├── age
 ├── courses
 └── active
```

The `.get()` method can safely retrieve a value while providing a default when the key does not exist.

---

## Nested Data Structures

Python allows collections to contain other collections.

For example:

```text id="5i6qkg"
Students
 ├── Student 1
 │    ├── Name
 │    └── Courses
 └── Student 2
      ├── Name
      └── Courses
```

This structure is commonly used when working with real-world data.

---

## Python Practice

All exercises are available in:

```text id="c2aq4w"
day7.ipynb
```

Practice included:

* Set operations
* Dictionary operations
* Dictionary iteration
* Nested dictionaries
* Nested lists
* Data lookup
* Student database example

---

# Git Feature Branch

Day 7 introduced a dedicated feature branch for data-structure work.

Create and switch to the branch:

```bash id="qj7qz4"
git switch -c feature/data-structures
```

Check the active branch:

```bash id="r4qf3z"
git branch
```

Stage and commit the completed work:

```bash id="8qv4af"
git add .
git commit -m "feat: add sets and dictionary practice"
```

---

# Mini Task — Inventory Manager

Create an inventory structure containing:

* Item name
* Stock quantity
* Price
* Supplier

The program should support:

* Adding stock.
* Calculating total inventory value.
* Removing out-of-stock items.

The implementation was completed in `day7.ipynb`.

---

## Day 7 Deliverables

```text id="xk4qkl"
class/
└── day7/
    └── day7.ipynb
```

* [x] Sets
* [x] Set operations
* [x] Dictionaries
* [x] Dictionary methods
* [x] Nested data structures
* [x] Data iteration
* [x] Feature branches
* [x] Git commit workflow

---

## Expected Outcome

By the end of Day 7, the learner can work with sets, dictionaries, and nested data structures and manage related development work using a dedicated Git feature branch.
