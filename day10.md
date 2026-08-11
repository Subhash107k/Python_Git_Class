# Day 10 — Advanced Functions (*args, **kwargs, Lambdas) & Merging Branches

## Learning Objectives
- Handle dynamic numbers of positional and keyword arguments using `*args` and `**kwargs`.
- Write anonymous single-line lambda functions.
- Apply functional utilities: `map()` and `filter()`.
- Merge Git feature branches into `main` (`git merge`) and clean up merged branches.

---

## Topics Covered
1. **Dynamic Parameter Packing**:
   - Variable-length positional arguments: `*args` (collected into a tuple).
   - Variable-length keyword arguments: `**kwargs` (collected into a dictionary).
2. **Lambda Expressions & Higher-Order Functions**:
   - Syntax: `lambda inputs: expression`.
   - Transforming sequences using `map(func, iterable)`.
   - Filtering sequences using `filter(func, iterable)`.
3. **Branch Merging & Repository Cleanup**:
   - Switching to target branch: `git switch main`.
   - Merging feature branch: `git merge feature/data-structures`.
   - Deleting local branch: `git branch -d feature/data-structures`.

---

## Theory & Classroom Explanation

### 1. Flexible Functions with `*args` and `**kwargs`
- `*args` allows functions to accept an arbitrary number of positional arguments.
- `**kwargs` allows functions to accept an arbitrary number of keyword arguments.

```python
def flexible_func(*args, **kwargs):
    print("Positional args tuple:", args)
    print("Keyword args dict   :", kwargs)
```

### 2. Git Branch Merging
Merging integrates commits from a source branch into a target branch. If `main` has not diverged, Git performs a fast-forward merge.

---

## Practical Coding Exercises

### Exercise 10.1: Dynamic Arguments & Lambdas
Create `day10_advanced_functions.py`:

```python
# Day 10: *args, **kwargs, Lambdas, map & filter

# Dynamic argument logger using *args and **kwargs
def audit_logger(event_name, *scores, **user_metadata):
    print(f"\n=== EVENT LOG: {event_name.upper()} ===")
    print("Metadata:")
    for key, value in user_metadata.items():
        print(f" - {key.title()}: {value}")
        
    if scores:
        avg_score = sum(scores) / len(scores)
        print(f"Evaluated Scores ({len(scores)} entries): Average = {avg_score:.2f}")

audit_logger("Performance Review", 88, 92, 79, 95, student_id="STU101", role="Engineer")

# Lambda Functions with map() and filter()
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Double numbers using map & lambda
doubled = list(map(lambda x: x * 2, numbers))

# Filter even numbers using filter & lambda
evens = list(filter(lambda x: x % 2 == 0, numbers))

print(f"\nOriginal Numbers: {numbers}")
print(f"Doubled (map)   : {doubled}")
print(f"Evens (filter)  : {evens}")
```

---

## Git / GitHub Practice

### Step 1: Commit `day10_advanced_functions.py` on Feature Branch
```bash
git add day10_advanced_functions.py
git commit -m "feat: implement *args, **kwargs, lambdas, map, and filter functions"
git push origin feature/data-structures
```

### Step 2: Merge Feature Branch into Main
```bash
git switch main
git pull origin main
git merge feature/data-structures
```

### Step 3: Delete Merged Local Branch & Push Main
```bash
git branch -d feature/data-structures
git push origin main
```

---

## Mini Task
Create `flexible_formatter.py`:
1. Define a function `format_invoice(title, *line_items, **tax_rates)`.
2. Compute line item totals and apply keyword tax rates dynamically.
3. Call the function with variable items and tax rates.

Merge changes into `main` and push to GitHub.

---

## Expected Outcome
Student constructs flexible functions with `*args`/`**kwargs`, writes lambdas, and merges Git feature branches cleanly.
