# Day 4 — Conditional Logic, Decision Making & Git Branching Basics

## Learning Objectives
- Control program execution using `if`, `elif`, and `else` statements.
- Evaluate boolean expressions, truthy/falsy values, and compound conditions.
- Understand why Git branches exist and how isolation protects production code.
- Create and switch between Git feature branches (`git branch`, `git switch`).

---

## Topics Covered
1. **Conditional Control Flow**:
   - Truthy and Falsy values in Python (Empty strings, `0`, `None`, empty lists are Falsy).
   - `if`, `elif`, `else` execution blocks.
   - Nested conditional statements.
   - Logical chaining with `and`, `or`, and `not`.
2. **PEP 8 Code Structure**:
   - Indentation block rules (4 spaces).
3. **Git Branching Fundamentals**:
   - Why branches exist (isolating feature development from stable code).
   - Listing branches: `git branch`.
   - Creating feature branches: `git branch <branch-name>`.
   - Switching branches: `git switch <branch-name>` (or `git checkout <branch-name>`).
   - Create & switch shortcut: `git switch -c <branch-name>`.

---

## Theory & Classroom Explanation

### 1. Conditional Logic Execution
Conditionals allow programs to execute specific blocks of code based on dynamic evaluations:

```python
if condition_1:
    # Code block 1
elif condition_2:
    # Code block 2
else:
    # Fallback block
```

### 2. Git Branching Isolation
A **branch** in Git represents an independent line of development. The default branch is usually named `main` or `master`. Creating a branch creates a pointer to a specific commit snapshot, allowing developers to work on new features without corrupting working code on `main`.

```text
       (Feature Branch)  ───> C3 ───> C4
                        /
main:  C0 ─────────> C1 ──────────────> C2 (Main Branch)
```

---

## Practical Coding Exercises

### Exercise 4.1: Grading & Decision Logic
Create `day4_conditionals.py`:

```python
# Day 4: Conditional Logic & Decision Making

score_input = input("Enter exam score (0 - 100): ")

# Input validation using conditional check
if score_input.replace(".", "", 1).isdigit():
    score = float(score_input)
    
    if 0 <= score <= 100:
        if score >= 90:
            grade = "A (Distinction)"
        elif score >= 80:
            grade = "B (Very Good)"
        elif score >= 70:
            grade = "C (Good)"
        elif score >= 60:
            grade = "D (Pass)"
        else:
            grade = "F (Fail)"
            
        print(f"Score: {score} | Evaluation: {grade}")
    else:
        print("Error: Score must be between 0 and 100.")
else:
    print("Invalid input: Please enter a valid number.")
```

---

## Git / GitHub Practice

### Step 1: Create a Feature Branch
Create and switch to a new branch for conditional features:
```bash
git switch -c feature/conditionals
```
*(Or `git checkout -b feature/conditionals`)*

Verify active branch:
```bash
git branch
```
*Observe asterisk `*` next to `feature/conditionals`.*

### Step 2: Commit Code on Feature Branch
```bash
git add day4_conditionals.py
git commit -m "feat: add grade evaluator script with input validation"
```

### Step 3: Switch Back to Main Branch to Verify Isolation
```bash
git switch main
```
*Observe `day4_conditionals.py` status on main.*

Switch back to feature branch:
```bash
git switch feature/conditionals
```

---

## Mini Task
Create `login_system.py` on your `feature/conditionals` branch:
1. Define hardcoded `STORED_USER = "admin"` and `STORED_PASS = "python123"`.
2. Accept `username` and `password` input from user.
3. Validate credentials using `if`/`elif`/`else` and logical operators.
4. Output specific error messages for incorrect username vs incorrect password.

Commit the script to `feature/conditionals`.

---

## Expected Outcome
Student builds nested conditional logic, validates user input, and manages isolated Git feature branches.
