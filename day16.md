# Day 16 — Advanced Python: Iterators, Generators, Decorators & GitHub Issues

## Learning Objectives
- Understand iterables vs iterators (`iter()`, `next()`).
- Create memory-efficient generator functions using `yield`.
- Construct function decorators (`@decorator`) to modify function behavior dynamically.
- Use GitHub Issues to track project tasks and link commits using issue identifiers.

---

## Topics Covered
1. **Iterators & Generators**:
   - The Iterator Protocol (`__iter__()` and `__next__()`).
   - Generators: Lazy evaluation using `yield`.
   - Memory efficiency of generators over lists.
   - Generator expressions: `(x**2 for x in range(1000000))`.
2. **Function Decorators**:
   - Functions as first-class objects (passing functions as arguments).
   - Higher-order wrapper functions.
   - Decorator syntax: `@timing_decorator`, `@log_decorator`.
3. **GitHub Issue Tracking**:
   - Creating issues on GitHub.
   - Linking commits to issues using syntax like `Fixes #12` or `Closes #5`.

---

## Theory & Classroom Explanation

### 1. Generators & Memory Efficiency
Generators calculate sequence values on demand (lazy evaluation) rather than storing all elements in memory simultaneously. This allows processing datasets containing millions of rows with minimal memory usage.

```python
# List: Allocates memory for 1,000,000 integers at once
big_list = [x for x in range(1_000_000)]

# Generator: Calculates one number at a time on demand
big_gen = (x for x in range(1_000_000))
```

### 2. Decorator Mechanics
Decorators dynamically wrap functions to extend or monitor execution without altering original function source code:

```python
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Before function execution")
        result = func(*args, **kwargs)
        print("After function execution")
        return result
    return wrapper
```

---

## Practical Coding Exercises

### Exercise 16.1: Generators & Decorators
Create `day16_advanced_python.py`:

```python
# Day 16: Generators & Function Decorators
import time

# Generator Function
def large_number_stream(limit: int):
    """Generator function yielding numbers one at a time."""
    current = 1
    while current <= limit:
        yield current
        current += 1

# Custom Execution Timer Decorator
def execution_timer(func):
    """Decorator measuring execution duration of wrapped function."""
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"[DECORATOR TIMER] Function '{func.__name__}' executed in {end_time - start_time:.6f} seconds.")
        return result
    return wrapper

# Applying Decorator
@execution_timer
def process_data_stream(limit: int):
    print(f"Processing data stream up to {limit:,} items...")
    stream = large_number_stream(limit)
    total_sum = sum(stream)
    return total_sum

result = process_data_stream(1_000_000)
print(f"Stream Total Sum: {result:,}")
```

---

## Git / GitHub Practice

### Step 1: Create an Issue on GitHub UI
1. Go to your GitHub repository.
2. Click **Issues** $\rightarrow$ **New Issue**.
3. Title: `Optimize memory using generator stream`.
4. Note the issue number assigned (e.g. `#1`).

### Step 2: Commit Code Referencing Issue ID
```bash
git add day16_advanced_python.py
git commit -m "feat: implement generator function stream and timing decorator (Fixes #1)"
git push origin main
```
*Observe GitHub automatically closing Issue #1 upon push.*

---

## Mini Task
Write `decorator_logger.py`:
1. Create a decorator `@log_args_and_return` that prints function arguments and return values.
2. Apply it to a function `multiply(a, b)` and test calls.
3. Link your commit to a GitHub issue.

---

## Expected Outcome
Student builds lazy generators, constructs custom decorators, and links Git commits to GitHub Issue trackers.
