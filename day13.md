# Day 13 — Exception Handling & Resolving Merge Conflicts

## Learning Objectives
- Handle runtime errors gracefully using `try`, `except`, `else`, and `finally`.
- Catch specific exceptions (`FileNotFoundError`, `ValueError`, `KeyError`, `ZeroDivisionError`).
- Raise built-in and custom exceptions.
- Understand how Git merge conflicts occur and resolve conflict markers manually.
- **Milestone**: Complete **Project 2** (Automated Data File Processor & Report Generator).

---

## Topics Covered
1. **Exception Handling Architecture**:
   - `try` block (monitoring error-prone code).
   - `except Exception as e` (handling exceptions).
   - `else` block (executing code when no exception occurs).
   - `finally` block (executing cleanup code unconditionally).
   - Raising exceptions using `raise`.
2. **Git Merge Conflicts**:
   - Why conflicts occur (simultaneous changes on identical lines).
   - Understanding conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).
   - Resolving conflicts manually and finalizing merge commits.
3. **Project 2 Deliverable**: Automated Data File Processor with Exception Logging.

---

## Theory & Classroom Explanation

### 1. Exception Handling Architecture
Errors occur during runtime (file missing, bad input, invalid index). Exception handling prevents programs from crashing abruptly:

```python
try:
    file = open("config.json")
except FileNotFoundError as e:
    print(f"Error caught: {e}")
else:
    print("File opened successfully!")
finally:
    print("Cleanup complete.")
```

### 2. Resolving Git Merge Conflicts
When two branches modify the same line of a file, Git cannot determine which version to keep automatically. Git halts the merge and inserts **conflict markers**:

```text
<<<<<<< HEAD (Current Branch)
print("Hello from Main Branch")
=======
print("Hello from Feature Branch")
>>>>>>> feature/branch-b
```

To resolve: Edit the file, remove the conflict markers, select the desired code state, run `git add`, and run `git commit`.

---

## Practical Coding Exercises

### Exercise 13.1: Exception Handling Logic
Create `day13_exceptions.py`:

```python
# Day 13: Exception Handling Architecture
import json

def load_and_parse_json(file_path: str):
    """Safely loads JSON file with full exception handling."""
    try:
        print(f"Attempting to read file: '{file_path}'...")
        with open(file_path, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data
    except FileNotFoundError:
        print(f"[ERROR] Target file '{file_path}' was not found.")
    except json.JSONDecodeError as err:
        print(f"[ERROR] Failed to parse JSON contents: {err}")
    except Exception as err:
        print(f"[UNEXPECTED ERROR] {err}")
    else:
        print("[SUCCESS] Data parsed without error!")
    finally:
        print("[LOG] File read attempt completed.\n")
    return None

# Test missing file error handling
load_and_parse_json("non_existent_file.json")
```

---

## Milestone Deliverable: Project 2 — File Data Processor

Create `project2_file_processor.py`:

```python
# Project 2: Automated JSON/CSV Data Processor & Report Generator
import csv
import json

def process_transaction_file(input_json: str, output_csv: str):
    try:
        with open(input_json, "r", encoding="utf-8") as f:
            transactions = json.load(f)
            
        total_amount = 0
        valid_records = []
        
        for item in transactions:
            if "amount" not in item or "account" not in item:
                raise KeyError(f"Invalid transaction record schema: {item}")
            
            amount = float(item["amount"])
            total_amount += amount
            valid_records.append(item)
            
        with open(output_csv, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "account", "amount"])
            writer.writeheader()
            writer.writerows(valid_records)
            
        print(f"Project 2 Success: Processed {len(valid_records)} records.")
        print(f"Total Portfolio Transaction Amount: ${total_amount:.2f}")
        
    except FileNotFoundError:
        print(f"Project 2 Error: Input file '{input_json}' missing.")
    except Exception as e:
        print(f"Project 2 Execution Error: {e}")

# Sample run test
process_transaction_file("users_export.json", "processed_summary.csv")
```

---

## Git / GitHub Practice

### Step 1: Simulate Merge Conflict
1. Create `branch-a` and `branch-b`.
2. Edit line 1 of `conflict_test.txt` differently on both branches.
3. Attempt `git merge branch-b` while on `branch-a`.

### Step 2: Manually Resolve Conflict
Open `conflict_test.txt`, remove `<<<<<<<`, `=======`, and `>>>>>>>` markers, save the file.

Finalize merge:
```bash
git add conflict_test.txt
git commit -m "fix: resolve manual merge conflict between branch-a and branch-b"
```

---

## Expected Outcome
Student constructs exception-handled scripts, completes Project 2, and resolves manual Git merge conflicts cleanly.
