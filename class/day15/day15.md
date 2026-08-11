# Day 15 — Advanced OOP & GitHub Pull Requests

## Overview

Day 15 focused on the main advanced OOP concepts—**inheritance, encapsulation, and polymorphism**—along with the professional GitHub Pull Request workflow.

All hands-on Python practice was completed in `day15.ipynb`.

---

## Learning Objectives

* Understand inheritance, encapsulation, and polymorphism.
* Use `super()` to initialize parent classes.
* Override methods in child classes.
* Understand public, protected, and private attributes.
* Create feature branches and submit Pull Requests.

---

## Topics Covered

### Python OOP

* Inheritance
* Encapsulation
* Polymorphism
* Method overriding
* `super()`
* Public attributes
* Protected attributes (`_name`)
* Private attributes (`__name`)
* Properties / getters and setters

### Git & GitHub

* Feature branches
* Pull Requests
* Code review
* PR merging
* Synchronizing `main`

---

## Short Examples

### 1. Inheritance

A child class can reuse functionality from a parent class.

```python
class Animal:
    def speak(self):
        print("Animal sound")


class Dog(Animal):
    pass


dog = Dog()
dog.speak()
```

---

### 2. Encapsulation

Python uses naming conventions to indicate attribute visibility.

```python
class Account:
    def __init__(self):
        self.name = "Alice"       # Public
        self._balance = 1000      # Protected
        self.__pin = "1234"       # Private
```

Private data should normally be accessed through methods.

---

### 3. Polymorphism

Different classes can implement the same method differently.

```python
class Dog:
    def speak(self):
        return "Woof"


class Cat:
    def speak(self):
        return "Meow"


for animal in [Dog(), Cat()]:
    print(animal.speak())
```

---

### 4. `super()`

`super()` allows a child class to call the parent class constructor or methods.

```python
class User:
    def __init__(self, name):
        self.name = name


class Admin(User):
    def __init__(self, name):
        super().__init__(name)
```

---

# Python Practice

All detailed exercises are available in:

```text
day15.ipynb
```

Practice included:

* Inheritance
* Encapsulation
* Private attributes
* `super()`
* Method overriding
* Polymorphism

---

# GitHub Pull Request Workflow

A Pull Request allows changes to be reviewed before they are merged into `main`.

```text
Feature Branch
      ↓
Commit
      ↓
Push to GitHub
      ↓
Pull Request
      ↓
Code Review
      ↓
Merge
      ↓
main
```

### Create Feature Branch

```bash
git switch -c feature/oop-refactor
```

### Commit & Push

```bash
git add .
git commit -m "feat: add advanced OOP examples"
git push -u origin feature/oop-refactor
```

### After PR Merge

```bash
git switch main
git pull origin main
```

---

# Mini Task — Shape Calculator

Create:

```text
Shape
 ├── Rectangle
 └── Circle
```

Each class should implement an `area()` method.

Use a polymorphic loop to calculate the total area.

Submit the work through a GitHub Pull Request.

---

## Day 15 Deliverables

```text
class/
└── day15/
    └── day15.ipynb
```

* [x] Inheritance
* [x] Encapsulation
* [x] Polymorphism
* [x] `super()`
* [x] Method overriding
* [x] Feature branches
* [x] Pull Requests
* [x] Code review

---

## Expected Outcome

By the end of Day 15, the learner can build basic class hierarchies, apply encapsulation and polymorphism, and use a professional **feature branch → Pull Request → review → merge** workflow with GitHub.
