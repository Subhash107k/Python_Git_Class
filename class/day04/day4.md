# Day 4 — Conditional Logic, Decision Making & Git Branching

## Overview

Day 4 introduced **decision-making in Python** and the fundamentals of **Git branching**.

The Python section focused on controlling program flow with `if`, `elif`, and `else`, evaluating Boolean expressions, working with truthy and falsy values, and combining multiple conditions using logical operators.

The Git section introduced branches as isolated development environments. Branching allows new features and experiments to be developed without directly modifying the stable `main` branch.

All Python hands-on exercises were completed in the Day 4 Jupyter Notebook.

---

# Learning Objectives

By the end of Day 4, the learner can:

* Explain how conditional statements control program execution.
* Use `if`, `elif`, and `else` to implement decisions.
* Work with Boolean expressions.
* Understand Python truthy and falsy values.
* Combine conditions using `and`, `or`, and `not`.
* Build nested conditional logic.
* Validate basic user input using conditional statements.
* Follow Python's indentation rules.
* Explain the purpose of Git branches.
* List existing branches.
* Create a new branch.
* Switch between branches.
* Create and switch to a branch using a single command.
* Understand how branches protect stable project code.

---

# Topics Covered

## Python

1. Conditional Statements

   * `if`
   * `elif`
   * `else`

2. Boolean Expressions

   * Comparisons
   * `True` and `False`
   * Compound conditions

3. Truthy and Falsy Values

   * `False`
   * `None`
   * `0`
   * Empty strings
   * Empty lists
   * Empty tuples
   * Empty dictionaries
   * Empty sets

4. Logical Operators

   * `and`
   * `or`
   * `not`

5. Nested Conditions

6. Conditional Input Validation

7. Python Indentation and PEP 8

## Git

1. Branching Concepts
2. Main Branch
3. Feature Branches
4. `git branch`
5. `git switch`
6. `git switch -c`
7. `git checkout` as the older alternative
8. Branch isolation
9. Switching between branches

---

# Theory & Classroom Explanation

## 1. Conditional Logic

Programs often need to make decisions based on changing information.

For example:

```text
If score is high
    → Excellent

Otherwise if score is sufficient
    → Pass

Otherwise
    → Fail
```

Python provides three primary conditional keywords:

```text
if
elif
else
```

The general structure is:

```text
if condition:
    action
elif another_condition:
    action
else:
    fallback_action
```

Only the appropriate branch is executed based on the conditions being evaluated.

---

# 2. `if` Statement

An `if` statement executes its block when its condition evaluates to `True`.

Conceptually:

```text
Condition
   │
   ├── True  → Execute block
   │
   └── False → Skip block
```

The condition can contain comparisons, variables, function results, or more complex expressions.

---

# 3. `elif` Statement

`elif` means **"else if"**.

It allows a program to test additional conditions after an initial `if` condition evaluates to false.

A conditional chain can contain multiple `elif` branches.

Example decision structure:

```text
Score
 │
 ├── 90+ → A
 ├── 80+ → B
 ├── 70+ → C
 ├── 60+ → D
 └── Below 60 → F
```

Python evaluates the conditions from top to bottom and executes the first matching branch.

---

# 4. `else` Statement

The `else` block provides a fallback when none of the preceding conditions are true.

Conceptually:

```text
if condition:
    option A
else:
    option B
```

An `else` block does not have its own condition.

---

# 5. Boolean Expressions

Conditional statements depend on expressions that evaluate to Boolean values.

Examples of comparisons include:

```text
age >= 18
score == 100
username == "admin"
password != ""
```

The result is either:

```text
True
```

or:

```text
False
```

These Boolean results determine which branch of the program executes.

---

# 6. Truthy and Falsy Values

Python allows many values to be evaluated directly in a Boolean context.

Common falsy values include:

```text
False
None
0
0.0
""
[]
()
{}
set()
```

Most other values are truthy.

For example:

```text
"Python"
[1, 2, 3]
42
```

are truthy.

### Important Concept

Truthy and falsy behavior allows concise checks for things such as empty input.

For example, an empty string can be treated as false in a condition.

---

# 7. Logical Operators

Logical operators allow multiple conditions to be combined.

## `and`

All required conditions must be true.

```text
Condition A AND Condition B
```

Example use cases:

* User is logged in **and** has permission.
* Age is valid **and** score is valid.

---

## `or`

At least one condition must be true.

```text
Condition A OR Condition B
```

Example use cases:

* User is an administrator **or** moderator.
* Input matches option A **or** option B.

---

## `not`

Reverses a Boolean result.

```text
not True  → False
not False → True
```

It is useful when checking that something is **not** true.

---

# 8. Nested Conditional Statements

A conditional can contain another conditional.

Conceptually:

```text
if user_exists:
    if password_correct:
        allow_login
    else:
        reject_password
else:
    reject_user
```

Nested conditions are useful when one decision depends on another.

However, excessive nesting can make code difficult to read. As programs become more complex, clearer logical expressions or separate functions can often improve maintainability.

---

# 9. Input Validation

Conditional statements can be used to validate user input.

For example, a program may need to verify that:

* A score is within an acceptable range.
* A username is not empty.
* A selected option is valid.
* A numeric value meets a required condition.

A typical validation flow is:

```text
Receive Input
     ↓
Check Input
     ↓
 ┌───┴────┐
Valid    Invalid
 ↓          ↓
Process    Error
```

Day 4 introduced basic validation concepts that will become more robust when exception handling is introduced later.

---

# 10. Python Indentation

Python uses indentation to define blocks of code.

The standard convention is:

```text
4 spaces per indentation level
```

Indentation determines which statements belong to a conditional block.

Incorrect indentation can result in errors or unintended program behavior.

Consistent indentation is therefore both a Python requirement and an important readability practice.

---

# Python Practice

All practical Python exercises for Day 4 were completed in:

```text
day4.ipynb
```

The notebook covers:

* Basic `if` statements
* `if` / `else`
* `if` / `elif` / `else`
* Boolean expressions
* Truthy and falsy values
* Logical operators
* Nested conditions
* Score and grade evaluation
* Basic input validation
* Login decision logic
* Conditional practice problems

The notebook contains the executable examples and experiments, while this document records the concepts and outcomes.

---

# Git Branching

## 1. What is a Git Branch?

A Git branch is a movable pointer to a line of development in a repository.

Branches allow developers to work on features, fixes, or experiments independently from the stable branch.

Instead of making every change directly on `main`, a developer can create a feature branch.

```text
main
  │
  C1 ─── C2 ─── C3
             \
              F1 ─── F2
                    feature/conditionals
```

This keeps feature development isolated until it is ready to be integrated.

---

# 2. Why Use Branches?

Branches are useful for:

* Developing new features.
* Testing experimental ideas.
* Fixing bugs independently.
* Protecting stable code.
* Working with multiple developers.
* Preparing changes for review.

The main idea is:

```text
Stable Code
    │
    ├── Feature A
    ├── Feature B
    └── Bug Fix
```

Each line of work can be developed separately.

---

# 3. Main Branch

The primary branch is commonly named:

```text
main
```

Older repositories may use:

```text
master
```

The exact name depends on the repository configuration.

For this project, `main` is treated as the stable development branch.

---

# 4. List Branches

To see the available local branches:

```bash
git branch
```

The currently active branch is marked with:

```text
*
```

For example:

```text
* main
```

means the repository is currently on `main`.

---

# 5. Create a Branch

Create a feature branch without switching to it:

```bash
git branch feature/conditionals
```

The branch now exists, but the current branch remains unchanged.

---

# 6. Switch Branches

Use:

```bash
git switch feature/conditionals
```

The working directory now reflects the selected branch.

Verify:

```bash
git branch
```

The output should identify:

```text
* feature/conditionals
```

---

# 7. Create and Switch in One Command

The more convenient approach is:

```bash
git switch -c feature/conditionals
```

This performs two operations:

```text
Create Branch
     +
Switch to Branch
```

It is the preferred modern workflow for creating a new local branch.

---

# 8. Older Git Alternative

Older Git workflows commonly use:

```bash
git checkout -b feature/conditionals
```

This still works in many Git installations, but `git switch` provides a clearer command specifically for branch switching.

---

# Git Practice Workflow

The Day 4 branching workflow was:

```text
Check Current Branch
        ↓
   git branch
        ↓
Create Feature Branch
        ↓
git switch -c feature/conditionals
        ↓
Work on Feature
        ↓
git status
        ↓
git add
        ↓
git commit
```

---

# Feature Branch Practice

The Day 4 conditional work was developed on:

```text
feature/conditionals
```

The branch was used to isolate conditional-logic work from the stable `main` branch.

After completing the changes, the feature branch could be checked with:

```bash
git status
```

and committed using an appropriate commit message.

Example:

```bash
git commit -m "feat: add conditional logic practice"
```

---

# Switching Between Branches

To return to the stable branch:

```bash
git switch main
```

To return to the feature branch:

```bash
git switch feature/conditionals
```

This demonstrates branch isolation.

### Important

A file created and committed on a feature branch does not automatically appear in `main`.

It becomes part of `main` only after the feature branch is merged or its commits are otherwise incorporated into `main`.

---

# Mini Task — Login Decision System

The Day 4 mini task focused on building a basic conditional login system.

The program requirements were:

1. Define a demonstration username and password.
2. Accept username input.
3. Accept password input.
4. Check the supplied credentials.
5. Use `if`, `elif`, `else`, and logical operators.
6. Provide different messages for:

   * Incorrect username.
   * Incorrect password.
   * Successful authentication.

The implementation was completed in the Day 4 notebook.

> **Learning note:** Hardcoded credentials are suitable only for a classroom demonstration. Real applications should never store passwords directly in source code.

---

# Git Branching Exercise

After completing the conditional exercises:

```bash
git status
```

Check the current branch:

```bash
git branch
```

Create or switch to:

```bash
git switch -c feature/conditionals
```

Stage the completed work:

```bash
git add .
```

Commit the changes:

```bash
git commit -m "feat: add conditional logic practice"
```

Return to `main`:

```bash
git switch main
```

Then return to the feature branch:

```bash
git switch feature/conditionals
```

This demonstrates how Git maintains separate development states.

---

# Day 4 Deliverables

```text
class/
└── day4/
    └── day4.ipynb
```

### Python

* [x] `if`
* [x] `elif`
* [x] `else`
* [x] Boolean expressions
* [x] Truthy and falsy values
* [x] `and`
* [x] `or`
* [x] `not`
* [x] Nested conditions
* [x] Basic input validation
* [x] Conditional decision making
* [x] Python indentation

### Git

* [x] Understand branches
* [x] Understand `main`
* [x] Create feature branches
* [x] `git branch`
* [x] `git switch`
* [x] `git switch -c`
* [x] Switch between `main` and feature branches
* [x] Commit changes on a feature branch
* [x] Understand branch isolation

---

# Expected Outcome

After completing Day 4, the learner can build programs that make decisions based on user input and Boolean conditions.

The learner also understands how Git branches provide isolated development environments.

The overall workflow is:

```text
                 PYTHON
                    │
             User Input
                    ↓
          Boolean Evaluation
                    ↓
          if / elif / else
                    ↓
          Decision / Output
                    │
                    ▼
                   GIT
                    │
                  main
                    │
                    ▼
          feature/conditionals
                    │
                    ↓
              Develop Feature
                    ↓
                  Commit
                    │
                    ▼
             Stable main
```

Day 4 establishes the foundation for both **program control flow** and **branch-based development**, which are essential skills for building and managing larger software projects.
