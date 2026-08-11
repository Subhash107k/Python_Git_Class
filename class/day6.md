# Day 6 — Lists, Tuples & Basic Repository Management

## Learning Objectives
- Master Python sequence types: mutable `list` vs immutable `tuple`.
- Execute list operations: `.append()`, `.insert()`, `.remove()`, `.pop()`, `.sort()`.
- Use custom key functions for list sorting (`key=func`).
- Master tuple packing, tuple unpacking, and sequence indexing.
- Understand remote Git operations: `git fetch` vs `git pull`.

---

## Topics Covered
1. **Lists (`[]`)**:
   - Indexed, ordered, mutable data collections.
   - List methods: `.append()`, `.insert()`, `.remove()`, `.pop()`, `.extend()`, `.sort()`, `.reverse()`.
   - Custom key sorting (e.g., `key=len` or custom proximity functions).
2. **Tuples (`()`)**:
   - Indexed, ordered, immutable data collections.
   - Single element tuple syntax (`t = ("apple",)`).
   - Tuple unpacking: `x, y, z = (10, 20, 30)`.
   - Extended unpacking: `head, *tail = (1, 2, 3, 4, 5)`.
   - Nested lists & tuples indexing: `data[0][1]`.
3. **Git Remote Management**:
   - `git fetch` (downloading remote history without merging).
   - `git pull` (fetching and merging remote updates into working branch).

---

## Theory & Classroom Explanation

### 1. Lists vs Tuples
- **Lists** are **mutable**: elements can be added, deleted, or altered in-place.
- **Tuples** are **immutable**: once created, elements cannot be added, removed, or changed. Tuples provide data integrity and performance advantages.

```python
mutable_list = [1, 2, 3]
mutable_list[0] = 99  # Valid: [99, 2, 3]

immutable_tuple = (1, 2, 3)
# immutable_tuple[0] = 99  # TypeError
```

---

## Practical Coding Exercises

### Exercise 6.1: Custom List Sorting & Tuples
Create `day6_sequences.py`:

```python
# Day 6: Lists, Custom Sorting & Tuples

# Custom Sort Key Function (Preserved from existing ListMethod.ipynb material)
def proximity_to_fifty(n):
    return abs(n - 50)

numbers = [100, 50, 65, 82, 23]
print("Original Numbers:", numbers)

numbers.sort(key=proximity_to_fifty)
print("Sorted by proximity to 50:", numbers)

# List Operations
fruits = ["apple", "orange", "banana"]
fruits.append("mango")
fruits.insert(1, "pineapple")
popped_item = fruits.pop(2)

print(f"\nFruit List: {fruits}")
print(f"Popped Item: {popped_item}")

# Tuple Unpacking
coordinates = (27.7172, 85.3240, 1400)
latitude, longitude, elevation = coordinates
print(f"\nLocation -> Lat: {latitude}, Lon: {longitude}, Elevation: {elevation}m")

# Extended Unpacking
first, *middle, last = (10, 20, 30, 40, 50)
print(f"First: {first}, Middle: {middle}, Last: {last}")
```

---

## Git / GitHub Practice

### Step 1: Fetch Remote History Changes
```bash
git fetch origin
```

### Step 2: Pull Latest GitHub Updates
```bash
git pull origin main
```

### Step 3: Commit Local Work
```bash
git add day6_sequences.py
git commit -m "feat: add list operations, custom sort keys, and tuple unpacking exercises"
git push origin main
```

---

## Mini Task
Create `student_roster.py`:
1. Define a list of tuples containing `(student_name, score)` (e.g. `[("Alice", 88), ("Bob", 95), ("Charlie", 78)]`).
2. Sort the roster in descending order based on score using a custom function or `key=lambda`.
3. Display the sorted roster neatly using f-strings.

Commit and push your script to GitHub.

---

## Expected Outcome
Student manipulates lists and tuples, applies custom sort keys, unpacks sequences, and syncs code via `git pull` and `git push`.
