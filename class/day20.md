# Day 20 — Portfolio Project Completion, Defense & Professional Git Release

## Learning Objectives
- Finalize, test, and optimize the **Final Capstone Portfolio Application**.
- Conduct peer code reviews and merge feature branches into `main`.
- Tag the final version release (`v3.0`), publish a GitHub Release, and present project capstone.

---

## Topics Covered
1. **Final Capstone Execution**:
   - Integrating OOP models, File Services, Exception Handling, and NumPy Analytics Engine.
   - CLI user interface execution.
2. **Production Release Workflow**:
   - Final code reviews and branch merging.
   - Release tagging: `git tag -a v3.0 -m "Release v3.0 - Final Portfolio Capstone Project"`.
   - Creating official GitHub Releases via web interface.
3. **Course Graduation**:
   - Portfolio showcase defense.

---

## Practical Capstone Implementation

### Complete Capstone Code: `main.py`
Create `main.py`:

```python
# Day 20 Capstone: Personal Asset & Analytics Management System (PAAMS CLI)
import csv
import json
import time
import numpy as np

# 1. Custom Decorator
def log_execution_time(func):
    def wrapper(*args, **kwargs):
        t0 = time.time()
        res = func(*args, **kwargs)
        print(f"[LOG TIMER] Executed '{func.__name__}' in {time.time()-t0:.4f}s")
        return res
    return wrapper

# 2. OOP Domain Model
class Asset:
    def __init__(self, name: str, symbol: str, price: float, quantity: float):
        self.name = name
        self.symbol = symbol
        self.price = price
        self.quantity = quantity

    def calculate_valuation((self) -> float:
        return self.price * self.quantity

    def __str__(self):
        return f"{self.name} ({self.symbol}): {self.quantity} units @ ${self.price:.2f} = ${self.calculate_valuation():,.2f}"

# 3. Analytics Service with NumPy
class PortfolioAnalytics:
    def __init__(self, assets: list):
        self.assets = assets

    @log_execution_time
    def get_numpy_summary(self):
        prices = np.array([a.price for a in self.assets])
        quantities = np.array([a.quantity for a in self.assets])
        valuations = prices * quantities
        
        total_val = float(np.sum(valuations))
        mean_val = float(np.mean(valuations))
        max_val = float(np.max(valuations))
        
        return {
            "total_valuation": total_val,
            "mean_asset_value": mean_val,
            "max_asset_value": max_val
        }

# 4. CLI Entry Point
def main_cli():
    print("==================================================")
    print("   PERSONAL ASSET & ANALYTICS MANAGEMENT SYSTEM   ")
    print("==================================================")
    
    portfolio = [
        Asset("Bitcoin", "BTC", 65000.0, 1.5),
        Asset("Ethereum", "ETH", 3500.0, 10.0),
        Asset("Apple Inc", "AAPL", 220.0, 50.0)
    ]
    
    print("\n--- Current Holdings ---")
    for asset in portfolio:
        print(asset)
        
    analytics = PortfolioAnalytics(portfolio)
    summary = analytics.get_numpy_summary()
    
    print("\n--- Portfolio NumPy Analytics Summary ---")
    print(f"Total Valuation  : ${summary['total_valuation']:,.2f}")
    print(f"Average Asset Val: ${summary['mean_asset_value']:,.2f}")
    print(f"Highest Asset Val: ${summary['max_asset_value']:,.2f}")
    print("==================================================")

if __name__ == "__main__":
    main_cli()
```

---

## Git / GitHub Practice

### Step 1: Merge Portfolio Setup to Main
```bash
git switch main
git merge feature/portfolio-setup
```

### Step 2: Tag Final Version v3.0 Release
```bash
git tag -a v3.0 -m "Release v3.0: Final Capstone Portfolio Application Complete"
git push origin main --tags
```

---

## Final Graduation Outcome
Congratulations! You have completed the 20-Day Python + Git Zero-to-Hero Program and graduated as a **Practical Python Developer & GitHub Portfolio Creator**.
