# Day 5 — Loops, Iteration Control & Connecting Local Git to GitHub

## Learning Objectives
- Execute iterative loops using `for` loops, `while` loops, and `range()`.
- Control loop iteration using `break`, `continue`, and `pass`.
- Create a GitHub account, set up SSH/HTTPS authentication, and create a remote repository.
- Connect local Git repositories to GitHub remotes (`git remote add`, `git push`).
- **Milestone**: Complete **Project 1** (Interactive CLI Calculator & User Profile Tool).

---

## Topics Covered
1. **Looping Mechanics**:
   - `range(start, stop, step)` sequence generator.
   - `for` loop over sequences (ranges, strings).
   - `while` loops and condition-driven iterations.
   - Loop control statements: `break` (exit loop), `continue` (skip iteration), `pass` (placeholder).
2. **Connecting to GitHub**:
   - What is GitHub? Remote central hosting platform.
   - Adding a remote repository: `git remote add origin <URL>`.
   - Renaming default branch to `main`: `git branch -M main`.
   - Pushing local commits to GitHub: `git push -u origin main`.
3. **Project 1 Deliverable**: Interactive CLI Calculator & Profile Tool.

---

## Theory & Classroom Explanation

### 1. Loop Control Flow
- `for` loops iterate over a predefined sequence.
- `while` loops repeat as long as a boolean condition evaluates to `True`.
- `continue` immediately terminates the current iteration and jumps to the next loop evaluation.
- `break` completely terminates loop execution.

### 2. Local vs Remote Repositories
Local Git stores project history on your computer. **GitHub** hosts the repository online, enabling remote backup, collaboration, and code sharing.

```text
 Local Repository                     GitHub Remote Repository
┌────────────────┐   git push origin  ┌───────────────────────┐
│ Local Commits  │ ─────────────────> │ github.com/user/repo │
└────────────────┘                    └───────────────────────┘
```

---

## Practical Coding Exercises

### Exercise 5.1: Range & Loop Control
Create `day5_loops.py`:

```python
# Day 5: Iteration & Loop Control

print("1. Counting even numbers using for loop & range:")
for num in range(1, 21):
    if num % 2 != 0:
        continue  # Skip odd numbers
    if num > 16:
        break     # Stop loop early
    print(num, end=" ")
print("\n")

print("2. Condition-based iteration using while loop:")
count = 5
while count > 0:
    print(f"Countdown: {count}")
    count -= 1
print("Blast off!")
```

---

## Milestone Deliverable: Project 1 — Interactive CLI Tool

Create `project1_cli_tool.py`:

```python
# Project 1: Interactive CLI Calculator & User Profile System

print("==========================================")
print("       PERSONAL CLI ASSISTANT v1.0        ")
print("==========================================")

user_name = input("Enter your name: ")

while True:
    print(f"\nWelcome {user_name}, select an option:")
    print("1. Run Number Summation Utility")
    print("2. Run String Inverter")
    print("3. Exit Program")
    
    choice = input("Enter choice (1-3): ")
    
    if choice == "1":
        limit = int(input("Enter upper range number: "))
        total_sum = sum(range(1, limit + 1))
        print(f"Sum of numbers from 1 to {limit} is: {total_sum}")
    elif choice == "2":
        text = input("Enter string to reverse: ")
        print(f"Reversed Result: '{text[::-1]}'")
    elif choice == "3":
        print(f"Goodbye {user_name}! Thank you for using CLI Assistant.")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
```

---

## Git / GitHub Practice

### Step 1: Commit Project 1 on Main Branch
```bash
git switch main
git merge feature/conditionals
git add day5_loops.py project1_cli_tool.py
git commit -m "feat: complete Project 1 CLI calculator and profile assistant"
```

### Step 2: Connect Remote GitHub Repository
Connect your local repository to your remote GitHub repository:
```bash
git remote add origin https://github.com/Subhash107k/Python_Git_Class.git
git branch -M main
git push -u origin main
```

---

## Expected Outcome
Student builds interactive looping applications, completes Project 1, connects local repository to GitHub, and performs their first remote push.
