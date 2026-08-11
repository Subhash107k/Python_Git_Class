# Day 9 — Functions, Parameters, Return Values & Git Stash

## Learning Objectives
- Define modular, reusable function blocks using `def`.
- Master positional parameters, keyword arguments, default arguments, and return values.
- Understand variable scope rules (Local vs Global scope).
- Manage uncommitted temporary workspace changes using `git stash`.

---

## Topics Covered
1. **Function Fundamentals**:
   - `def function_name(parameters):` declaration syntax.
   - Parameters vs Arguments.
   - Positional arguments vs Keyword arguments.
   - Default parameter values (`def greet(name="Student"):`).
   - Returning single vs returning multiple values as tuples.
2. **Variable Scope**:
   - Local scope vs Global scope.
   - The `global` keyword (and why to avoid overusing it).
3. **Git Workspace Management (`git stash`)**:
   - Temporarily shelving uncommitted edits: `git stash`.
   - Listing stashed edits: `git stash list`.
   - Applying stashed edits: `git stash pop` / `git stash apply`.

---

## Theory & Classroom Explanation

### 1. Function Architecture & DRY Principle
Functions group statement blocks into reusable units, adhering to the **DRY (Don't Repeat Yourself)** principle.

```python
def calculate_area(width: float, height: float = 10.0) -> float:
    """Calculates rectangle area with default height fallback."""
    return width * height
```

### 2. What is Git Stash?
When switching branches or fetching updates, Git requires a clean working directory. `git stash` takes your uncommitted modifications, saves them on a temporary stack, and resets your working directory to match the `HEAD` commit.

```text
Working Directory (Modified)  ───>  git stash  ───>  Stash Stack [stash@{0}]
Working Directory (Cleaned)   <───  git stash pop  <───  Stack Popped
```

---

## Practical Coding Exercises

### Exercise 9.1: Function Design & Multi-Returns
Create `day9_functions.py`:

```python
# Day 9: Functions, Parameters & Return Values

# Function with default parameters & type hints
def calculate_summary(numbers: list, scale_factor: float = 1.0):
    """Calculates scaled sum and average of a numerical list."""
    if not numbers:
        return 0, 0.0
    
    scaled_numbers = [n * scale_factor for n in numbers]
    total_sum = sum(scaled_numbers)
    average = total_sum / len(scaled_numbers)
    
    # Return multiple values as a tuple
    return total_sum, average

# Calling with positional and keyword arguments
sample_data = [10, 20, 30, 40, 50]

total, avg = calculate_summary(sample_data, scale_factor=1.5)
print(f"Scaled Total  : {total}")
print(f"Scaled Average: {avg}")

# Scope Demonstration (Preserving global scope context from DAY1.ipynb)
app_version = "1.0.0"

def display_info():
    local_status = "Running"
    print(f"App Version: {app_version} | Status: {local_status}")

display_info()
```

---

## Git / GitHub Practice

### Step 1: Modify Working File & Stash Changes
Edit `day9_functions.py` (e.g. add an uncommitted print statement).

Shelve changes:
```bash
git stash
```

Verify clean working tree:
```bash
git status
```

### Step 2: List Stashed Changes
```bash
git stash list
```

### Step 3: Re-apply Stashed Changes
```bash
git stash pop
```

### Step 4: Commit Code
```bash
git add day9_functions.py
git commit -m "feat: implement modular functions with default arguments and variable scope"
```

---

## Mini Task
Write `geometry_helper.py`:
1. Create `calculate_circle(radius)` returning area and circumference.
2. Create `calculate_rectangle(length, width=5.0)` returning area and perimeter.
3. Test functions with default arguments and unpack multiple returns.

Practice `git stash` while editing, pop the stash, and commit.

---

## Expected Outcome
Student defines modular functions with default parameters, unpacks multiple return values, and manages uncommitted edits using `git stash`.
