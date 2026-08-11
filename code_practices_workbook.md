# 20-Day Python + Git Coding Practice & Debugging Workbook

This workbook contains dedicated hands-on coding exercises, problem-solving challenges, and debugging drills for each of the 20 days in the **Python + Git Zero-to-Hero Program**.

---

## Day 1 — Setup, Syntax & Interpreter Practices

### Challenge 1.1: Multi-Line Banner Output
Write a script `practice_day1_banner.py` that prints a formatted 3-line ASCII banner containing your name, preferred IDE, and operating system.

### Challenge 1.2: Syntax Fix Debugging
The following script has 3 syntax/execution errors. Locate and fix them:

```python
# BROKEN CODE - FIX ME
print("Starting Python Program"
# Missing parenthesis above
print 'Learning Python Syntax' 
# Missing quotes or parentheses for Python 3
print("Line 3 complete)
```

**Corrected Output**:
```text
Starting Python Program
Learning Python Syntax
Line 3 complete
```

---

## Day 2 — Variables, Data Types & Type Conversion Practices

### Challenge 2.1: Temperature Converter
Write a script `temp_converter.py` that asks the user for a temperature in Celsius (`float`), converts it to Fahrenheit using the formula:
$$F = (C \times \frac{9}{5}) + 32$$
and prints the result rounded to 2 decimal places using an f-string.

### Challenge 2.2: Data Type Debugging
Fix the type error in the script below:

```python
# BROKEN CODE - FIX ME
age = input("Enter your age: ")
years_to_hundred = 100 - age  # TypeError: unsupported operand type(s) for -: 'int' and 'str'
print(f"You will turn 100 in {years_to_hundred} years!")
```

---

## Day 3 — Operators & String Slicing Practices

### Challenge 3.1: Palindrome Checker
Write a script `palindrome_checker.py` that takes a word input, strips leading/trailing spaces, converts it to lowercase, and checks whether it reads the same backward as forward using string slicing (`[::-1]`).

**Test Cases**:
- Input: `" Racecar "` $\rightarrow$ Output: `True ("racecar" == "racecar")`
- Input: `"Python"` $\rightarrow$ Output: `False ("python" != "nohtyp")`

### Challenge 3.2: String Method Debugging
Fix the following script so it correctly replaces space separators with hyphens:

```python
# BROKEN CODE - FIX ME
text = "  python git zero to hero  "
text.strip()
text.replace(" ", "-")
print(text)  # Why didn't text change? Remember string immutability!
```

---

## Day 4 — Conditional Logic Practices

### Challenge 4.1: Leap Year Validator
Write `leap_year.py` that prompts the user for a year (`int`) and determines if it is a leap year according to the rules:
1. Divisible by 4, AND
2. NOT divisible by 100 UNLESS also divisible by 400.

### Challenge 4.2: Condition Boundary Debugging
Fix the logical bug in the age classifier below:

```python
# BROKEN CODE - FIX ME
age = 25

if age > 13:
    print("Teenager")
elif age > 18:
    print("Adult")  # Why does an 18+ adult get classified as Teenager?
else:
    print("Child")
```

---

## Day 5 — Loop & Iteration Practices

### Challenge 5.1: Prime Number Checker
Write `prime_checker.py` that asks for a number $N \ge 2$ and uses a `for` loop with `break` to check if $N$ is prime (divisible only by 1 and itself).

### Challenge 5.2: Infinite Loop Debugging
Fix the infinite loop in the countdown timer below:

```python
# BROKEN CODE - FIX ME
counter = 10
while counter > 0:
    print(f"Countdown: {counter}")
    # Missing counter decrement!
```

---

## Day 6 — Lists, Tuples & Custom Sorting Practices

### Challenge 6.1: Frequency & Proximity Sorter
Write `sort_by_length.py`:
1. Accept a list of words: `["elephant", "dog", "cat", "hippopotamus", "monkey"]`.
2. Sort the words by word length in ascending order using `key=len`.
3. Unpack the shortest word into `shortest` and the rest into `*others`.

### Challenge 6.2: Immutable Tuple Mutability Bug
Fix the attempt to modify a tuple below:

```python
# BROKEN CODE - FIX ME
user_data = ("Alice", 25, "Developer")
user_data[1] = 26  # TypeError: 'tuple' object does not support item assignment
```

---

## Day 7 — Sets & Dictionary Practices

### Challenge 7.1: Duplicate Remover & Word Counter
Write `word_frequency.py`:
1. Take a paragraph string: `"python git python code git python dev"`.
2. Split the paragraph into words and use a `set` to find all unique words.
3. Build a dictionary counting occurrences of each word (`{word: count}`).

### Challenge 7.2: Key Error Debugging
Fix the key error crash below:

```python
# BROKEN CODE - FIX ME
student = {"name": "Bob", "age": 22}
print(student["gpa"])  # KeyError: 'gpa' -> Use .get() safely!
```

---

## Day 8 — Comprehension & Benchmarking Practices

### Challenge 8.1: Matrix Flattener & Filter
Given a 2D matrix `[[1, 2, 3], [4, 5, 6], [7, 8, 9]]`, write a single-line list comprehension that flattens the matrix into a 1D list containing **only odd numbers**: `[1, 3, 5, 7, 9]`.

### Challenge 8.2: Comprehension Syntax Debugging
Fix the syntax error in the dictionary comprehension below:

```python
# BROKEN CODE - FIX ME
# Attempting to map numbers 1 to 5 to their squares if even
squares = {x: x**2 for x in range(1, 6) if x % 2 == 0 else x: 0} # Invalid syntax for if-else in comprehension!
```

---

## Day 9 — Modular Function Practices

### Challenge 9.1: Tax & Tip Calculator
Write `calculator_functions.py`:
1. Function `calculate_total(bill_amount, tax_rate=0.08, tip_rate=0.15)` returning `(tax, tip, final_total)`.
2. Test the function using both positional and keyword arguments.

### Challenge 9.2: Scope Variable Leak Debugging
Fix the variable scope issue below:

```python
# BROKEN CODE - FIX ME
def set_discount():
    discount = 0.20

set_discount()
price = 100 * (1 - discount)  # NameError: name 'discount' is not defined
```

---

## Day 10 — Advanced Function (*args, **kwargs, Lambdas) Practices

### Challenge 10.1: Universal Math Utility
Write `universal_math.py`:
1. Function `math_ops(operation, *numbers, **metadata)` where `operation` can be `"sum"` or `"product"`.
2. Apply `filter()` with a `lambda` to filter out negative numbers before computing.

### Challenge 10.2: Lambda Map Syntax Bug
Fix the map execution below:

```python
# BROKEN CODE - FIX ME
nums = [1, 2, 3, 4]
squared = map(lambda x: x**2, nums)
print("Squared Numbers:", squared)  # Prints <map object at ...> instead of list!
```

---

## Day 11 — Modules & Package Practices

### Challenge 11.1: Custom Helper Package
1. Create file `converters.py` with `km_to_miles(km)` and `c_to_f(c)`.
2. Include an `if __name__ == '__main__':` self-test block.
3. Import `converters` into `main_app.py` and run inside `.venv`.

### Challenge 11.2: Circular Import Debugging
Identify why importing `module_a` from `module_b` causes an `ImportError` when both import each other at top-level.

---

## Day 12 — File Handling Practices

### Challenge 12.1: CSV Transaction Parser
Write `csv_parser.py` that opens a CSV file `expenses.csv` containing headers `category,amount`, calculates total expenditure by category using a dictionary, and writes `summary.json`.

### Challenge 12.2: Unclosed File Handle Bug
Fix the resource leak below using a `with` context manager:

```python
# BROKEN CODE - FIX ME
f = open("data.txt", "w")
f.write("Important data")
# What happens if an exception occurs before f.close()?
```

---

## Day 13 — Exception Handling Practices

### Challenge 13.1: Safe Division Calculator
Write `safe_calculator.py` that continuously prompts the user for two numbers and divides them, catching `ValueError` (for non-numeric inputs) and `ZeroDivisionError` (for division by 0) without crashing.

### Challenge 13.2: Swallowing Exception Bug
Fix the dangerous silent exception handling below:

```python
# BROKEN CODE - FIX ME
try:
    data = int(input("Enter number: "))
except Exception:
    pass  # Silently swallowing errors masks critical bugs!
```

---

## Day 14 — Basic OOP Practices

### Challenge 14.1: Car Fleet Management Class
Write `car_fleet.py`:
1. Class `Car` with attributes `make`, `model`, `year`, `mileage`.
2. Method `drive(distance)` that increments `mileage`.
3. Method `__str__()` displaying car details neatly.

### Challenge 14.2: Missing Self Parameter Bug
Fix the method definition below:

```python
# BROKEN CODE - FIX ME
class Person:
    def __init__(name):  # Missing 'self'!
        name = name
```

---

## Day 15 — Advanced OOP Practices

### Challenge 15.1: Employee Hierarchy
Write `employee_hierarchy.py`:
1. Base class `Employee(name, salary)` with method `get_bonus()` returning `salary * 0.05`.
2. Child class `Manager(Employee, department)` overriding `get_bonus()` returning `salary * 0.15 + 1000`.

### Challenge 15.2: Private Attribute Access Bug
Fix the illegal access to private attribute below:

```python
# BROKEN CODE - FIX ME
class Account:
    def __init__(self):
        self.__balance = 500

acc = Account()
print(acc.__balance)  # AttributeError: 'Account' object has no attribute '__balance'
```

---

## Day 16 — Generator & Decorator Practices

### Challenge 16.1: Fibonacci Generator & Logging Decorator
Write `fibonacci_stream.py`:
1. Generator function `fibonacci_gen(limit)` yielding Fibonacci numbers up to `limit`.
2. Decorator `@log_execution` printing function start/stop times.

### Challenge 16.2: Missing Wrapper Return Bug
Fix the decorator that fails to return the original function's result:

```python
# BROKEN CODE - FIX ME
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Executing...")
        func(*args, **kwargs)  # Missing 'return'!
    return wrapper
```

---

## Day 17 — Standard Library & Context Manager Practices

### Challenge 17.1: Directory Clean-up Utility
Write `directory_cleaner.py`:
1. Use `pathlib.Path` to scan a directory for files older than 30 days.
2. Use `@contextmanager` to log the file audit operation.

### Challenge 17.2: Path Concatenation Bug
Fix string path concatenation using `pathlib.Path` (`path / "filename.txt"`).

---

## Day 18 — NumPy Array Analytics Practices

### Challenge 18.1: Matrix Normalization & Masking
Write `numpy_practices.py`:
1. Create a 5x5 random matrix with values between 10 and 100.
2. Normalize matrix values:
   $$Z = \frac{X - \mu}{\sigma}$$
3. Extract all normalized values greater than `1.0` using boolean masking.

### Challenge 18.2: Incompatible Shape Broadcasting Bug
Fix the shape mismatch error below:

```python
# BROKEN CODE - FIX ME
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6]])  # Shape (2, 3)
b = np.array([10, 20])                 # Shape (2,) -> Cannot broadcast (2,3) with (2,)!
# How to fix? Reshape b to (2, 1) or pass 3 elements!
```

---

## Day 19 — Portfolio Scaffolding Practices

### Challenge 19.1: Package Import Scaffolding
Create `src/utils/validators.py` and test importing it into `main.py` using `from src.utils.validators import validate_email`.

---

## Day 20 — Capstone Integration & Code Review

### Challenge 20.1: Full Application Audit & Test Run
1. Run `python main.py` for your Capstone Project.
2. Verify exception handling when input files are missing.
3. Check `git log --oneline` to ensure all 20 days of commit history exist.
