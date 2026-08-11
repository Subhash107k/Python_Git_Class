# Day 18 — NumPy & Numerical Data Analytics

## Learning Objectives

- Understand NumPy arrays and their advantages over Python lists.
- Create, reshape, filter, and manipulate arrays.
- Use vectorization and broadcasting for fast calculations.
- Perform basic matrix operations.
- Save and load NumPy `.npy` files.
- **Milestone:** Complete the inventory analytics engine exercise.

---

## Topics Covered

### 1. NumPy Fundamentals

- `np.array()`
- `np.zeros()`, `np.ones()`
- `np.arange()`, `np.linspace()`
- `.shape`, `.ndim`, `.size`
- `.reshape()` and `.T`

### 2. Array Operations

- Element-wise arithmetic.
- Vectorization.
- Broadcasting.
- Boolean masking and filtering.

Example:

```python
import numpy as np

numbers = np.array([10, 25, 60, 80])
print(numbers[numbers > 50])
```

### 3. Linear Algebra

- Matrix multiplication: `@`, `np.matmul()`
- Determinant: `np.linalg.det()`
- Inverse: `np.linalg.inv()`

### 4. NumPy File Storage

- `np.save()` — save arrays.
- `np.load()` — load arrays.
- `.npy` — efficient binary NumPy format.

---

## Theory & Classroom Explanation

### Why NumPy?

Python lists store references to Python objects, while NumPy arrays store data in a more efficient, uniform structure. NumPy also performs many operations through optimized compiled code.

### Broadcasting

Broadcasting allows NumPy to perform operations between compatible arrays of different shapes.

```python
matrix + row_vector
```

The smaller array can automatically be applied across matching dimensions.

---

## Inventory Analytics Engine Exercise

Build an inventory system that:

- Stores prices and quantities using NumPy arrays.
- Calculates total inventory value.
- Filters high-value inventory using boolean masking.
- Uses an OOP class to organize the analytics logic.
- Saves analytics data using `.npy`.

**Suggested file:**

```text
inventory_analytics.py
```

---

## Git / GitHub Practice

Add NumPy-generated files to `.gitignore`:

```text
*.npy
```

Commit the inventory analytics exercise:

```bash
git add day18_numpy_analytics.py inventory_analytics.py .gitignore
git commit -m "feat: complete inventory analytics with NumPy"
```

Create release tag:

```bash
git tag -a v2.0 -m "Release Version 2.0 - NumPy Analytics"
git push origin main
git push origin --tags
```

---

## Expected Outcome

Student understands NumPy arrays, vectorization, broadcasting, masking, matrix operations, and `.npy` storage while completing the inventory analytics exercise.
