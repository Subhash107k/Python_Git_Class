# Day 12 — File Handling (TXT, CSV, JSON) & Git Reset Safety

## Learning Objectives
- Read and write files safely using built-in `open()` and context managers (`with`).
- Process CSV files using Python's built-in `csv` module.
- Serialize and deserialize structured data using the `json` module.
- Understand Git file recovery and undo commands: `git restore`, `git revert`, and `git reset`.

---

## Topics Covered
1. **File I/O Basics**:
   - File modes: Read (`'r'`), Write (`'w'`), Append (`'a'`).
   - Context manager safety: `with open(...) as file:`.
2. **CSV Processing**:
   - Reading CSV: `csv.reader()`, `csv.DictReader()`.
   - Writing CSV: `csv.writer()`, `csv.DictWriter()`.
3. **JSON Processing**:
   - `json.dump()` & `json.dumps()` (Serialization).
   - `json.load()` & `json.loads()` (Deserialization).
4. **Git Undo & Recovery Commands**:
   - `git restore <file>` (discard working tree edits).
   - `git revert <commit>` (safe public history undo).
   - `git reset` (`--soft` vs `--hard` CAUTION).

---

## Theory & Classroom Explanation

### 1. Context Managers (`with` statement)
Opening files without context managers risks leaving file handles open if an exception occurs. The `with` statement guarantees file handles close automatically upon exiting the block:

```python
with open("data.txt", "w", encoding="utf-8") as f:
    f.write("Safe file writing!")
```

### 2. Git Safe Undo Tools
- `git restore`: Restores modified files in working directory back to staged state.
- `git revert`: Creates a **new commit** that reverses changes from an earlier commit. Safe for shared repositories.
- `git reset --hard`: Wipes working directory and staging index to match a specified commit.

> [!CAUTION]
> Avoid using `git reset --hard` on uncommitted work as lost changes cannot be recovered!

---

## Practical Coding Exercises

### Exercise 12.1: JSON & CSV Data Processing
Create `day12_files.py`:

```python
# Day 12: File Handling (JSON & CSV)
import csv
import json

# 1. JSON Data Writing (Serialization)
users_data = [
    {"id": 1, "username": "alice_dev", "role": "admin", "skills": ["Python", "Git"]},
    {"id": 2, "username": "bob_coder", "role": "user", "skills": ["SQL", "Excel"]}
]

json_filename = "users_export.json"
with open(json_filename, "w", encoding="utf-8") as json_file:
    json.dump(users_data, json_file, indent=4)
print(f"JSON data successfully exported to {json_filename}")

# 2. Reading JSON Data (Deserialization)
with open(json_filename, "r", encoding="utf-8") as json_file:
    loaded_users = json.load(json_file)

# 3. Writing Processed Data to CSV
csv_filename = "users_report.csv"
with open(csv_filename, "w", newline="", encoding="utf-8") as csv_file:
    fieldnames = ["id", "username", "role"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    
    writer.writeheader()
    for user in loaded_users:
        writer.writerow({
            "id": user["id"],
            "username": user["username"],
            "role": user["role"]
        })

print(f"CSV report successfully generated: {csv_filename}")
```

---

## Git / GitHub Practice

### Step 1: Test `git restore` Working File Recovery
Make an unintended edit to `users_export.json`.
Restore file:
```bash
git restore users_export.json
```

### Step 2: Commit New Code & Process Safe Revert
```bash
git add day12_files.py users_export.json users_report.csv
git commit -m "feat: implement JSON serialization and CSV report generation"
```

Revert latest commit safely:
```bash
git revert HEAD --no-edit
```
*Observe new revert commit added to history tree without rewriting past commits.*

---

## Mini Task
Write `log_processor.py`:
1. Create a dictionary containing server status metrics.
2. Save metrics to `server_log.json`.
3. Read `server_log.json`, parse metrics, and write a summary line to `server_summary.txt`.

Stage and commit changes.

---

## Expected Outcome
Student safely reads and writes TXT, CSV, and JSON files using context managers, and applies safe Git recovery tools.
