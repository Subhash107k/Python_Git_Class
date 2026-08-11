# Day 17 — Standard Library, Context Managers & Advanced Git Operations

## Learning Objectives
- Explore standard library utility modules: `pathlib`, `datetime`, `math`, `random`.
- Construct custom Context Managers using `__enter__`/`__exit__` and `@contextmanager`.
- Understand advanced Git operations: `git rebase` vs `git merge` and `git cherry-pick`.
- Apply safe Git practices when dealing with linear repository histories.

---

## Topics Covered
1. **Python Standard Library Utility Modules**:
   - Object-oriented filesystem paths: `pathlib.Path`.
   - Date and time formatting: `datetime.datetime`.
   - Mathematical operations & randomness: `math`, `random`.
2. **Custom Context Managers**:
   - Class-based context managers (`__enter__` and `__exit__`).
   - Generator-based context managers using `contextlib.contextmanager`.
3. **Advanced Git Operations**:
   - `git rebase <base-branch>` (linearizing commit trees).
   - `git cherry-pick <commit-hash>` (porting specific commits).
   - Safe Git rules: Never rebase public shared history!

---

## Theory & Classroom Explanation

### 1. Object-Oriented File Paths (`pathlib`)
`pathlib` replaces legacy `os.path` strings with clean object-oriented path methods:

```python
from pathlib import Path

current = Path(".")
for py_file in current.glob("*.py"):
    print(py_file.name, py_file.stat().st_size)
```

### 2. Git Rebase vs Git Merge
- **`git merge`**: Preserves complete history by creating a dedicated merge commit.
- **`git rebase`**: Re-applies your feature commits on top of another base commit, creating a clean linear timeline.

> [!WARNING]
> Only rebase private commits on your local feature branch. Never rebase commits that have already been pushed to public remote branches!

---

## Practical Coding Exercises

### Exercise 17.1: Pathlib & Custom Context Manager
Create `day17_stdlib_context.py`:

```python
# Day 17: Pathlib, Datetime & Custom Context Managers
from pathlib import Path
from datetime import datetime
from contextlib import contextmanager

# 1. Custom Context Manager using @contextmanager
@contextmanager
def file_activity_logger(action_name: str):
    """Context manager logging start and end execution timestamps."""
    start_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{start_time}] START LOG: Beginning action '{action_name}'...")
    try:
        yield
    finally:
        end_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{end_time}] END LOG: Completed action '{action_name}'.\n")

# 2. Workspace File Inspection using Pathlib inside Context Manager
with file_activity_logger("Workspace File Scan"):
    workspace_dir = Path(".")
    print("Python source files found in workspace root:")
    
    for file_path in workspace_dir.glob("*.py"):
        size_kb = file_path.stat().st_size / 1024
        print(f" - {file_path.name:<30} | Size: {size_kb:.2f} KB")
```

---

## Git / GitHub Practice

### Step 1: Cherry-Pick a Specific Commit
Apply a specific commit hash from a feature branch to `main`:
```bash
git cherry-pick <commit-hash>
```

### Step 2: Perform Local Branch Rebase
On feature branch:
```bash
git switch feature/branch
git rebase main
```

### Step 3: Push Updates to Remote
```bash
git switch main
git merge feature/branch
git push origin main
```

---

## Mini Task
Write `log_cleaner.py`:
1. Use `pathlib.Path` to create a directory `temp_logs/` and write 3 dummy `.log` files.
2. Use `@contextmanager` to log the deletion of all `.log` files inside `temp_logs/`.
3. Commit the script and push to GitHub.

---

## Expected Outcome
Student navigates filesystems using `pathlib`, writes custom context managers, and understands advanced Git operations safely.
