# Day 7 — Sets, Dictionaries & Nested Data Structures

## Learning Objectives
- Work with unordered unique element collections using `set`.
- Perform set algebraic operations (`union`, `intersection`, `difference`).
- Construct key-value mapping structures using `dict`.
- Navigate and query nested data structures (lists of dicts, dicts of dicts).
- Create and work on isolated feature branches in Git.

---

## Topics Covered
1. **Sets (`{}`)**:
   - Unordered collections of unique, immutable elements.
   - Set methods: `.add()`, `.remove()`, `.discard()`, `.pop()`.
   - Set operations: `union()` (`|`), `intersection()` (`&`), `difference()` (`-`).
2. **Dictionaries (`{key: value}`)**:
   - Unordered/insertion-ordered key-value hash maps.
   - Accessing values safely using `.get(key, default)`.
   - Dictionary methods: `.keys()`, `.values()`, `.items()`, `.pop()`, `del`.
   - Iterating over keys, values, and items (`for k, v in d.items():`).
3. **Nested Data Structures**:
   - Deep nested access (e.g. `students["s1"]["courses"][0]`).
4. **Git Feature Branch Isolation**:
   - Creating `feature/data-structures` branch.

---

## Theory & Classroom Explanation

### 1. Sets Mechanics
Sets store distinct values by computing hash values for each element. Duplicates are automatically discarded:

```python
raw = [1, 2, 2, 3, 3, 3]
unique_set = set(raw)  # {1, 2, 3}
```

### 2. Dictionaries Mechanics
Dictionaries store associations between unique immutable keys and arbitrary values. Retrieving values by key operates in $O(1)$ constant time complexity.

---

## Practical Coding Exercises

### Exercise 7.1: Sets & Nested Dictionaries
Create `day7_dict_sets.py`:

```python
# Day 7: Sets, Dictionaries & Nested Structures

# Set Algebra (Preserved from existing material)
tags_a = {"python", "git", "coding", "vscode"}
tags_b = {"git", "github", "linux", "python"}

print("Union (All tags):", tags_a | tags_b)
print("Intersection (Common tags):", tags_a & tags_b)
print("Difference (Tags in A but not B):", tags_a - tags_b)

# Nested Dictionaries
student_database = {
    "STD101": {
        "name": "Alice",
        "age": 20,
        "courses": ["Math", "Python"],
        "active": True
    },
    "STD102": {
        "name": "Bob",
        "age": 22,
        "courses": ["SQL", "Git"],
        "active": False
    }
}

# Accessing nested structures
print("\nAlice's Second Course:", student_database["STD101"]["courses"][1])

# Iterating over dictionary items
print("\n--- Student Roster Summary ---")
for student_id, info in student_database.items():
    status = "Active" if info["active"] else "Inactive"
    print(f"[{student_id}] {info['name']} ({info['age']} yrs) - Status: {status}")
```

---

## Git / GitHub Practice

### Step 1: Create Branch for Data Structures
```bash
git switch -c feature/data-structures
```

### Step 2: Stage & Commit Code
```bash
git add day7_dict_sets.py
git commit -m "feat: implement set operations and nested dictionary lookups"
```

---

## Mini Task
Build `inventory_manager.py` using nested dictionaries:
1. Define an inventory structure tracking item stock, price, and supplier.
2. Write functions to:
   - Add stock to an existing item.
   - Calculate total value of all inventory items (`stock * price`).
   - Remove out-of-stock items.

Commit `inventory_manager.py` to `feature/data-structures`.

---

## Expected Outcome
Student constructs set algebra logic, queries nested dictionaries, and isolates code edits on feature branches.
