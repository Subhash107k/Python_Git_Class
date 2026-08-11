# Day 11 — Modules, Packages, Virtual Environments & Conflict Prevention

## Learning Objectives
- Organize code into reusable custom Python modules and packages.
- Control entry points using `if __name__ == '__main__':`.
- Create and manage isolated Virtual Environments (`venv`).
- Track dependencies with `pip install` and `requirements.txt`.
- Apply Git pre-merge conflict prevention strategies.

---

## Topics Covered
1. **Modules & Packages**:
   - Creating custom modules (`import module_name`, `from module_name import function`).
   - Packaging directories with `__init__.py`.
   - Entry point guards: `if __name__ == '__main__':`.
2. **Virtual Environments & Dependency Management**:
   - Why isolation is required.
   - Creating virtual environments: `python -m venv .venv`.
   - Activating virtual environments (PowerShell / Bash / CMD).
   - Package management: `pip install <package>`, `pip freeze > requirements.txt`.
3. **Git Pre-merge Conflict Prevention**:
   - Syncing local branch with updated `main` before merging.

---

## Theory & Classroom Explanation

### 1. `if __name__ == '__main__':` Guard
When Python imports a module, it executes all top-level statements in that file. Checking `__name__ == '__main__'` ensures that test execution blocks run **only** when the file is executed directly, not when imported.

### 2. Virtual Environments (`venv`)
A virtual environment isolates project dependencies, preventing global library version conflicts between different projects.

---

## Practical Coding Exercises

### Exercise 11.1: Custom Modules & Entry Point Guard
Create custom module `math_helpers.py`:

```python
# Custom Module: math_helpers.py

def add(a: float, b: float) -> float:
    return a + b

def multiply(a: float, b: float) -> float:
    return a * b

def calculate_discount(price: float, discount_percent: float) -> float:
    return price * (1 - discount_percent / 100)

# Entry point guard: Self-test runs only when executed directly
if __name__ == "__main__":
    print("Running math_helpers self-test...")
    assert add(2, 3) == 5
    assert multiply(4, 5) == 20
    print("All math_helpers unit tests passed!")
```

Create main application file `app_main.py`:

```python
# Main Application: app_main.py
from math_helpers import add, calculate_discount

price = 100.0
discount = 15.0
final_price = calculate_discount(price, discount)

print(f"Original Price: ${price:.2f}")
print(f"Discount ({discount}%): ${price - final_price:.2f}")
print(f"Final Price: ${final_price:.2f}")
```

---

## Virtual Environment Setup

### Step 1: Create & Activate Virtual Environment
```bash
# Create virtual environment named .venv
python -m venv .venv

# Activate on Windows PowerShell:
.venv\Scripts\Activate.ps1
# (Or Git Bash: source .venv/Scripts/activate)
```

### Step 2: Install Package & Save Manifest
```bash
pip install requests
pip freeze > requirements.txt
```

---

## Git / GitHub Practice

### Step 1: Verify `.gitignore` Excludes `.venv/`
Ensure `.venv/` is listed in your `.gitignore` file.

### Step 2: Commit Module & Dependency Files
```bash
git add math_helpers.py app_main.py requirements.txt .gitignore
git commit -m "feat: add custom math_helpers module, main entry app, and requirements manifest"
git push origin main
```

---

## Mini Task
1. Create a module `string_helpers.py` containing `reverse_string(s)` and `count_vowels(s)`.
2. Add an `if __name__ == '__main__':` self-test block inside `string_helpers.py`.
3. Create `main_script.py` importing `string_helpers`, run it inside your active `.venv`, and commit.

---

## Expected Outcome
Student builds custom Python modules, manages virtual environments, exports `requirements.txt`, and uses `if __name__ == '__main__':` guards.
