# Day 14 — Object-Oriented Programming: Classes, Objects & Git Tagging

## Learning Objectives
- Understand Object-Oriented Programming (OOP) concepts: Blueprints vs Instances.
- Define custom classes, instantiate objects, and use `__init__()` constructors.
- Understand the `self` parameter, instance attributes, and class attributes.
- Custom string representation using `__str__()` and `__repr__()`.
- Create annotated Git release tags (`git tag -a`).

---

## Topics Covered
1. **OOP Fundamentals**:
   - Classes (blueprints defining state & behavior) vs Objects (concrete instances).
   - Constructor method: `def __init__(self, ...):`.
   - Instance attributes vs Class attributes.
   - Instance methods.
   - String representation methods: `__str__()` and `__repr__()`.
2. **Git Tagging & Release Management**:
   - What are Git tags? Markers for specific important points in history.
   - Creating annotated tags: `git tag -a v1.0 -m "Release message"`.
   - Listing tags: `git tag`.
   - Pushing tags to remote GitHub repositories: `git push origin --tags`.

---

## Theory & Classroom Explanation

### 1. Classes vs Objects
A **Class** is a blueprint defining attributes (data state) and methods (behavior). An **Object** is a concrete instance created from that class blueprint.

```python
class Car:
    # Class attribute (shared by all instances)
    wheels = 4

    # Constructor method
    def __init__(self, brand: str, model: str):
        # Instance attributes (unique to each object instance)
        self.brand = brand
        self.model = model
```

### 2. Git Release Tags
While branches move forward with each commit, **tags** point to specific static commits in repository history (such as `v1.0`, `v2.0` software release points).

---

## Practical Coding Exercises

### Exercise 14.1: Domain Class Design
Create `day14_oop_basics.py`:

```python
# Day 14: Object-Oriented Programming Basics

class Student:
    # Class attribute
    school_name = "Python Academy"

    def __init__(self, student_id: str, name: str, gpa: float):
        # Instance attributes
        self.student_id = student_id
        self.name = name
        self.gpa = gpa
        self.enrolled_courses = []

    def enroll_course(self, course_name: str):
        """Instance method adding course to student schedule."""
        self.enrolled_courses.append(course_name)
        print(f"[{self.name}] Enrolled in course: '{course_name}'")

    def update_gpa(self, new_gpa: float):
        """Instance method validating and updating GPA."""
        if 0.0 <= new_gpa <= 4.0:
            self.gpa = new_gpa
            print(f"[{self.name}] Updated GPA to: {self.gpa:.2f}")
        else:
            raise ValueError("GPA must be between 0.0 and 4.0")

    def __str__(self):
        """Human-readable string representation."""
        return f"Student({self.student_id}): {self.name} | GPA: {self.gpa:.2f} | Courses: {len(self.enrolled_courses)}"

# Instantiating Objects
student1 = Student("STU101", "Alice", 3.8)
student2 = Student("STU102", "Bob", 3.5)

# Invoking Methods
student1.enroll_course("Python Fundamentals")
student1.enroll_course("Git Version Control")
student1.update_gpa(3.95)

print("\n" + str(student1))
print(student2)
```

---

## Git / GitHub Practice

### Step 1: Commit OOP Exercises
```bash
git add day14_oop_basics.py
git commit -m "feat: implement Student domain class with custom methods and string representation"
```

### Step 2: Create Annotated Release Tag for Milestone v1.0
```bash
git tag -a v1.0 -m "Release Version 1.0 - Completed Core Python & Data File Processor"
```

Verify tag created:
```bash
git tag
```

### Step 3: Push Commit & Tags to GitHub Remote
```bash
git push origin main
git push origin --tags
```

---

## Mini Task
Create `bank_account.py`:
1. Define a class `BankAccount` with attributes `account_number`, `owner_name`, and `balance` (default `0.0`).
2. Add methods `deposit(amount)`, `withdraw(amount)` (preventing negative balances), and `get_balance()`.
3. Instantiate two accounts, execute transactions, print account summaries, commit, and tag as `v1.1`.

---

## Expected Outcome
Student defines custom classes, instantiates objects, manages state using methods, and tags release milestones in Git.
