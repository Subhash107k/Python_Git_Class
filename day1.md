# Day 1 — Python & Git Foundations: Setup, Environment & Syntax

## Learning Objectives
- Understand Python's role as a high-level, interpreted programming language.
- Set up the Python 3.x development environment and Visual Studio Code (VS Code).
- Write, execute, and troubleshoot your first Python scripts via the CLI terminal.
- Understand the fundamentals of Version Control Systems (VCS).
- Initialize a local Git repository and configure user identification.

---

## Topics Covered
1. **Introduction to Python**:
   - What is Python? Features: interpreted, dynamically typed, readable, multi-paradigm.
   - The Python Interpreter vs Compiled Languages.
   - Installing Python 3.x and configuring Environment Variables (PATH).
   - Setting up VS Code and installing the Python extension.
2. **Python Basic Syntax**:
   - The `print()` function for console output.
   - Single-line comments (`#`) and multi-line docstrings (`""" ... """`).
   - Code indentation standards (PEP 8: 4 spaces per indentation level).
3. **Introduction to Git & Version Control**:
   - What is Version Control? Why is local tracking essential?
   - Difference between **Git** (local CLI tool) and **GitHub** (remote cloud platform).
   - Git identity configuration: `git config`.
   - Initializing a Git repository: `git init`.

---

## Theory & Classroom Explanation

### 1. How Python Executes Code
Unlike compiled languages like C or C++ which compile code directly into machine binaries, Python is an **interpreted language**. When you run a `.py` script:
1. Python compiles source code into intermediate bytecode (`.pyc`).
2. The Python Virtual Machine (PVM) interprets and executes the bytecode line by line.

### 2. What is Version Control?
Version Control Systems (VCS) record changes made to files over time. This allows developers to:
- Revert files back to a previous state.
- Compare changes over time.
- See who modified a file and when an error was introduced.
- Work safely without fear of accidentally deleting working code.

**Git** is a distributed version control system. Every developer's computer holds a complete copy of the repository's history.

---

## Practical Coding Exercises

### Exercise 1.1: Hello World & Syntax Basics
Create a file named `day1_syntax.py` and write the following code:

```python
# Day 1: Python Basic Output and Comments

# Single-line comment: Display welcoming messages
print("==========================================")
print("Welcome to Python + Git Zero-to-Hero!")
print("==========================================")

# Multi-line string / comment demonstration
"""
This is a multi-line docstring.
It can span multiple lines and is often used
to document modules, functions, and classes.
"""

print("Executing line 1...")
print("Executing line 2...")
print("Python installation and environment setup successful!")
```

### Exercise 1.2: Running Scripts via Terminal
Open your terminal (PowerShell / Command Prompt / Bash) in VS Code and run:
```bash
python day1_syntax.py
```

---

## Code Practice & Debugging Exercises

### Practice 1: Multi-Line Banner Output
Write a script `practice_day1_banner.py` that prints a formatted 3-line ASCII banner containing your name, preferred IDE, and operating system.

```python
# Sample Solution Framework
print("************************************")
print("Developer: Alex | IDE: VS Code | OS: Windows")
print("************************************")
```

### Practice 2: Syntax Debugging Drill
The following code block has 3 syntax errors. Find and fix them:

```python
# BROKEN CODE - FIX ME
# print("Starting Python Program"
# print 'Learning Python Syntax' 
# print("Line 3 complete)

# CORRECTED SOLUTION:
print("Starting Python Program")
print("Learning Python Syntax")
print("Line 3 complete")
```

---

## Git / GitHub Practice

### Step 1: Configure Git Identity
Set your global name and email (run once per machine):
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

Verify your configuration:
```bash
git config --list
```

### Step 2: Initialize Your Local Git Repository
Navigate to your project directory in terminal and run:
```bash
git init
```
*Output expected*: `Initialized empty Git repository in D:/My_Projects/.../.git/`

---

## Mini Task
Create a script named `day1_intro.py` that outputs:
1. Your full name.
2. Your current programming experience level.
3. Your primary goal for this 20-day course.

Run the script in terminal, verify it displays without syntax errors, and run `git status` to verify Git detects the new file.

---

## Expected Outcome
By the end of Day 1, you can launch VS Code, write clean Python scripts, execute them using the terminal, and initialize local Git version control for your workspace.
