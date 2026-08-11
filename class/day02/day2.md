# Day 2 — Variables, Data Types, Type Conversion & Git Staging

## Overview

Day 2 builds on the Python and Git foundations established on Day 1. The focus is on working with variables, understanding Python's built-in scalar data types, converting user input into appropriate types, and producing readable formatted output.

The Git portion introduces the complete basic local workflow: modifying files, checking their status, staging selected changes, and creating commits that record project snapshots.

---

# Learning Objectives

By the end of Day 2, the learner can:

* Create and assign values to Python variables.
* Explain Python's dynamic typing system.
* Inspect values and their types using `type()`.
* Follow common PEP 8 naming conventions.
* Use multiple assignment.
* Work with `int`, `float`, `str`, `bool`, and `complex` values.
* Understand that `input()` returns a string.
* Convert values using `int()`, `float()`, `str()`, and `bool()`.
* Use f-strings for readable output formatting.
* Perform basic calculations using user-provided data.
* Understand the Git working directory, staging area, and repository.
* Check changes with `git status`.
* Stage specific files using `git add`.
* Create meaningful commits using `git commit`.

---

# Topics Covered

## 1. Python Variables

* Variable assignment
* Names and references
* Dynamic typing
* `type()`
* Multiple assignment
* Reassignment
* PEP 8 naming conventions

## 2. Python Data Types

* `int`
* `float`
* `str`
* `bool`
* `complex`

## 3. Type Conversion and User Input

* `input()`
* `int()`
* `float()`
* `str()`
* `bool()`
* Numeric calculations
* f-string formatting

## 4. Git Staging and Commits

* Working Directory
* Staging Area / Index
* Local Repository
* `git status`
* `git add`
* `git commit`
* Reviewing staged changes

---

# Theory & Classroom Explanation

## 1. Variables in Python

A Python variable is best understood as a **name bound to an object**.

For example:

```python
x = 5
```

Here, `x` refers to an integer object whose value is `5`.

The same name can later refer to an object of a different type:

```python
x = 5
print(type(x))

x = "Hello"
print(type(x))
```

Output:

```text
<class 'int'>
<class 'str'>
```

This is possible because Python uses **dynamic typing**.

### Important Concept

Python variables do not have to be declared with a fixed type before assignment.

```python
age = 20
name = "Subhash"
height = 1.75
is_student = True
```

Python determines the type of each object at runtime.

---

# 2. Variable Naming

Python allows many valid variable names, but readable naming is important.

### Recommended Style

PEP 8 generally recommends **snake_case** for variable and function names.

```python
first_name = "Subhash"
student_age = 21
total_price = 1500.50
```

### Avoid

```python
firstName = "Subhash"
StudentAge = 21
```

`camelCase` is valid Python syntax, but `snake_case` is the conventional style for variables and functions.

### Invalid Names

```python
2name = "Python"       # Invalid
student-name = "A"    # Invalid
class = "Python"      # Invalid keyword
```

A variable name should:

* Start with a letter or `_`.
* Contain letters, numbers, and underscores.
* Not be a Python keyword.
* Clearly describe the value it represents.

---

# 3. Multiple Assignment

Python supports assigning multiple values in a single statement:

```python
a, b, c = 10, 20, 30
```

This is equivalent to:

```python
a = 10
b = 20
c = 30
```

You can also assign the same value to multiple variables:

```python
x = y = z = 0
```

---

# 4. Fundamental Python Data Types

Python provides several built-in data types.

| Type      | Example    | Description                    |
| --------- | ---------- | ------------------------------ |
| `int`     | `25`       | Integer numbers                |
| `float`   | `25.5`     | Decimal/floating-point numbers |
| `str`     | `"Python"` | Text                           |
| `bool`    | `True`     | Boolean truth value            |
| `complex` | `3 + 4j`   | Complex number                 |

---

## Integer — `int`

Integers represent whole numbers.

```python
age = 21
year = 2026
temperature = -5
```

---

## Floating-Point — `float`

Floating-point numbers represent decimal values.

```python
height = 1.75
price = 1250.50
temperature = 36.5
```

---

## String — `str`

Strings represent text.

```python
name = "Subhash"
message = "Learning Python"
```

Strings can use either single or double quotes:

```python
name = "Python"
language = 'Python'
```

---

## Boolean — `bool`

Boolean values represent one of two states:

```python
is_student = True
is_logged_in = False
```

The only Boolean values are:

```python
True
False
```

---

## Complex — `complex`

Python supports complex numbers using `j` for the imaginary component.

```python
number = 3 + 4j

print(number.real)
print(number.imag)
```

Output:

```text
3.0
4.0
```

---

# 5. Checking Data Types

The built-in `type()` function can be used to inspect the type of a value.

```python
age = 21
name = "Python"
height = 1.75
is_student = True

print(type(age))
print(type(name))
print(type(height))
print(type(is_student))
```

Output:

```text
<class 'int'>
<class 'str'>
<class 'float'>
<class 'bool'>
```

---

# 6. User Input

The `input()` function allows a program to receive input from the user.

```python
name = input("Enter your name: ")

print(f"Hello, {name}!")
```

### Important Rule

`input()` **always returns a string**.

For example:

```python
age = input("Enter your age: ")

print(type(age))
```

Even if the user enters:

```text
21
```

the value returned by `input()` is:

```text
"21"
```

It is a `str`, not an `int`.

---

# 7. Type Conversion

Type conversion changes a value from one type to another.

## String to Integer

```python
age = int("21")
```

## String to Float

```python
price = float("1250.50")
```

## Number to String

```python
age = 21
message = str(age)
```

## Boolean Conversion

```python
print(bool(1))
print(bool(0))
```

Output:

```text
True
False
```

> **Note:** `bool()` follows Python's truth-value rules. For example, `bool("False")` is `True` because the string is non-empty.

---

# 8. f-Strings

f-strings provide a convenient way to insert values into strings.

```python
name = "Subhash"
age = 21

print(f"My name is {name} and I am {age} years old.")
```

Output:

```text
My name is Subhash and I am 21 years old.
```

They can also contain expressions:

```python
price = 100
quantity = 3

print(f"Total: {price * quantity}")
```

---

# Practical Coding Exercises

## Exercise 2.1 — Data Types & Type Conversion

Create:

```text
day2_datatypes.py
```

Use:

```python
# Day 2: Variables, Data Types & Type Conversion

print("==========================================")
print("Python Variables and Data Types")
print("==========================================")

user_name = input("Enter your username: ")
age_input = input("Enter your age: ")
height_input = input("Enter your height in meters: ")

# input() returns strings, so convert numeric values.
age = int(age_input)
height = float(height_input)

is_student = True

# Complex number
complex_value = 3 + 4j

print("\n--- Data Type Summary ---")
print(f"Username: {user_name}")
print(f"Username type: {type(user_name).__name__}")

print(f"Age: {age}")
print(f"Age type: {type(age).__name__}")

print(f"Height: {height} m")
print(f"Height type: {type(height).__name__}")

print(f"Is Student: {is_student}")
print(f"Boolean type: {type(is_student).__name__}")

print(
    f"Complex number: {complex_value} | "
    f"Real: {complex_value.real} | "
    f"Imaginary: {complex_value.imag}"
)
```

### Key Learning

This exercise demonstrates:

```text
input()
  ↓
str
  ↓
int() / float()
  ↓
Correct numeric type
  ↓
Calculation / Output
```

---

# Exercise 2.2 — User Calculator

Create:

```text
user_calculator.py
```

Code:

```python
# Day 2: Basic User Calculator

print("================================")
print("      SIMPLE CALCULATOR")
print("================================")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

addition = num1 + num2
subtraction = num1 - num2
multiplication = num1 * num2

print("\n--- Results ---")
print(f"Addition:       {addition}")
print(f"Subtraction:    {subtraction}")
print(f"Multiplication: {multiplication}")
```

### Challenge

Extend the calculator to support division.

Consider what should happen when the user enters:

```text
0
```

as the second number.

This introduces the concept of preventing runtime errors.

---

# Code Practice & Debugging

## Practice 1 — Temperature Converter

Create:

```text
temp_converter.py
```

The program should:

1. Ask for Celsius.
2. Convert the value to `float`.
3. Convert Celsius to Fahrenheit.
4. Display the result to two decimal places.

Formula:

```text
F = (C × 9 / 5) + 32
```

Solution:

```python
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius:.1f}°C is equal to {fahrenheit:.2f}°F")
```

Example:

```text
Enter temperature in Celsius: 25
25.0°C is equal to 77.00°F
```

---

# Practice 2 — Type Conversion Debugging Drill

### Broken Code

```python
age = input("Enter your age: ")
years_left = 100 - age

print(f"You have {years_left} years left until 100.")
```

### Problem

`input()` returns a string.

Therefore:

```python
100 - age
```

attempts to subtract a string from an integer.

This causes a `TypeError`.

### Correct Version

```python
age = int(input("Enter your age: "))

years_left = 100 - age

print(f"You have {years_left} years left until 100.")
```

### General Debugging Pattern

When working with numeric input:

```python
value = input(...)
```

usually needs to become:

```python
value = int(input(...))
```

or:

```python
value = float(input(...))
```

depending on the required data type.

---

# Git: Understanding the Three-Stage Workflow

Git organizes changes through three important areas:

```text
┌──────────────────────┐
│   Working Directory  │
│                      │
│  Files you edit      │
└──────────┬───────────┘
           │
           │ git add
           ▼
┌──────────────────────┐
│    Staging Area      │
│      / Index         │
│                      │
│ Changes selected for │
│ the next commit      │
└──────────┬───────────┘
           │
           │ git commit
           ▼
┌──────────────────────┐
│   Local Repository   │
│                      │
│   Commit history     │
└──────────────────────┘
```

---

# 1. Working Directory

The working directory contains the actual project files you are editing.

For example:

```text
day1_intro.py
day2_datatypes.py
user_calculator.py
temp_converter.py
```

When you create or modify a file, the change initially exists in the working directory.

---

# 2. Staging Area

The staging area allows you to select which changes should be included in the next commit.

For example:

```bash
git add day2_datatypes.py
```

Only that file is staged.

You can stage multiple files:

```bash
git add day2_datatypes.py user_calculator.py
```

Or stage all current changes:

```bash
git add .
```

---

# 3. Local Repository

The repository stores committed snapshots.

A commit represents a checkpoint in the project's history.

Example:

```bash
git commit -m "feat: add variables and type conversion exercises"
```

---

# Git Practice

## Step 1 — Check Current Status

Run:

```bash
git status
```

Look for:

* Untracked files
* Modified files
* Staged files
* Current branch

---

## Step 2 — Stage Day 2 Files

For example:

```bash
git add day2_datatypes.py
git add user_calculator.py
git add temp_converter.py
```

Or:

```bash
git add day2_datatypes.py user_calculator.py temp_converter.py
```

Then verify:

```bash
git status
```

---

# Step 3 — Review Staged Changes

Before committing, you can inspect what has been staged:

```bash
git diff --staged
```

This is an important professional habit because it allows you to review the exact changes that will become part of the commit.

---

# Step 4 — Commit Changes

Create a meaningful commit:

```bash
git commit -m "feat: add variables type casting and calculator exercises"
```

Then verify:

```bash
git status
```

A clean working tree should indicate that there are no remaining changes to commit.

---

# Understanding the Git Workflow

The complete workflow practiced on Day 2 is:

```text
Create / Modify Code
        ↓
   git status
        ↓
    git add
        ↓
git diff --staged
        ↓
   git commit
        ↓
   git status
```

This workflow becomes the foundation for managing the entire Python project.

---

# Mini Project — Receipt Generator

Create:

```text
receipt_generator.py
```

The program should ask the user for:

1. Item name — `str`
2. Quantity — `int`
3. Unit price — `float`

Calculate:

```text
total = quantity × unit_price
```

### Example Implementation

```python
print("================================")
print("       RECEIPT GENERATOR")
print("================================")

item_name = input("Enter item name: ")
quantity = int(input("Enter quantity: "))
unit_price = float(input("Enter unit price: "))

total = quantity * unit_price

print("\n----------- RECEIPT ------------")
print(f"Item:       {item_name}")
print(f"Quantity:   {quantity}")
print(f"Unit Price: Rs. {unit_price:.2f}")
print(f"Total:      Rs. {total:.2f}")
print("--------------------------------")
print("Thank you!")
```

### Example Output

```text
================================
       RECEIPT GENERATOR
================================

Enter item name: Notebook
Enter quantity: 3
Enter unit price: 150

----------- RECEIPT ------------
Item:       Notebook
Quantity:   3
Unit Price: Rs. 150.00
Total:      Rs. 450.00
--------------------------------
Thank you!
```

---

# Mini Project Git Workflow

After completing the receipt generator:

```bash
git status
```

Stage the file:

```bash
git add receipt_generator.py
```

Review the staged change:

```bash
git diff --staged
```

Commit it:

```bash
git commit -m "feat: add receipt generator"
```

Finally:

```bash
git status
```

---

# Common Errors & Troubleshooting

## `ValueError`

If the program expects an integer:

```python
age = int(input("Enter age: "))
```

but the user enters:

```text
twenty
```

Python cannot convert it to an integer and raises a `ValueError`.

---

## `TypeError`

Example:

```python
age = input("Enter age: ")

result = age + 10
```

`age` is a string, while `10` is an integer.

Convert the input first:

```python
age = int(input("Enter age: "))
result = age + 10
```

---

## `ZeroDivisionError`

This occurs when attempting:

```python
result = 10 / 0
```

When creating calculators, consider how division by zero should be handled.

---

# Day 2 Deliverables

By the end of Day 2, the project should include:

```text
class/day2/
│
├── day2_datatypes.py
├── user_calculator.py
├── temp_converter.py
└── receipt_generator.py
```

The learner should have practiced:

* [ ] Variable assignment
* [ ] Dynamic typing
* [ ] `type()`
* [ ] PEP 8 naming conventions
* [ ] Multiple assignment
* [ ] `int`
* [ ] `float`
* [ ] `str`
* [ ] `bool`
* [ ] `complex`
* [ ] `input()`
* [ ] Type conversion
* [ ] f-strings
* [ ] Basic calculations
* [ ] Debugging `TypeError`
* [ ] Debugging `ValueError`
* [ ] `git status`
* [ ] `git add`
* [ ] `git diff --staged`
* [ ] `git commit`

---

# Expected Outcome

After completing Day 2, the learner can take raw console input, convert it into appropriate Python data types, perform calculations, and produce clean formatted output.

The learner also understands how Git moves changes from the working directory into the staging area and finally into the repository's commit history.

The complete Day 2 workflow is:

```text
                 PYTHON
                    │
        ┌───────────▼───────────┐
        │      User Input        │
        └───────────┬───────────┘
                    ↓
             Type Conversion
                    ↓
             Data Processing
                    ↓
             Formatted Output
                    │
                    ▼
                  GIT
                    │
             Modify Files
                    ↓
              git status
                    ↓
                git add
                    ↓
           git diff --staged
                    ↓
               git commit
                    ↓
             Project History
```

Day 2 therefore establishes the practical connection between **Python data handling** and **professional source-code management with Git**.
