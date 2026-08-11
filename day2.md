# Day 2 — Variables, Data Types, Type Conversion & Git Staging

## Learning Objectives
- Understand dynamic typing, variable declarations, and PEP 8 naming conventions.
- Master Python scalar data types (`int`, `float`, `str`, `bool`, `complex`).
- Perform explicit type casting (`int()`, `float()`, `str()`, `bool()`).
- Capture user input using `input()` and format output using f-strings.
- Understand the Git 3-Stage Architecture (Working Directory $\rightarrow$ Staging Area $\rightarrow$ Repository).
- Execute basic Git workflow commands: `git status`, `git add`, `git commit`.

---

## Topics Covered
1. **Python Variables & Memory**:
   - Creating variables and assign values (`x = 10`).
   - Dynamic typing vs static typing (`type()`).
   - PEP 8 naming conventions (snake_case vs camelCase).
   - Multiple assignment (`a, b, c = 10, 20, 30`).
2. **Fundamental Data Types**:
   - Integers (`int`), Floating-point numbers (`float`), Strings (`str`), Booleans (`bool`).
   - Complex numbers (`complex`: real and imaginary components).
3. **Type Conversion & Input**:
   - Explicit casting: `int()`, `float()`, `str()`, `bool()`.
   - Capturing user console input with `input()`.
   - String interpolation using f-strings (`f"Hello {name}"`).
4. **Git Staging & Committing**:
   - Working Directory vs Staging Area (Index) vs Commit History.
   - `git status` (checking file state).
   - `git add <file>` (staging changes).
   - `git commit -m "message"` (saving snapshots).

---

## Theory & Classroom Explanation

### 1. Variables in Python
In Python, a variable is not a container holding data; it is a **reference/label pointing to an object in memory**. 

```python
x = 5       # 'x' points to an integer object 5
x = "Hello" # 'x' now points to a string object "Hello"
```

Python determines data types dynamically at runtime. You can inspect the data type of any variable using `type(variable)`.

### 2. The 3 Stages of Git
Git manages files across three distinct states:
1. **Working Directory**: The actual files on your hard drive that you are currently editing.
2. **Staging Area (Index)**: A temporary buffer holding changes you intend to include in your next snapshot.
3. **Local Repository**: The `.git` database containing all committed history snapshots.

```text
 Working Directory          Staging Area           Local Repository
┌──────────────────┐       ┌────────────┐       ┌────────────────────┐
│ Edit files       │ ───>  │ git add    │ ───>  │ git commit -m "..."│
└──────────────────┘       └────────────┘       └────────────────────┘
```

---

## Practical Coding Exercises

### Exercise 2.1: Data Types & Type Conversion
Create `day2_datatypes.py`:

```python
# Day 2: Variables, Data Types & Casting

# Variable declarations
user_name = input("Enter your username: ")
age_input = input("Enter your age: ")
height_input = input("Enter your height in meters (e.g., 1.75): ")

# Type Conversion (input() always returns str)
age = int(age_input)
height = float(height_input)
is_student = True

# Complex number example (preserving complex type from existing material)
complex_val = 3 + 4j
print(f"Complex number: {complex_val}, Real: {complex_val.real}, Imag: {complex_val.imag}")

# Output formatting with f-strings
print("\n--- User Profile Summary ---")
print(f"Username: {user_name} | Type: {type(user_name)}")
print(f"Age: {age} years | Type: {type(age)}")
print(f"Height: {height}m | Type: {type(height)}")
print(f"Is Student: {is_student} | Type: {type(is_student)}")
```

### Exercise 2.2: User Calculator
Create `user_calculator.py`:

```python
# Simple Sum Calculator
num1_str = input("Enter first number: ")
num2_str = input("Enter second number: ")

# Explicit casting
num1 = float(num1_str)
num2 = float(num2_str)
result = num1 + num2

print(f"Calculation: {num1} + {num2} = {result}")
```

---

## Code Practice & Debugging Exercises

### Practice 1: Temperature Conversion Challenge
Write a script `temp_converter.py` that asks the user for a temperature in Celsius (`float`), converts it to Fahrenheit using $F = (C \times \frac{9}{5}) + 32$, and prints the result rounded to 2 decimal places using an f-string.

```python
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius:.1f}°C is equal to {fahrenheit:.2f}°F")
```

### Practice 2: Type Casting Debugging Drill
Fix the `TypeError` in the script below:

```python
# BROKEN CODE - FIX ME
# age = input("Enter your age: ")
# years_left = 100 - age
# print(f"You have {years_left} years left until 100.")

# CORRECTED SOLUTION:
age = int(input("Enter your age: "))
years_left = 100 - age
print(f"You have {years_left} years left until 100.")
```

---

## Git / GitHub Practice

### Step 1: Check Working Directory Status
```bash
git status
```
*Observe untracked files highlighted in red.*

### Step 2: Stage Specific Files
```bash
git add day1_intro.py day2_datatypes.py user_calculator.py temp_converter.py
```

Check status again:
```bash
git status
```
*Observe files ready to be committed highlighted in green.*

### Step 3: Create Your First Commit
```bash
git commit -m "feat: add variable assignment, type casting, and calculator script"
```

---

## Mini Task
Build a script `receipt_generator.py` that asks the user for:
1. Item name (`str`)
2. Quantity (`int`)
3. Unit price (`float`)

Calculate total cost (`quantity * unit_price`), format the receipt output neatly using f-strings, run the script, stage it, and commit it with a clear commit message.

---

## Expected Outcome
Student takes console user input, casts variables safely, formats clean f-strings, and stages/commits changes into Git history.
