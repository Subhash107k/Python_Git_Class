# Day 5 — Loops, Iteration Control & GitHub Remote Workflow

## Overview

Day 5 introduced **iteration and repetitive program execution in Python** and connected the local Git workflow to **GitHub**.

The Python section covered `for` loops, `while` loops, `range()`, and loop-control statements such as `break`, `continue`, and `pass`.

The Git section moved beyond local version control and introduced remote repositories. The local project was connected to GitHub, allowing committed work to be pushed online and maintained as a remote backup.

Day 5 also marked the completion of the interactive CLI tool exercise.

All Python hands-on exercises were completed in the Day 5 Jupyter Notebook.

---

# Learning Objectives

By the end of Day 5, the learner can:

- Explain why loops are used in programming.
- Use `for` loops to iterate over sequences.
- Use `while` loops for condition-based repetition.
- Generate number sequences using `range()`.
- Use `break` to terminate a loop.
- Use `continue` to skip the current iteration.
- Understand the purpose of `pass`.
- Build programs that repeat operations until the user chooses to exit.
- Understand the difference between a local and remote Git repository.
- Explain the role of GitHub in a Git-based workflow.
- Create a GitHub remote repository.
- Connect a local Git repository to GitHub.
- Verify configured Git remotes.
- Push local commits to GitHub.
- Complete and commit the CLI tool exercise.

---

# Topics Covered

## Python

1. Iteration and Loops
   - `for`
   - `while`

2. The `range()` Function
   - `range(stop)`
   - `range(start, stop)`
   - `range(start, stop, step)`

3. Looping Through Sequences
   - Numbers
   - Strings
   - Other iterable objects

4. Loop Control
   - `break`
   - `continue`
   - `pass`

5. Condition-Based Repetition

6. Building Interactive CLI Programs

## Git & GitHub

1. Local vs Remote Repositories
2. GitHub Repository Concepts
3. Remote Repository URLs
4. `git remote`
5. `git remote add`
6. `git remote -v`
7. `git branch -M`
8. `git push`
9. Upstream Branches
10. HTTPS / SSH Authentication
11. First Local-to-GitHub Push

---

# Python: Loops and Iteration

## 1. What is a Loop?

A loop allows a program to execute a block of code repeatedly.

Without loops, repetitive tasks would require writing the same instructions many times.

For example:

```text
Without Loop
────────────
Print 1
Print 2
Print 3
Print 4
Print 5
```

With a loop:

```text
Start
  ↓
Repeat operation
  ↓
Check condition
  ↓
Continue / Stop
```

Loops are fundamental to automation, data processing, searching, validation, and interactive applications.

---

# 2. `for` Loop

A `for` loop is commonly used when iterating through a known sequence or iterable.

Conceptually:

```text
Sequence
   ↓
Item 1 → Process
   ↓
Item 2 → Process
   ↓
Item 3 → Process
   ↓
...
   ↓
End
```

A `for` loop can iterate over:

- Numbers
- Strings
- Lists
- Tuples
- Dictionaries
- Sets
- Other iterable objects

---

# 3. The `range()` Function

`range()` generates a sequence of numbers that can be used with loops.

The three common forms are:

```text
range(stop)
range(start, stop)
range(start, stop, step)
```

### Important Rule

The `stop` value is **not included**.

For example:

```text
range(1, 5)
```

produces:

```text
1 2 3 4
```

The `step` value determines how the sequence changes between values.

This makes `range()` useful for:

- Counting
- Repeating operations a specific number of times
- Generating numeric sequences
- Iterating over indexes

---

# 4. `while` Loop

A `while` loop continues executing while its condition remains `True`.

Conceptually:

```text
       Condition
          ↓
       ┌───────┐
       │ True? │
       └───┬───┘
          Yes
           ↓
     Execute Code
           ↓
     Update Condition
           │
           └──────→ Check Again

          No
           ↓
         Stop
```

A `while` loop is useful when the number of iterations is not necessarily known beforehand.

Common examples include:

- Menu-driven programs
- Repeated user input
- Retry systems
- Countdown programs
- Programs that run until a user chooses to exit

---

# 5. `break`

The `break` statement immediately terminates the current loop.

Conceptually:

```text
Loop
 ↓
Iteration
 ↓
Condition met?
 ├── No → Continue
 └── Yes → break → Exit Loop
```

It is useful when a program has found what it needs or when the user chooses to stop an operation.

---

# 6. `continue`

The `continue` statement skips the remaining code in the current iteration and moves to the next iteration.

Conceptually:

```text
Start Iteration
      ↓
Check Condition
      ↓
continue?
 ├── Yes → Next Iteration
 └── No  → Continue Current Iteration
```

It is useful when certain values or situations should be ignored without terminating the entire loop.

---

# 7. `pass`

`pass` performs no action.

It is commonly used as a placeholder when Python syntax requires a statement but the implementation has not yet been written.

Example concept:

```text
Function / Condition / Class
          ↓
      pass for now
```

Unlike `break` and `continue`, `pass` does **not** control loop execution.

---

# 8. Comparing Loop Controls

| Statement  | Purpose                             |
| ---------- | ----------------------------------- |
| `break`    | Completely exits the loop           |
| `continue` | Skips the current iteration         |
| `pass`     | Does nothing; acts as a placeholder |

Understanding this difference is important when controlling program flow.

---

# Python Practice

All Day 5 Python exercises were completed in:

```text
day5.ipynb
```

The notebook covers:

- `for` loops
- `while` loops
- `range()`
- Counting sequences
- Conditional loops
- `break`
- `continue`
- `pass`
- Nested loop logic
- User-controlled loops
- Menu-driven CLI logic

The notebook contains the executable code and experiments, while this documentation records the concepts and learning outcomes.

---

# Interactive CLI Application Practice

## Practice Overview

Day 5 completed the first practical exercise of the Python + Git learning journey.

### Exercise Focus

**Interactive CLI Calculator & User Profile Tool**

The exercise combines concepts learned during the first five days:

```text
Python Basics
     ↓
Variables & Data Types
     ↓
Operators & Strings
     ↓
Conditional Logic
     ↓
Loops
     ↓
Interactive CLI Application
```

---

# Exercise Features

The CLI application demonstrates:

- User name input.
- Interactive terminal menu.
- Repeated menu execution using a loop.
- Numeric calculation functionality.
- String manipulation.
- String reversal.
- User-selected operations.
- Invalid-option handling.
- Exit functionality.
- Basic conditional decision making.

The application remains active until the user selects the exit option.

---

# Architecture

The application follows a simple CLI flow:

```text
Start Program
     ↓
Ask for User Name
     ↓
Display Menu
     ↓
Receive Choice
     ↓
┌────┴──────────────┐
│                   │
Option 1          Option 2
│                   │
Number            String
Calculation       Processing
│                   │
└─────────┬─────────┘
          ↓
     Display Result
          ↓
     Return to Menu
          ↓
       Exit?
      ┌───┴───┐
     No      Yes
      │        │
      └──→   End
```

---

# Exercise Practice

The complete interactive CLI implementation was developed and tested in the Day 5 notebook.

The practice applies previously learned concepts rather than introducing advanced Python features.

### Concepts Used

- Variables
- `input()`
- Type conversion
- Operators
- Strings
- String slicing
- `if` / `elif` / `else`
- `for` / `while`
- `break`
- Basic validation
- Formatted output

---

# Git: Local vs Remote Repository

Before Day 5, Git was primarily being used locally.

```text
Local Computer
┌──────────────────────┐
│ Working Directory    │
│ Staging Area         │
│ Local Repository     │
└──────────────────────┘
```

GitHub introduces a remote copy:

```text
Local Repository
       │
       │ git push
       ↓
GitHub Remote
Repository
```

The local repository remains the primary Git history on the computer, while GitHub provides online hosting and collaboration capabilities.

---

# What is GitHub?

GitHub is an online platform for hosting Git repositories.

It provides capabilities such as:

- Remote repository hosting.
- Collaboration.
- Code sharing.
- Pull requests.
- Issue tracking.
- Project management.
- Repository backup.
- Continuous integration and deployment integrations.

Git and GitHub are related but are **not the same thing**.

### Git

A distributed version control system installed locally.

### GitHub

An online platform that can host Git repositories remotely.

---

# Local Repository vs GitHub Repository

| Local Git                | GitHub                                          |
| ------------------------ | ----------------------------------------------- |
| Stored on your computer  | Stored online                                   |
| Works without internet   | Requires network access for remote operations   |
| Maintains commit history | Hosts a remote copy of the repository           |
| Uses Git commands        | Provides Git hosting and collaboration features |
| Local development        | Sharing, backup, and collaboration              |

---

# Connecting a Local Repository to GitHub

After creating a repository on GitHub, the local repository can be connected to it using a remote.

The standard remote name is:

```text
origin
```

Add the remote:

```bash
git remote add origin <repository-url>
```

---

# Verify the Remote

Use:

```bash
git remote -v
```

This displays the configured fetch and push URLs.

Example structure:

```text
origin  <repository-url> (fetch)
origin  <repository-url> (push)
```

This confirms that the local repository knows where the remote repository is located.

---

# Rename the Default Branch

To ensure the primary branch is named `main`:

```bash
git branch -M main
```

This renames the current branch to `main`.

---

# Push Local Commits to GitHub

The first push can be performed with:

```bash
git push -u origin main
```

The `-u` option establishes an upstream relationship between the local `main` branch and the remote `origin/main` branch.

After this relationship is established, future pushes can usually be performed more simply with:

```bash
git push
```

---

# Authentication

GitHub requires authentication for operations involving private repositories and many write operations.

Two common approaches are:

### HTTPS

Uses a GitHub HTTPS repository URL.

Authentication may involve Git Credential Manager or another supported credential mechanism.

### SSH

Uses an SSH key pair configured with GitHub.

SSH is commonly preferred by developers who frequently interact with GitHub from the command line.

The exact authentication setup depends on the development environment.

---

# Day 5 Git Workflow

The complete workflow introduced on Day 5 was:

```text
Create / Modify Files
        ↓
git status
        ↓
git add
        ↓
git commit
        ↓
Connect Remote
        ↓
git remote add origin
        ↓
Verify Remote
        ↓
git remote -v
        ↓
Push to GitHub
        ↓
git push -u origin main
```

This represents the transition from **local Git development to remote Git collaboration**.

---

# Git Workflow for the CLI Exercise

Before pushing the exercise work, the feature was integrated into the main development branch.

Typical workflow:

```bash
git switch main
git merge feature/conditionals
```

Then verify the work:

```bash
git status
```

Stage the completed work:

```bash
git add .
```

Commit the milestone:

```bash
git commit -m "feat: complete CLI tool exercise"
```

Finally, push the repository:

```bash
git push
```

---

# Important Git Concept: Merge

Day 5 also reinforces the purpose of merging.

A merge combines changes from one branch into another.

For example:

```text
main
 │
 C1 ─── C2 ───────── C4
          \         /
           C3 ─────
          feature
```

The feature branch contains development work that can later be integrated into `main`.

---

# Day 5 Milestone

## CLI Exercise Completed

**Interactive CLI Calculator & User Profile Tool**

### Status

- [x] Project requirements defined
- [x] User interaction implemented
- [x] Menu-driven workflow implemented
- [x] Loop-based interaction implemented
- [x] Conditional decision making implemented
- [x] Calculator functionality implemented
- [x] String-processing functionality implemented
- [x] Exit functionality implemented
- [x] Project tested
- [x] Project committed with Git
- [x] Local repository connected to GitHub
- [x] Project pushed to GitHub

---

# Day 5 Deliverables

```text
class/
└── day5/
    └── day5.ipynb

projects/
└── project1/
    └── CLI calculator & profile tool
```

### Python

- [x] `for` loops
- [x] `while` loops
- [x] `range()`
- [x] `break`
- [x] `continue`
- [x] `pass`
- [x] Interactive loops
- [x] Menu-driven program logic

### Git & GitHub

- [x] Understand local repositories
- [x] Understand remote repositories
- [x] Create GitHub repository
- [x] Configure remote
- [x] `git remote add`
- [x] `git remote -v`
- [x] `git branch -M main`
- [x] `git push`
- [x] Upstream branch concept
- [x] HTTPS / SSH authentication concepts
- [x] Push local project to GitHub

### Project Practice

- [x] CLI tool exercise completed
- [x] Exercise tested
- [x] Exercise committed to Git
- [x] Exercise published to GitHub

---

# Expected Outcome

By the end of Day 5, the learner can build an interactive Python program using loops and conditional logic and manage that project using a complete local-to-remote Git workflow.

The development workflow has now expanded from:

```text
Python Code
    ↓
Git Repository
```

to:

```text
Python Code
    ↓
Git
    ↓
Commit
    ↓
GitHub
    ↓
Remote Repository
```

Day 5 therefore represents the first major milestone of the learning journey: **building a practical Python CLI application and publishing its Git history to GitHub.**
