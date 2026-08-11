# Day 18 — Numerical Computing with NumPy & Advanced Data Analytics

## Learning Objectives
- Understand fast numerical array processing using NumPy (`np.ndarray`).
- Master array creation, reshaping, boolean masking, vectorization, and broadcasting.
- Perform linear algebra matrix operations (`matmul`, `det`, `inv`).
- Save and load efficient binary array files (`.npy`).
- **Milestone**: Complete **Project 3** (OOP Inventory System + NumPy Analytics Engine).

---

## Topics Covered
1. **NumPy Fundamentals**:
   - `np.ndarray` vs standard Python lists.
   - Array creation: `np.array()`, `np.zeros()`, `np.ones()`, `np.arange()`, `np.linspace()`.
   - Reshaping & dimensional attributes: `.shape`, `.ndim`, `.size`, `.reshape()`, `.T`.
2. **Vectorization & Indexing**:
   - Element-wise arithmetic & Broadcasting rules.
   - Boolean indexing (Masking): `arr[arr > 50]` (preserving `day4.ipynb` material).
   - Linear algebra: matrix multiplication (`@`, `np.matmul`), determinant (`np.linalg.det`), inverse (`np.linalg.inv`).
   - Saving and loading binary arrays: `np.save()` and `np.load()`.
3. **Project 3 Deliverable**: OOP Inventory System + NumPy Analytics Engine.

---

## Theory & Classroom Explanation

### 1. Why Use NumPy?
Standard Python lists store references to objects scattered in memory. NumPy arrays store elements in **contiguous memory blocks** of uniform data types. Operations execute in compiled C routines, providing up to $100\times$ faster execution.

### 2. Broadcasting Rules
Broadcasting allows element-wise operations between arrays of different shapes when:
1. Array dimensions match, or
2. One of the array dimensions has a length of 1.

---

## Practical Coding Exercises

### Exercise 18.1: NumPy Analytics & Matrix Operations
Create `day18_numpy_analytics.py`:

```python
# Day 18: Numerical Computing & Analytics with NumPy
import numpy as np

# 1. Vectorized Matrix Arithmetic & Broadcasting (Preserved from Day_Two.ipynb)
matrix = np.array([[10, 20, 30], 
                   [40, 50, 60]])
row_vector = np.array([1, 2, 3])

# Broadcasting row_vector across matrix rows
broadcasted_sum = matrix + row_vector
print("Matrix:\n", matrix)
print("Broadcasted Result:\n", broadcasted_sum)

# 2. Boolean Masking (Filtering data without loops)
data = np.random.randint(10, 100, size=15)
high_values = data[data > 50]
print("\nRandom Dataset:", data)
print("Filtered Values (> 50):", high_values)

# 3. Linear Algebra Matrix Operations
square_matrix = np.array([[4, 2], [3, 1]])
determinant = np.linalg.det(square_matrix)
inverse_matrix = np.linalg.inv(square_matrix)

print("\nSquare Matrix:\n", square_matrix)
print(f"Determinant: {determinant:.2f}")
print("Inverse Matrix:\n", inverse_matrix)

# 4. Binary File Persistence (.npy)
binary_filename = "analytics_cache.npy"
np.save(binary_filename, broadcasted_sum)
loaded_cache = np.load(binary_filename)
print(f"\nSaved and reloaded binary cache shape: {loaded_cache.shape}")
```

---

## Milestone Deliverable: Project 3 — Inventory Analytics Engine

Create `project3_inventory_analytics.py`:

```python
# Project 3: OOP Inventory System + NumPy Analytics Engine
import numpy as np

class InventoryAnalyticsEngine:
    def __init__(self, item_prices: list, stock_quantities: list):
        self.prices = np.array(item_prices, dtype=float)
        self.quantities = np.array(stock_quantities, dtype=int)

    def calculate_total_valuation(self) -> float:
        # Vectorized multiplication
        item_values = self.prices * self.quantities
        return float(np.sum(item_values))

    def filter_high_value_items(self, threshold: float):
        total_values = self.prices * self.quantities
        mask = total_values > threshold
        return self.prices[mask], self.quantities[mask]

# Run Test
engine = InventoryAnalyticsEngine([19.99, 49.99, 5.00, 120.00], [100, 20, 500, 15])
print(f"Project 3 Total Portfolio Value: ${engine.calculate_total_valuation():,.2f}")
```

---

## Git / GitHub Practice

### Step 1: Update `.gitignore` for NumPy Binary Files
Ensure `*.npy` is in your `.gitignore` file.

### Step 2: Commit Code & Push Release Tag v2.0
```bash
git add day18_numpy_analytics.py project3_inventory_analytics.py .gitignore
git commit -m "feat: complete Project 3 OOP inventory analytics engine with NumPy vectorization"
git tag -a v2.0 -m "Release Version 2.0 - Completed Intermediate Python & NumPy Analytics"
git push origin main
git push origin --tags
```

---

## Expected Outcome
Student executes vectorized array calculations, boolean masking, matrix math, and binary array I/O, completing Project 3.
