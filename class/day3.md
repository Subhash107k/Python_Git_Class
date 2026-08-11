# Day 3 — Operators, Strings, String Methods & Git Logs

## Learning Objectives
- Master arithmetic, comparison, logical, and assignment operators.
- Understand string immutability, sequence indexing, and slicing.
- Apply built-in string manipulation methods.
- Inspect Git commit history using `git log` and review code changes with `git diff`.

---

## Topics Covered
1. **Operators in Python**:
   - Arithmetic: `+`, `-`, `*`, `/` (float div), `//` (floor div), `%` (modulus), `**` (exponentiation).
   - Comparison: `==`, `!=`, `>`, `<`, `>=`, `<=`.
   - Logical: `and`, `or`, `not`.
2. **String Fundamentals & Slicing**:
   - String immutability (strings cannot be mutated in-place).
   - Zero-indexed sequences: positive `[0]` and negative `[-1]` indexing.
   - Slicing syntax: `sequence[start:stop:step]` (e.g. `text[::-1]` for string reversal).
3. **Built-in String Methods**:
   - `.upper()`, `.lower()`, `.title()`, `.strip()`, `.replace()`, `.split()`, `.join()`.
4. **Git Inspection & History Navigation**:
   - `git log` (viewing commit logs).
   - `git log --oneline --graph --all` (compact formatted commit tree).
   - `git diff` (comparing working tree modifications against staged/committed state).

---

## Theory & Classroom Explanation

### 1. String Immutability
In Python, strings are **immutable**. Once created, their memory contents cannot be altered directly:

```python
name = "ARIMA"
# name[0] = "N"  # Raises TypeError: 'str' object does not support item assignment

# Correct approach: Create a new string
name = name.replace("ARIMA", "NIKESH")
```

### 2. Slicing Mechanics
Slicing extracts substrings using `[start:stop:step]`:
- `start`: Inclusive starting index (default 0).
- `stop`: Exclusive stopping index (up to, but not including).
- `step`: Incremental step (negative step reverses the string).

---

## Practical Coding Exercises

### Exercise 3.1: Operators & String Transformations
Create `day3_strings.py`:

```python
# Day 3: Operators & String Manipulation

# Operators Demo
a, b = 17, 5
print(f"Division: {a / b} | Floor Division: {a // b} | Modulus: {a % b} | Exponent: {a ** b}")

# String Cleaning & Slicing (Preserved from existing material)
raw_text = "  python programming is versatile and powerful!  "
cleaned = raw_text.strip()

print(f"\nCleaned Text: '{cleaned}'")
print(f"Uppercase: {cleaned.upper()}")
print(f"Title Case: {cleaned.title()}")
print(f"First 6 characters: {cleaned[:6]}")
print(f"Reversed string: {cleaned[::-1]}")

# Replacing & Splitting
replaced = cleaned.replace("versatile", "awesome")
words = replaced.split()
joined_with_hyphen = "-".join(words)

print(f"Replaced String: {replaced}")
print(f"Words List: {words}")
print(f"Hyphenated: {joined_with_hyphen}")
```

---

## Git / GitHub Practice

### Step 1: Inspect Unstaged Code Changes with `git diff`
Make edits to `day3_strings.py` and run:
```bash
git diff
```
*Observe exact line-by-line additions (`+`) and deletions (`-`).*

### Step 2: Stage & Commit `day3_strings.py`
```bash
git add day3_strings.py
git commit -m "feat: implement operator arithmetic, string slicing, and string transformations"
```

### Step 3: Inspect Formatted Git Log History
```bash
git log --oneline --graph --all
```

---

## Mini Task
Create `string_analyzer.py` that takes a sentence from user input:
1. Strips leading/trailing whitespace.
2. Displays total word count.
3. Prints the sentence in uppercase and reversed.
4. Checks if the sentence contains the word `"Python"`.

Stage, commit, and inspect your `git log` output.

---

## Expected Outcome
Student slices strings, applies string methods, inspects `git diff` outputs, and navigates compact `git log` histories.
