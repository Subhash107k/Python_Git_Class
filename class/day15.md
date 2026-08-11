# Day 15 — Advanced OOP & GitHub Pull Request Workflows

## Learning Objectives
- Implement the core pillars of OOP: Inheritance, Encapsulation, and Polymorphism.
- Use `super()` constructor chaining and method overriding.
- Protect data attributes using Encapsulation access modifiers (Public, Protected, Private).
- Understand professional GitHub collaboration workflows using Pull Requests (PRs).

---

## Topics Covered
1. **Pillars of OOP**:
   - Encapsulation: Public (`name`), Protected (`_balance`), Private (`__pin`).
   - Getter and Setter methods / properties.
   - Inheritance: Base/Parent class vs Derived/Child class.
   - Using `super().__init__()` for parent class initialization.
   - Polymorphism & Method Overriding.
2. **GitHub Pull Request (PR) Workflow**:
   - Creating feature branches (`git switch -c feature/oop-refactor`).
   - Pushing feature branches to GitHub.
   - Opening Pull Requests via GitHub interface.
   - Peer code review and merging PRs into `main`.

---

## Theory & Classroom Explanation

### 1. Encapsulation & Data Hiding
- **Public** (`self.name`): Accessible anywhere.
- **Protected** (`self._status`): Accessible within class and child subclasses.
- **Private** (`self.__pin`): Name-mangled; inaccessible directly from outside the class.

### 2. GitHub Pull Requests
Pull Requests (PRs) notify team members that a feature branch is ready for review. PRs allow code inspection, discussion, automated testing, and code approvals before merging changes into `main`.

```text
Local Feature Branch ───> git push origin ───> Remote Feature Branch ───> Open Pull Request ───> Merge to Main
```

---

## Practical Coding Exercises

### Exercise 15.1: Inheritance & Encapsulation
Create `day15_advanced_oop.py`:

```python
# Day 15: Advanced OOP — Inheritance & Encapsulation

# Base Class
class BankUser:
    def __init__(self, name: str, user_id: str):
        self.name = name                 # Public attribute
        self.user_id = user_id           # Public attribute
        self._status = "Active"          # Protected attribute
        self.__secret_pin = "1234"       # Private attribute

    def verify_pin(self, pin_input: str) -> bool:
        """Public method accessing private data safely."""
        return self.__secret_pin == pin_input

    def display_profile(self):
        """Polymorphic method base implementation."""
        print(f"User: {self.name} | ID: {self.user_id} | Status: {self._status}")

# Derived Class inheriting from BankUser
class PremiumUser(BankUser):
    def __init__(self, name: str, user_id: str, reward_points: int):
        # Call parent constructor using super()
        super().__init__(name, user_id)
        self.reward_points = reward_points

    # Polymorphic Method Overriding
    def display_profile(self):
        print(f"PREMIUM USER: {self.name} | ID: {self.user_id} | Points: {self.reward_points} | Status: {self._status}")

# Instantiating Derived Class
user1 = BankUser("Bob", "USR001")
user2 = PremiumUser("Alice", "USR002", reward_points=1500)

user1.display_profile()
user2.display_profile()

print("\nAlice PIN Verification ('1234'):", user2.verify_pin("1234"))
print("Alice PIN Verification ('9999'):", user2.verify_pin("9999"))
```

---

## Git / GitHub Practice

### Step 1: Create Branch & Commit
```bash
git switch -c feature/oop-refactor
git add day15_advanced_oop.py
git commit -m "refactor: implement OOP inheritance, encapsulation, and polymorphism"
```

### Step 2: Push Feature Branch to GitHub
```bash
git push -u origin feature/oop-refactor
```

### Step 3: Open Pull Request on GitHub UI
1. Navigate to your GitHub repository in your browser.
2. Click **Compare & pull request** button.
3. Add title: `feat: Add advanced OOP inheritance and encapsulation logic`.
4. Submit PR, conduct code review, and click **Merge pull request**.

### Step 4: Sync Main Branch Locally
```bash
git switch main
git pull origin main
```

---

## Mini Task
Build `shape_calculator.py` using inheritance:
1. Base class `Shape` with abstract method `area()`.
2. Derived classes `Rectangle(Shape)` and `Circle(Shape)` overriding `area()`.
3. Put objects in a list `[Rectangle(4, 5), Circle(3)]` and compute total area using a polymorphic loop.

Submit via Pull Request on GitHub.

---

## Expected Outcome
Student constructs inherited class hierarchies, protects private state using encapsulation, and executes GitHub Pull Request workflows.
