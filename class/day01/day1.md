# Day 1 — Python & Git Foundations

## Overview

Day 1 establishes the foundation for the Python and Git work completed throughout this learning project. The focus is on understanding Python fundamentals, preparing the development environment, writing and executing basic Python programs, and learning the essential Git workflow for tracking project changes.

---

## Learning Objectives

By the end of Day 1, the learner can:

* Explain what Python is and why it is widely used.
* Understand the basic characteristics of Python, including readability, dynamic typing, and interpreted execution.
* Set up Python 3.x and verify the installation from the terminal.
* Configure Visual Studio Code (VS Code) for Python development.
* Create, execute, and troubleshoot basic Python scripts.
* Use `print()` for console output.
* Understand Python comments, strings, and indentation.
* Explain the purpose of Version Control Systems (VCS).
* Understand the difference between Git and GitHub.
* Configure Git user identity.
* Initialize a local Git repository using `git init`.
* Check repository status using `git status`.

---

# Topics Covered

## 1. Introduction to Python

### What is Python?

Python is a high-level, general-purpose programming language designed with an emphasis on readability and developer productivity.

Python is commonly used for:

* Web development
* Data analysis
* Machine learning and artificial intelligence
* Automation and scripting
* Desktop applications
* APIs and backend development
* Scientific computing
* DevOps and system administration

### Key Characteristics of Python

* **High-level** — abstracts many low-level system details.
* **Readable** — uses a clean and relatively simple syntax.
* **Dynamically typed** — variable types are determined at runtime.
* **Interpreted** — Python programs are executed through the Python runtime.
* **Multi-paradigm** — supports procedural, object-oriented, and functional programming.
* **Cross-platform** — runs on Windows, Linux, and macOS.
* **Extensive ecosystem** — provides a large standard library and third-party package ecosystem.

---

# 2. Python Execution Model

Python is commonly described as an interpreted language, but its execution process involves multiple stages.

When a Python program is executed:

```text
Python Source Code
        ↓
Python Compiler
        ↓
Bytecode
        ↓
Python Virtual Machine (PVM)
        ↓
Program Output
```

For example:

```bash
python day1_syntax.py
```

The Python interpreter reads the source program and handles its execution. Python implementations such as CPython may compile source code into bytecode before execution by the Python Virtual Machine.

### Python vs. Traditional Compiled Languages

| Python                                         | C/C++                                              |
| ---------------------------------------------- | -------------------------------------------------- |
| Usually executed through a runtime/interpreter | Usually compiled to native machine code            |
| Dynamically typed                              | Generally statically typed                         |
| Emphasizes rapid development                   | Often emphasizes performance and low-level control |
| Highly portable source code                    | Usually requires platform-specific compilation     |
| Automatic memory management                    | More direct memory-management control              |

> **Important:** Saying that Python simply executes code "line by line" is an oversimplification. Python source is processed into bytecode and then executed by the Python runtime.

---

# 3. Development Environment Setup

The development environment used for this project consists of:

* Python 3.x
* Visual Studio Code
* VS Code Python extension
* Terminal / PowerShell / Command Prompt
* Git

### Verify Python Installation

Run:

```bash
python --version
```

or:

```bash
python3 --version
```

Example:

```text
Python 3.x.x
```

### Verify Python Execution

Run:

```bash
python
```

Then test:

```python
print("Python is working!")
```

Exit the interpreter with:

```python
exit()
```

---

# 4. Python Basic Syntax

## `print()`

The `print()` function displays information in the console.

```python
print("Hello, Python!")
print("Learning Python and Git")
```

## Comments

Single-line comments begin with `#`.

```python
# This is a Python comment
print("Hello")
```

Comments are ignored during program execution and are primarily used to explain code.

## Multi-Line Documentation

Triple-quoted strings can be used for documentation strings (docstrings):

```python
"""
This module demonstrates
basic Python syntax.
"""
```

A true docstring is normally placed at the beginning of a module, function, or class.

## Indentation

Python uses indentation to define code blocks.

The commonly recommended style is **4 spaces per indentation level**.

Example:

```python
if True:
    print("This code belongs to the if block.")
```

Incorrect indentation can result in an `IndentationError`.

---

# Practical Coding Exercises

## Exercise 1.1 — Hello World & Syntax Basics

Create:

```text
day1_syntax.py
```

Add:

```python
# Day 1: Python Basic Output and Comments

print("==========================================")
print("Welcome to Python + Git Zero-to-Hero!")
print("==========================================")

"""
This is a multi-line documentation example.
It can span multiple lines and can be used
to document modules, functions, and classes.
"""

print("Executing line 1...")
print("Executing line 2...")
print("Python installation and environment setup successful!")
```

Run:

```bash
python day1_syntax.py
```

### Expected Output

```text
==========================================
Welcome to Python + Git Zero-to-Hero!
==========================================
Executing line 1...
Executing line 2...
Python installation and environment setup successful!
```

---

# Exercise 1.2 — Running Python Scripts from the Terminal

Navigate to the directory containing the Python file:

```bash
cd path/to/project
```

Run the program:

```bash
python day1_syntax.py
```

This establishes the basic development workflow:

```text
Write Code
   ↓
Save File
   ↓
Open Terminal
   ↓
Run Python Script
   ↓
Check Output
   ↓
Fix Errors
   ↓
Run Again
```

---

# Code Practice & Debugging

## Practice 1 — Multi-Line Developer Banner

Create:

```text
practice_day1_banner.py
```

The program should display:

* Developer name
* Development environment
* Operating system

Example:

```python
print("************************************")
print("Developer: Your Name")
print("IDE: VS Code")
print("OS: Windows")
print("************************************")
```

### Challenge

Modify the program so that all information appears on a single formatted line:

```text
Developer: Your Name | IDE: VS Code | OS: Windows
```

---

# Practice 2 — Syntax Debugging Drill

Identify and correct the syntax errors:

```python
# Broken code

print("Starting Python Program"
print 'Learning Python Syntax'
print("Line 3 complete)
```

### Correct Version

```python
print("Starting Python Program")
print("Learning Python Syntax")
print("Line 3 complete")
```

### Errors Identified

1. Missing closing `)` in the first `print()`.
2. Python 3 requires `print()` as a function.
3. Missing closing quotation mark in the third statement.

### Key Lesson

Syntax errors prevent Python from correctly parsing the program. The interpreter normally reports the location of the problem and provides an error message that helps identify what needs to be corrected.

---

# Introduction to Version Control

## What is Version Control?

Version Control is a system for recording and managing changes made to files throughout the development process.

It allows developers to:

* Track changes.
* Review previous versions.
* Identify when changes were introduced.
* Restore earlier versions.
* Maintain a history of development.
* Collaborate safely with other developers.

---

# Git vs. GitHub

Although Git and GitHub are commonly used together, they are different technologies.

### Git

**Git** is a distributed version control system that runs locally on your computer.

It manages:

* Repository history
* Commits
* Branches
* Changes
* Merges

### GitHub

**GitHub** is a cloud-based platform that hosts Git repositories and provides additional collaboration features.

```text
Git
↓
Local Version Control
↓
Your Computer
```

```text
GitHub
↓
Remote Repository Hosting
↓
Cloud / Collaboration
```

A project can use Git without GitHub.

---

# Git Practice

## Step 1 — Verify Git Installation

Run:

```bash
git --version
```

Example:

```text
git version 2.x.x
```

---

## Step 2 — Configure Git Identity

Configure your Git username:

```bash
git config --global user.name "Your Name"
```

Configure your email:

```bash
git config --global user.email "your.email@example.com"
```

These settings identify the author of commits created on the machine.

### Verify Configuration

Run:

```bash
git config --global --list
```

You can also check individual values:

```bash
git config --global user.name
git config --global user.email
```

---

# Step 3 — Initialize a Git Repository

Navigate to the project directory:

```bash
cd path/to/project
```

Initialize Git:

```bash
git init
```

Git creates a hidden `.git` directory containing the repository's local metadata and history information.

Example output:

```text
Initialized empty Git repository in D:/My_Projects/Python-Git/.git/
```

---

# Step 4 — Check Repository Status

Run:

```bash
git status
```

Git will show information about:

* The current branch
* Untracked files
* Modified files
* Staged changes
* Working-tree status

For example:

```text
Untracked files:
    day1_syntax.py
    day1_intro.py
```

This confirms that Git can detect the files in the project directory.

---

# Mini Project — Day 1 Introduction

Create:

```text
day1_intro.py
```

The program should display:

1. Your full name.
2. Your current programming experience level.
3. Your primary goal for the Python & Git learning project.

Example:

```python
print("========================================")
print("Python & Git Learning Project")
print("========================================")

print("Name: Your Name")
print("Experience Level: Beginner")
print("Goal: Build strong Python and Git fundamentals")
```

Run:

```bash
python day1_intro.py
```

Then check:

```bash
git status
```

---

# Suggested Day 1 Project Structure

After completing the exercises, the project can contain:

```text
python-git-project/
│
├── class/
│   └── day1/
│       ├── day1_syntax.py
│       ├── day1_intro.py
│       └── practice_day1_banner.py
│
├── docs/
│   └── day1_notes.md
│
└── .git/
```

The `.git` directory is created automatically by Git and normally should not be edited manually.

---

# Day 1 Git Workflow

The basic workflow introduced on Day 1 is:

```text
Create / Modify Files
        ↓
git status
        ↓
git add
        ↓
git commit
        ↓
Repository History
```

For example:

```bash
git status
git add .
git commit -m "Complete Day 1 Python and Git foundations"
```

The first commit creates a permanent checkpoint in the repository history.

---

# Troubleshooting

## Python Command Not Found

If this does not work:

```bash
python --version
```

try:

```bash
py --version
```

On Windows, the Python Launcher may be available even when `python` is not mapped correctly.

If neither command works, verify that Python is installed and that the Python executable is correctly configured in the system PATH.

---

## Git Command Not Found

If:

```bash
git --version
```

fails, Git may not be installed or may not be available through the system PATH.

Verify the Git installation before continuing.

---

## SyntaxError

Example:

```text
SyntaxError: '(' was never closed
```

Check:

* Parentheses
* Quotation marks
* Colons
* Commas
* Python syntax

---

## IndentationError

Example:

```text
IndentationError: unexpected indent
```

Check that indentation is consistent and preferably use **4 spaces** for each indentation level.

---

# Day 1 Deliverables

By completing Day 1, the project should contain:

* [ ] Python installation verified.
* [ ] VS Code configured for Python.
* [ ] First Python script created.
* [ ] Basic `print()` syntax practiced.
* [ ] Comments and docstrings explored.
* [ ] Python indentation understood.
* [ ] Python script executed through the terminal.
* [ ] Basic syntax errors identified and corrected.
* [ ] Git installation verified.
* [ ] Git username and email configured.
* [ ] Local Git repository initialized.
* [ ] `git status` used to inspect project changes.
* [ ] Day 1 practice scripts completed.

---

# Expected Outcome

After completing Day 1, the learner has established the core development environment and understands the basic workflow used throughout the project.

The learner can:

```text
Write Python Code
       ↓
Run Python from Terminal
       ↓
Understand & Fix Basic Errors
       ↓
Organize Project Files
       ↓
Initialize Git
       ↓
Track Project Changes
```

Day 1 therefore provides the foundation for the subsequent Python programming, problem-solving, Git, and practical project work covered in the remaining days.
