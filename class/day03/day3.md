# Day 3 — Operators, Strings, String Methods & Git History

## Overview

Day 3 focused on Python operators, string manipulation, and Git history management.

The Python section covered how operators are used to perform calculations, compare values, combine conditions, and update variables. String fundamentals included indexing, slicing, immutability, and commonly used string methods.

The Git section introduced tools for reviewing changes and inspecting repository history using `git diff` and `git log`.

All hands-on Python exercises and practice activities were completed in the corresponding Jupyter Notebook.

---

## Learning Objectives

By the end of Day 3, the learner can:

* Use arithmetic, comparison, logical, and assignment operators.
* Understand operator precedence.
* Work with Python strings as immutable sequences.
* Access characters using positive and negative indexing.
* Extract text using string slicing.
* Reverse strings using slicing.
* Apply common string methods for text processing.
* Understand the difference between working-tree and staged changes in Git.
* Inspect code modifications using `git diff`.
* Review staged changes using `git diff --staged`.
* Inspect commit history using `git log`.
* View a compact commit history using `git log --oneline --graph --all`.

---

# Topics Covered

## 1. Python Operators

### Arithmetic Operators

Python provides operators for mathematical calculations:

| Operator | Purpose             |
| -------- | ------------------- |
| `+`      | Addition            |
| `-`      | Subtraction         |
| `*`      | Multiplication      |
| `/`      | Division            |
| `//`     | Floor division      |
| `%`      | Modulus / remainder |
| `**`     | Exponentiation      |

### Comparison Operators

Comparison operators return a Boolean value (`True` or `False`).

```text
==    Equal to
!=    Not equal to
>     Greater than
<     Less than
>=    Greater than or equal to
<=    Less than or equal to
```

### Logical Operators

Logical operators combine Boolean expressions.

```text
and    Both conditions must be true
or     At least one condition must be true
not    Reverses a Boolean result
```

### Assignment Operators

Python also provides augmented assignment operators:

```text
=      Assignment
+=     Add and assign
-=     Subtract and assign
*=     Multiply and assign
/=     Divide and assign
//=    Floor divide and assign
%=     Modulus and assign
**=    Exponentiate and assign
```

---

# 2. Operator Precedence

Python follows a defined order when evaluating expressions.

For example, multiplication is performed before addition unless parentheses change the order.

```text
10 + 5 * 2
```

is evaluated as:

```text
10 + (5 * 2)
```

Parentheses can be used when a specific evaluation order is required.

Understanding precedence helps prevent unexpected calculation results.

---

# 3. Strings in Python

A string is a sequence of characters.

Example:

```text
Python
```

Because strings are sequences, individual characters can be accessed using indexes.

Python uses **zero-based indexing**:

```text
 P   y   t   h   o   n
 0   1   2   3   4   5
```

The first character is therefore at index `0`.

---

# 4. Negative Indexing

Python also supports negative indexes for accessing characters from the end.

```text
 P   y   t   h   o   n
-6  -5  -4  -3  -2  -1
```

For example:

```text
text[-1]
```

returns the final character.

Negative indexing is useful when working with the end of strings or other sequences.

---

# 5. String Slicing

Slicing extracts part of a string.

The general syntax is:

```text
sequence[start:stop:step]
```

Important rules:

* `start` is inclusive.
* `stop` is exclusive.
* `step` controls the movement between indexes.

Common patterns include:

```text
text[:5]       First five characters
text[2:]       From index 2 to the end
text[1:5]      Characters from index 1 through 4
text[::2]      Every second character
text[::-1]     Reverse the string
```

---

# 6. String Immutability

Python strings are **immutable**.

This means that an existing string cannot be modified character-by-character.

An operation such as changing one character directly results in a `TypeError`.

Instead, string methods create a new string value.

For example, operations such as:

```text
upper()
lower()
replace()
strip()
```

do not modify the original string object. They return a new string.

This concept is important for understanding how Python handles string data.

---

# 7. Common String Methods

The following methods were practiced:

| Method          | Purpose                             |
| --------------- | ----------------------------------- |
| `.upper()`      | Converts text to uppercase          |
| `.lower()`      | Converts text to lowercase          |
| `.title()`      | Converts text to title case         |
| `.strip()`      | Removes leading/trailing whitespace |
| `.replace()`    | Replaces part of a string           |
| `.split()`      | Splits a string into a list         |
| `.join()`       | Combines strings into one string    |
| `.find()`       | Finds the position of text          |
| `.count()`      | Counts occurrences                  |
| `.startswith()` | Checks the beginning of a string    |
| `.endswith()`   | Checks the end of a string          |

These methods form the foundation of basic text processing in Python.

---

# 8. String Analysis Concepts

During practice, strings were used to perform tasks such as:

* Cleaning user input.
* Counting characters.
* Counting words.
* Converting text to uppercase or lowercase.
* Searching for specific words.
* Replacing text.
* Splitting sentences into individual words.
* Joining words into a formatted string.
* Reversing text.
* Checking prefixes and suffixes.

---

# Python Practice

All practical Python exercises for Day 3 were completed in the Jupyter Notebook:

```text
day3.ipynb
```

The notebook covers:

* Arithmetic operators
* Comparison operators
* Logical operators
* Assignment operators
* Operator precedence
* String indexing
* Negative indexing
* Slicing
* String reversal
* String immutability
* String methods
* String analysis
* User-input text processing

The notebook serves as the hands-on implementation and experimentation area, while this document records the concepts and learning outcomes.

---

# Git: Reviewing Project Changes

Day 3 introduced Git commands for inspecting changes and reviewing project history.

## 1. Check Repository Status

```bash
git status
```

This displays the current state of the working directory and staging area.

It can show:

* Untracked files
* Modified files
* Staged changes
* Current branch information

---

## 2. Review Unstaged Changes

```bash
git diff
```

`git diff` displays changes in tracked files that have been modified but are not currently staged.

The output uses:

```text
- removed line
+ added line
```

This makes it possible to review changes before adding them to the staging area.

---

## 3. Stage Changes

Use:

```bash
git add <file>
```

or stage all relevant changes:

```bash
git add .
```

After staging, verify the repository:

```bash
git status
```

---

## 4. Review Staged Changes

Once changes have been staged:

```bash
git diff --staged
```

This shows the changes that are currently prepared for the next commit.

### Difference

```text
git diff
```

Reviews:

```text
Working Directory → Staging Area
```

while:

```text
git diff --staged
```

reviews:

```text
Staging Area → Last Commit
```

---

# 5. Commit Changes

Create a meaningful commit:

```bash
git commit -m "feat: add operators and string manipulation practice"
```

A good commit message should briefly describe what was added or changed.

---

# Git History

## 6. View Full Commit History

```bash
git log
```

This displays detailed information about previous commits, including:

* Commit hash
* Author
* Date
* Commit message

---

## 7. Compact Commit History

```bash
git log --oneline
```

This provides a shorter view of the project's commit history.

Example:

```text
8f42a31 feat: add operators and string practice
2c91b20 feat: add variables and type conversion
a7315de feat: add Python and Git foundations
```

---

## 8. Visual Commit History

```bash
git log --oneline --graph --all
```

This provides a compact graphical representation of commits and becomes particularly useful when working with multiple branches.

---

# Git Workflow Practiced

The Day 3 Git workflow was:

```text
Modify Files
     ↓
git status
     ↓
git diff
     ↓
git add
     ↓
git diff --staged
     ↓
git commit
     ↓
git log
```

This workflow encourages reviewing changes before permanently recording them in project history.

---

# Mini Task

A **String Analyzer** was used as the main Day 3 practice task.

The program accepts a sentence and performs basic analysis such as:

* Removing unnecessary whitespace.
* Counting characters.
* Counting words.
* Converting text to uppercase.
* Reversing the sentence.
* Checking whether `"Python"` appears in the input.

The complete implementation and experimentation were performed in the Day 3 Jupyter Notebook.

---

# Day 3 Deliverables

```text
class/
└── day3/
    └── day3.ipynb
```

### Python

* [x] Arithmetic operators
* [x] Comparison operators
* [x] Logical operators
* [x] Assignment operators
* [x] Operator precedence
* [x] String indexing
* [x] Negative indexing
* [x] String slicing
* [x] String reversal
* [x] String immutability
* [x] String methods
* [x] Basic string analysis

### Git

* [x] `git status`
* [x] `git diff`
* [x] `git add`
* [x] `git diff --staged`
* [x] `git commit`
* [x] `git log`
* [x] `git log --oneline`
* [x] `git log --oneline --graph --all`

---

# Expected Outcome

After completing Day 3, the learner can:

```text
Work with Python Values
        ↓
Use Operators
        ↓
Manipulate Strings
        ↓
Analyze Text
        ↓
Review Code Changes
        ↓
Commit Changes
        ↓
Inspect Git History
```

Day 3 establishes two important development skills: **basic Python text processing** and **the ability to inspect and understand changes recorded in Git history**.
