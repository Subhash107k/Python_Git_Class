# Python + Git Zero-to-Hero: Practical Learning Program

---

## 1. ANALYSIS OF EXISTING PYTHON MATERIAL

After analyzing the existing notebook files (`DAY1.ipynb`, `Day_Two.ipynb`, `Day_Three.ipynb`, `day4.ipynb`, `ListMethod.ipynb`, `NUMPY.ipynb`, `Numpy_Guide.ipynb`), the key findings are:

- **`DAY1.ipynb`**: Covers basic print, arithmetic, variables, basic data types (`int`, `float`, `str`, `complex`, `bool`), type casting, f-strings, input/output, string immutability, slicing, string methods (`upper`, `lower`, `strip`, `title`, `replace`), `global` scope, collection overviews, list comprehensions, set methods, tuple unpacking, and dictionary operations.
- **`Day_Two.ipynb` & `Day_Three.ipynb`**: `Day_Three.ipynb` is almost an exact duplicate of `Day_Two.ipynb`. They cover lists/tuples/sets/dicts, memory/speed benchmarking between list and tuple using `sys` and `time`, dict comprehensions, and then jump straight into **NumPy** (`zeros`, `ones`, `linspace`, array concatenation, sorting, slicing, image slicing using `scikit-image` & `matplotlib`, photo masking with `np.where`, matrix math, `@` dot product, `matmul`, `det`, `inv`, `.npy` files).
- **`day4.ipynb`**: Covers NumPy boolean masking, vector math, `@` matrix multiplication, `reshape`, 3D arrays, and `%pip install` for `requests` and `pandas`.
- **`ListMethod.ipynb`**: Covers list sorting (`sort()`, `reverse()`, custom sorting with `key=myfunc`, `help()`).
- **`NUMPY.ipynb` & `Numpy_Guide.ipynb`**: Comprehensive reference notebooks for NumPy array operations, indexing, slicing, reshaping, stacking, splitting, linear algebra, and I/O.
- **Git/GitHub**: Zero Git or GitHub instructions were present in the existing notebook material.

---

## 2. IDENTIFIED PROBLEMS & GAPS

1. **Duplication**: `Day_Two.ipynb` and `Day_Three.ipynb` are duplicate notebooks.
2. **Missing Core Python Fundamentals**: Control Flow details (`break`, `continue`, `pass`), modular Functions (`def`, parameters, return values, `*args`, `**kwargs`), Standard File I/O (`open`, `with`, CSV, JSON), Exception Handling (`try`/`except`), OOP (`class`, inheritance, encapsulation), and Modules/Packages (`import`, `__name__ == '__main__'`, `venv`, `requirements.txt`) were absent or severely incomplete.
3. **Illogical Progression**: Advanced NumPy matrix operations, linear algebra (`det`, `inv`), and RGB image array slicing were introduced on Day 2 before students learned functions, loops, or standard file handling.
4. **No Git Integration**: Version control was completely missing from the existing curriculum.

---

## 3. IMPROVED LEARNING STRATEGY

The curriculum is restructured into a strict 7-stage learning progression:

$$\text{Beginner} \longrightarrow \text{Foundation} \longrightarrow \text{Core Python} \longrightarrow \text{Intermediate Python} \longrightarrow \text{Practical Dev} \longrightarrow \text{Git/GitHub} \longrightarrow \text{Capstone Project}$$

### Key Improvements:
- **Integrated Git & GitHub**: Taught from Day 1 (`git init`, `config`, `.gitignore`) and used daily for staging, committing, and pushing code.
- **Pedagogical Re-Sequencing**: Fundamentals $\rightarrow$ Control Flow $\rightarrow$ Data Structures $\rightarrow$ Functions $\rightarrow$ Modules & File I/O $\rightarrow$ OOP $\rightarrow$ Intermediate Python & NumPy $\rightarrow$ Portfolio Project.
- **Preserved Existing Content**: Preserved string methods, tuple vs list performance benchmarks, dictionary comprehensions, custom key sorting, and NumPy array operations, re-locating them to logical days.
- **No Artificial Time Allocations**: Lessons are organized strictly by **Day 1 through Day 20**.

---

## 4. DETAILED 20-DAY CURRICULUM PLAN

---

### Day 1 — Python & Git Foundations: Setup, Environment & Syntax
- **Learning Objectives**: Understand Python execution, install VS Code & Python 3.x, write Python scripts, initialize Git repository.
- **Topics Covered**: Interpreter vs `.py` script, basic syntax (`print()`, comments), Git intro, `git config`, `git init`.
- **Theory**: Python executes sequentially via an interpreter. Git tracks file changes over time using commit snapshots.
- **Practical Coding**:
  ```python
  print("Welcome to Python + Git Zero-to-Hero!")
  print("Learning Python syntax and version control.")
  ```
- **Git/GitHub Practice**:
  ```bash
  git config --global user.name "Your Name"
  git config --global user.email "your.email@example.com"
  git init
  ```
- **Mini Task**: Create `day1_intro.py`, print your name and learning goal, run via terminal, check `git status`.
- **Expected Outcome**: Student can run Python scripts from terminal and initialize local Git repos.

---

### Day 2 — Variables, Data Types, Type Conversion & Git Staging
- **Learning Objectives**: Master variables, dynamic typing, type casting (`int()`, `float()`, `str()`, `bool()`), and Git 3-stage architecture.
- **Topics Covered**: Variable naming rules, `type()`, scalar types (`int`, `float`, `str`, `bool`, `complex`), type casting, `input()`, Git 3-stage model (Working Tree $\rightarrow$ Staging $\rightarrow$ Repo).
- **Theory**: Variables are dynamically typed memory references. Git isolates unstaged changes from staged commits.
- **Practical Coding**:
  ```python
  name = input("Enter your name: ")
  age = int(input("Enter your age: "))
  height = float(input("Enter your height (m): "))
  print(f"User: {name} (Age: {age}), Height: {height}m")
  ```
- **Git/GitHub Practice**:
  ```bash
  git status
  git add day1_intro.py day2_variables.py
  git commit -m "feat: add variable assignment and type conversion exercises"
  ```
- **Mini Task**: Build `user_calculator.py`, convert user inputs to floats, display sum, commit with descriptive message.
- **Expected Outcome**: Student handles user input, dynamic types, type casting, and structured Git commits.

---

### Day 3 — Operators, Strings, String Methods & Git Logs
- **Learning Objectives**: Master arithmetic/comparison/logical operators, string slicing, string methods, `git log`, and `git diff`.
- **Topics Covered**: Arithmetic (`+`, `-`, `*`, `/`, `//`, `%`, `**`), comparison/logical ops, string immutability, slicing `[start:stop:step]`, methods (`upper`, `lower`, `strip`, `title`, `replace`, `split`, `join`), f-strings, `git log`, `git diff`.
- **Theory**: Strings are immutable sequences. `git diff` shows modifications between working tree and index.
- **Practical Coding**:
  ```python
  phrase = "  Python Programming is Awesome!  "
  clean_phrase = phrase.strip()
  print("Reversed:", clean_phrase[::-1])
  print("Replaced:", clean_phrase.replace("Awesome", "Powerful"))
  words = clean_phrase.split()
  print("Joined:", "-".join(words))
  ```
- **Git/GitHub Practice**:
  ```bash
  git diff
  git log --oneline --graph --all
  ```
- **Mini Task**: Create `string_analyzer.py` to count words, reverse strings, display formatted output, and commit.
- **Expected Outcome**: Student manipulates strings fluently and navigates Git history logs.

---

### Day 4 — Conditional Logic, Decision Making & Git Branching Basics
- **Learning Objectives**: Control program flow with `if`/`elif`/`else`, nested logic, and create Git feature branches.
- **Topics Covered**: Truthy/falsy values, `if`/`elif`/`else`, nested conditions, logical chaining (`and`/`or`/`not`), PEP 8 indentation, `git branch`, `git switch`.
- **Theory**: Conditional branching directs code execution based on boolean evaluation. Git branches isolate new feature development.
- **Practical Coding**:
  ```python
  score = float(input("Enter exam score (0-100): "))
  if score >= 90: grade = "A"
  elif score >= 80: grade = "B"
  elif score >= 70: grade = "C"
  elif score >= 60: grade = "D"
  else: grade = "F"
  print(f"Final Grade: {grade}")
  ```
- **Git/GitHub Practice**:
  ```bash
  git branch
  git switch -c feature/conditionals
  ```
- **Mini Task**: Create `grading_system.py` on branch `feature/conditionals`, write distinction rules, and commit.
- **Expected Outcome**: Student builds conditional structures and uses isolated Git feature branches.

---

### Day 5 — Loops, Iteration Control & Connecting Local Git to GitHub
- **Learning Objectives**: Master `for` loops, `while` loops, `range()`, `break`, `continue`, and push code to GitHub.
- **Topics Covered**: `range()`, `for` and `while` loops, `break`, `continue`, `pass`, GitHub remote setup (`git remote add`, `git push -u origin main`).
- **Theory**: Loops repeat execution until exit conditions are met. GitHub hosts remote repositories for backup and collaboration.
- **Practical Coding**:
  ```python
  for num in range(1, 21):
      if num % 2 != 0: continue
      if num > 16: break
      print(num, end=" ")
  print("\nLoop finished.")
  ```
- **Git/GitHub Practice**:
  ```bash
  git remote add origin https://github.com/username/python-git-zero-to-hero.git
  git branch -M main
  git push -u origin main
  ```
- **Mini Task & Project 1**: Complete **Project 1** (Interactive CLI Calculator & Profile Tool), push to GitHub repository.
- **Expected Outcome**: Student writes iterative loops and syncs local Git repositories with remote GitHub repositories.

---

### Day 6 — Lists, Tuples & Basic Repository Management
- **Learning Objectives**: Master sequence types (`list` vs `tuple`), custom sorting, tuple unpacking, `git fetch`, and `git pull`.
- **Topics Covered**: Lists (`[]`), mutability, `.append()`, `.insert()`, `.remove()`, `.pop()`, `.sort()`, custom sorting (`key=func`), Tuples (`()`), immutability, unpacking, nested indexing, `git fetch`, `git pull`.
- **Theory**: Lists are mutable; tuples are fixed at creation. `git fetch` retrieves remote changes without merging; `git pull` fetches and merges.
- **Practical Coding**:
  ```python
  def distance_from_fifty(n): return abs(n - 50)
  numbers = [100, 50, 65, 82, 23]
  numbers.sort(key=distance_from_fifty)
  print("Sorted by proximity to 50:", numbers)

  coordinates = (27.7172, 85.3240, 1400)
  lat, lon, elevation = coordinates
  print(f"Lat: {lat}, Lon: {lon}, Elev: {elevation}m")
  ```
- **Git/GitHub Practice**:
  ```bash
  git fetch origin
  git pull origin main
  ```
- **Mini Task**: Create `student_roster.py` sorting student tuples `(name, score)` by score, commit, and push.
- **Expected Outcome**: Student manages lists/tuples with custom sorting and pulls remote GitHub updates.

---

### Day 7 — Sets, Dictionaries & Nested Data Structures
- **Learning Objectives**: Work with unique sets, key-value dictionaries, nested collections, and Git feature branches.
- **Topics Covered**: Sets (`{}`), uniqueness, set algebra (`union`, `intersection`), Dictionaries (`{k: v}`), `.keys()`, `.values()`, `.items()`, `.get()`, nested structures (`dict` of `dicts`).
- **Theory**: Sets provide unique $O(1)$ lookups. Dictionaries map unique keys to values.
- **Practical Coding**:
  ```python
  unique_tags = {"python", "git", "vscode"}
  unique_tags.add("developer")

  student_db = {
      "EMP01": {"name": "Alice", "skills": ["Python", "Git"]},
      "EMP02": {"name": "Bob", "skills": ["SQL", "Excel"]}
  }
  print(student_db["EMP01"]["skills"][0])
  ```
- **Git/GitHub Practice**:
  ```bash
  git switch -c feature/data-structures
  git add day7_dict_sets.py
  git commit -m "feat: implement set operations and dictionary lookups"
  ```
- **Mini Task**: Build `inventory_manager.py` using nested dictionaries to track item stock and price. Commit changes.
- **Expected Outcome**: Student constructs and queries sets, dictionaries, and nested data structures.

---

### Day 8 — Comprehensions, Performance Benchmarking & GitHub Collaboration
- **Learning Objectives**: Write list/dict comprehensions, benchmark list vs tuple memory/speed, configure `.gitignore` and `README.md`.
- **Topics Covered**: List/Dict comprehensions, performance benchmarking (`sys.getsizeof()`, `time.time()`), styled `README.md`, `.gitignore` configuration (`__pycache__/`, `.venv/`).
- **Theory**: Comprehensions offer concise sequence creation. `.gitignore` prevents dynamic build and secret files from being committed.
- **Practical Coding**:
  ```python
  import sys, time
  sample_size = 1_000_000
  list_data = list(range(sample_size))
  tuple_data = tuple(range(sample_size))
  print(f"List Size: {sys.getsizeof(list_data)} bytes | Tuple Size: {sys.getsizeof(tuple_data)} bytes")

  squares_dict = {x: x**2 for x in range(1, 11) if x % 2 == 0}
  print("Even Squares Dict:", squares_dict)
  ```
- **Git/GitHub Practice**:
  ```bash
  echo "__pycache__/" > .gitignore
  echo ".venv/" >> .gitignore
  git add .gitignore README.md
  git commit -m "docs: add repository README and configure .gitignore"
  git push origin feature/data-structures
  ```
- **Mini Task**: Write a styled `README.md`, record memory benchmark observations, commit, and push.
- **Expected Outcome**: Student writes pythonic comprehensions, benchmarks memory usage, and configures repo documentation.

---

### Day 9 — Functions, Parameters, Return Values & Git Stash
- **Learning Objectives**: Write modular functions (`def`), default arguments, return values, and manage temporary changes with `git stash`.
- **Topics Covered**: `def` syntax, positional vs keyword arguments, return values, default parameters, scope (`global`), `git stash`, `git stash pop`.
- **Theory**: Functions promote DRY code modularity. `git stash` shelves uncommitted working directory changes temporarily.
- **Practical Coding**:
  ```python
  def calculate_metrics(numbers: list, scale_factor: float = 1.0):
      if not numbers: return 0, 0.0
      scaled = [n * scale_factor for n in numbers]
      return sum(scaled), sum(scaled) / len(scaled)

  total, avg = calculate_metrics([10, 20, 30, 40], scale_factor=1.5)
  print(f"Scaled Total: {total}, Scaled Avg: {avg}")
  ```
- **Git/GitHub Practice**:
  ```bash
  git stash
  git stash list
  git stash pop
  ```
- **Mini Task**: Write `geometry_helper.py` with area/perimeter functions, test `git stash` while switching branches, and pop.
- **Expected Outcome**: Student writes modular functions with defaults and handles uncommitted code with `git stash`.

---

### Day 10 — Advanced Functions (*args, **kwargs, Lambdas) & Merging Branches
- **Learning Objectives**: Master `*args`, `**kwargs`, lambda functions, `map()`, `filter()`, and branch merging (`git merge`).
- **Topics Covered**: `*args` (tuple packing), `**kwargs` (dict packing), lambda expressions, `map()`, `filter()`, `git merge`, `git branch -d`.
- **Theory**: `*args`/`**kwargs` allow dynamic function parameters. Merging incorporates feature branch commits into `main`.
- **Practical Coding**:
  ```python
  def generate_user_report(title, *scores, **details):
      print(f"=== {title.upper()} ===")
      for k, v in details.items(): print(f"{k.title()}: {v}")
      if scores: print(f"Average: {sum(scores)/len(scores):.2f}")

  generate_user_report("Audit", 88, 92, 79, name="Alice", role="Engineer")
  evens = list(filter(lambda x: x % 2 == 0, range(1, 11)))
  print("Evens:", evens)
  ```
- **Git/GitHub Practice**:
  ```bash
  git switch main
  git merge feature/data-structures
  git branch -d feature/data-structures
  git push origin main
  ```
- **Mini Task**: Create `flexible_logger.py` with `*args` and `**kwargs`, merge feature branch into `main`, and push.
- **Expected Outcome**: Student understands dynamic parameters, lambdas, and complete Git branch merge workflows.

---

### Day 11 — Modules, Packages, Virtual Environments & Conflict Prevention
- **Learning Objectives**: Build custom modules, package structures, manage `.venv` with `pip`, and prevent merge conflicts.
- **Topics Covered**: Module imports, `__init__.py`, `if __name__ == '__main__':`, virtual environments (`python -m venv`), `requirements.txt`, merge conflict prevention.
- **Theory**: Virtual environments isolate library dependencies. Entry guards prevent test code execution upon importing modules.
- **Practical Coding**:
  ```python
  # File: math_utils.py
  def add(a, b): return a + b
  def multiply(a, b): return a * b

  if __name__ == "__main__":
      assert add(2, 3) == 5
      print("Module self-test passed!")
  ```
- **Git/GitHub Practice**:
  ```bash
  python -m venv .venv
  # Windows: .venv\Scripts\activate
  pip install requests
  pip freeze > requirements.txt
  ```
- **Mini Task**: Scaffold custom module `string_helpers.py` and `app.py`, configure `.venv`, export `requirements.txt`, and commit.
- **Expected Outcome**: Student creates custom modules, manages virtual environments, and exports dependency manifests.

---

### Day 12 — File Handling (TXT, CSV, JSON) & Git Reset Safety
- **Learning Objectives**: Read/write TXT, CSV, and JSON files using context managers (`with`), and practice safe Git recovery (`restore`, `revert`, `reset`).
- **Topics Covered**: File modes (`'r'`, `'w'`, `'a'`), `with` statement, `csv.reader`/`writer`, `json.dump`/`load`, `git restore`, `git revert`, `git reset`.
- **Theory**: Context managers guarantee file handles close automatically. `git revert` safely undoes history by adding a new commit.
- **Practical Coding**:
  ```python
  import csv, json
  user_data = [{"id": 1, "name": "alice"}, {"id": 2, "name": "bob"}]

  with open("users.json", "w") as f: json.dump(user_data, f, indent=4)
  with open("users.json", "r") as f: loaded = json.load(f)

  with open("users.csv", "w", newline="") as f:
      writer = csv.DictWriter(f, fieldnames=["id", "name"])
      writer.writeheader()
      writer.writerows(loaded)
  ```
- **Git/GitHub Practice**:
  ```bash
  git restore users.json
  git revert HEAD
  ```
- **Mini Task**: Write `data_converter.py` reading JSON and writing a CSV report, commit, and test `git restore`.
- **Expected Outcome**: Student safely manipulates CSV/JSON files using context managers and recovers files safely in Git.

---

### Day 13 — Exception Handling & Resolving Merge Conflicts
- **Learning Objectives**: Handle runtime exceptions (`try`/`except`/`finally`), raise custom errors, and resolve Git merge conflicts manually.
- **Topics Covered**: `try`, `except Exception as e`, `else`, `finally`, `raise`, Git merge conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`).
- **Theory**: Exception handling prevents crashes. Merge conflicts happen when concurrent commits edit identical lines differently.
- **Practical Coding**:
  ```python
  def load_config(path):
      try:
          with open(path, "r") as f: return json.load(f)
      except FileNotFoundError:
          print(f"[ERROR] '{path}' not found.")
      except json.JSONDecodeError as e:
          print(f"[ERROR] Invalid JSON: {e}")
      finally:
          print("[LOG] Operation complete.")
      return None
  ```
- **Git/GitHub Practice**:
  ```bash
  # Resolve conflict markers manually in editor, then:
  git add resolved_file.py
  git commit -m "fix: resolve merge conflict between branches"
  ```
- **Mini Task & Project 2**: Complete **Project 2** (Automated File Data Processor with Exception Logging) and resolve a simulated merge conflict.
- **Expected Outcome**: Student builds exception-resistant file scripts and resolves Git merge conflicts cleanly.

---

### Day 14 — Object-Oriented Programming: Classes, Objects & Git Tagging
- **Learning Objectives**: Master OOP concepts, class creation, `__init__()` constructors, instance/class attributes, and Git release tags.
- **Topics Covered**: Classes vs Objects, `__init__()`, `self`, instance vs class attributes, `__str__()`, Git annotated tags (`git tag -a`).
- **Theory**: OOP encapsulates data and behavior into objects. Git tags mark release milestones (`v1.0`).
- **Practical Coding**:
  ```python
  class Student:
      school_name = "Python Academy"
      def __init__(self, student_id: str, name: str, gpa: float):
          self.student_id = student_id
          self.name = name
          self.gpa = gpa
      def update_gpa(self, new_gpa: float):
          if 0.0 <= new_gpa <= 4.0: self.gpa = new_gpa
          else: raise ValueError("Invalid GPA")
      def __str__(self):
          return f"Student({self.student_id}): {self.name} | GPA: {self.gpa:.2f}"

  s1 = Student("STU101", "Alice", 3.8)
  s1.update_gpa(3.95)
  print(s1)
  ```
- **Git/GitHub Practice**:
  ```bash
  git tag -a v1.0 -m "Release Version 1.0 - Completed Core Python & Data File Processor"
  git push origin --tags
  ```
- **Mini Task**: Create `bank_account.py` with `deposit()` and `withdraw()` methods, commit, and tag release `v1.1`.
- **Expected Outcome**: Student creates custom classes, manages instance state, and tags Git releases.

---

### Day 15 — Advanced OOP & GitHub Pull Request Workflows
- **Learning Objectives**: Implement Inheritance, Encapsulation, Polymorphism, method overriding (`super()`), and GitHub Pull Requests.
- **Topics Covered**: Encapsulation (`public`, `_protected`, `__private`), Inheritance, `super().__init__()`, method overriding, GitHub PR workflow.
- **Theory**: Inheritance promotes reuse. Encapsulation protects internal object state. PRs allow code review before merging to `main`.
- **Practical Coding**:
  ```python
  class BankUser:
      def __init__(self, name: str, user_id: str):
          self.name = name
          self.user_id = user_id
          self.__pin = "1234"
      def verify_pin(self, pin_input: str) -> bool:
          return self.__pin == pin_input

  class PremiumUser(BankUser):
      def __init__(self, name: str, user_id: str, points: int):
          super().__init__(name, user_id)
          self.points = points
      def display(self):
          print(f"Premium User: {self.name} | Points: {self.points}")

  u = PremiumUser("Alice", "U99", 500)
  u.display()
  print("PIN Valid:", u.verify_pin("1234"))
  ```
- **Git/GitHub Practice**:
  ```bash
  git switch -c feature/oop-refactor
  git add bank_system.py
  git commit -m "refactor: implement OOP inheritance and encapsulation"
  git push -u origin feature/oop-refactor
  # (Open Pull Request on GitHub)
  ```
- **Mini Task**: Build `shape_calculator.py` with base `Shape` class and derived `Rectangle`/`Circle` overriding `area()`. Submit PR on GitHub.
- **Expected Outcome**: Student implements OOP inheritance/encapsulation and executes GitHub Pull Request workflows.

---

### Day 16 — Advanced Python: Iterators, Generators, Decorators & GitHub Issues
- **Learning Objectives**: Build generators (`yield`), function decorators (`@decorator`), and link Git commits to GitHub Issues.
- **Topics Covered**: Iterators (`iter()`, `next()`), Generators (`yield`), Decorators (`@wrapper`), GitHub Issue linking (`Fixes #12`).
- **Theory**: Generators evaluate lazily to save memory. Decorators dynamically wrap and extend function behaviors.
- **Practical Coding**:
  ```python
  import time

  def large_range_gen(limit):
      curr = 0
      while curr < limit:
          yield curr
          curr += 1

  def execution_timer(func):
      def wrapper(*args, **kwargs):
          t0 = time.time()
          res = func(*args, **kwargs)
          print(f"[TIMER] {func.__name__} took {time.time()-t0:.6f}s")
          return res
      return wrapper

  @execution_timer
  def process():
      return sum(large_range_gen(500_000))

  print("Sum:", process())
  ```
- **Git/GitHub Practice**:
  ```bash
  git commit -m "feat: add memory-efficient generator (Fixes #4)"
  git push origin main
  ```
- **Mini Task**: Create `decorator_logger.py` logging arguments and outputs of functions, link commit to a GitHub Issue.
- **Expected Outcome**: Student writes lazy generators, custom decorators, and manages GitHub Issues.

---

### Day 17 — Standard Library, Context Managers & Advanced Git Operations
- **Learning Objectives**: Use `pathlib`, `datetime`, custom Context Managers (`@contextmanager`), `git rebase`, and `git cherry-pick`.
- **Topics Covered**: Standard library (`pathlib.Path`, `datetime`), Context Managers (`__enter__`/`__exit__`, `@contextmanager`), `git rebase`, `git cherry-pick`.
- **Theory**: Context managers handle resource cleanup automatically. Rebase rewrites history to create linear commit logs.
- **Practical Coding**:
  ```python
  from pathlib import Path
  from datetime import datetime
  from contextlib import contextmanager

  @contextmanager
  def activity_logger(action):
      print(f"[{datetime.now().strftime('%H:%M:%S')}] START: {action}")
      try: yield
      finally: print(f"[{datetime.now().strftime('%H:%M:%S')}] END: {action}")

  with activity_logger("Scanning Workspace"):
      for p in Path(".").glob("*.py"):
          print(f" - {p.name} ({p.stat().st_size} bytes)")
  ```
- **Git/GitHub Practice**:
  ```bash
  git cherry-pick <commit-hash>
  ```
- **Mini Task**: Write `log_cleaner.py` using `pathlib` and `@contextmanager`, commit, and practice cherry-picking commits.
- **Expected Outcome**: Student uses standard library tools, writes custom context managers, and understands advanced Git operations.

---

### Day 18 — Numerical Computing with NumPy & Advanced Data Analytics
- **Learning Objectives**: Master NumPy arrays, vectorization, reshaping, boolean masking, linear algebra, and binary `.npy` file I/O.
- **Topics Covered**: `np.ndarray`, `arange()`, `linspace()`, `reshape()`, broadcasting, boolean masking (`arr[arr > 50]`), `@`/`matmul`, `det`, `np.save`/`load`.
- **Theory**: NumPy arrays store contiguous C-memory blocks for fast vectorized operations. Broadcasting aligns mismatched array shapes.
- **Practical Coding**:
  ```python
  import numpy as np

  matrix = np.array([[10, 20, 30], [40, 50, 60]])
  row_vector = np.array([1, 2, 3])
  print("Broadcasted Add:\n", matrix + row_vector)

  data = np.random.randint(1, 100, size=15)
  print("Masked (> 50):", data[data > 50])

  sq = np.array([[2, 1], [1, 4]])
  print("Determinant:", np.linalg.det(sq))

  np.save("cache.npy", matrix)
  print("Loaded Cache Shape:", np.load("cache.npy").shape)
  ```
- **Git/GitHub Practice**:
  ```bash
  echo "*.npy" >> .gitignore
  git add day18_numpy_analytics.py .gitignore
  git commit -m "feat: integrate NumPy analytics engine and ignore binary cache"
  ```
- **Mini Task & Project 3**: Complete **Project 3** (OOP Inventory System + NumPy Analytics Engine), tag `v2.0`, and push.
- **Expected Outcome**: Student executes vectorized array computations, boolean masking, matrix math, and binary array I/O.

---

### Day 19 — Portfolio Project Architecture, Packaging & Production Workflows
- **Learning Objectives**: Scaffold a multi-module production Python project, write `setup.py`, and configure repository documentation.
- **Topics Covered**: Project directory layout (`src/`, `tests/`, `data/`), entry points (`main.py`), `setup.py`, documentation standards.
- **Project Structure**:
  ```text
  paams_app/
  │── .gitignore
  │── README.md
  │── requirements.txt
  ├── data/
  ├── src/
  │   ├── __init__.py
  │   ├── models/
  │   ├── services/
  │   └── utils/
  └── main.py
  ```
- **Git/GitHub Practice**:
  ```bash
  git switch -c feature/portfolio-setup
  git add .
  git commit -m "chore: scaffold multi-module portfolio project architecture"
  git push -u origin feature/portfolio-setup
  ```
- **Mini Task**: Scaffold capstone project files, write a detailed project plan in `README.md`, configure `requirements.txt`, and commit.
- **Expected Outcome**: Student scaffolds a production-ready modular Python application architecture.

---

### Day 20 — Portfolio Project Completion, Defense & Professional Git Release
- **Learning Objectives**: Complete, test, and present the Capstone Project, merge to `main`, tag `v3.0-final`, and publish a GitHub Release.
- **Topics Covered**: Project testing, refactoring, code review, merging feature branches, official GitHub Releases, project defense.
- **Practical Execution**: Complete implementation of the Personal Asset & Analytics Management System (PAAMS CLI), verify exception handling, file parsing, and NumPy analytics engine.
- **Git/GitHub Practice**:
  ```bash
  git switch main
  git merge feature/portfolio-setup
  git tag -a v3.0 -m "Release v3.0: Final Capstone Portfolio Application Complete"
  git push origin main --tags
  ```
- **Final Deliverable**: Publish live GitHub project repository containing 20-day commit history, styled `README.md`, tagged releases, and runnable Python code.
- **Expected Outcome**: Student graduates with a production-ready portfolio project hosted on GitHub as a practical Python developer.

---

## 5. PROGRESSIVE PROJECTS OVERVIEW

1. **Project 1 (End of Day 5)**: Interactive CLI Calculator & User Profile Tool (Variables, logic, loops, basic remote push).
2. **Project 2 (End of Day 13)**: Automated Data File Processor & Report Generator (Functions, CSV/JSON, exceptions, merge conflict resolution).
3. **Project 3 (End of Day 18)**: OOP Inventory & NumPy Analytics Engine (Classes, inheritance, encapsulation, NumPy array math, binary `.npy` cache).
4. **Final Capstone (End of Day 20)**: Personal Asset & Analytics Management System (PAAMS CLI) (Multi-module package, OOP models, file services, NumPy engine, custom decorators, exceptions, complete GitHub history & tagged release).

---

## 6. GIT / GITHUB COMMAND PROGRESSION TABLE

| Phase | Day Introduced | Command | Practical Classroom Context | Safety / Best Practice Rules |
| :--- | :--- | :--- | :--- | :--- |
| **Setup & Init** | Day 1 | `git config` | Set global user name and email | Run once per user machine. |
| **Setup & Init** | Day 1 | `git init` | Initialize local Git repository | Run once in project root folder. |
| **Basic Workflow**| Day 2 | `git status` | Check untracked and staged files | Run before/after staging and committing. |
| **Basic Workflow**| Day 2 | `git add` | Stage modified files | Stage specific files or `.`. |
| **Basic Workflow**| Day 2 | `git commit` | Save snapshot to repository history | Use clear imperative messages. |
| **History** | Day 3 | `git log` | Review repository commit timeline | Use `--oneline --graph` for readability. |
| **History** | Day 3 | `git diff` | Inspect unstaged vs staged changes | Review code changes before committing. |
| **Branching** | Day 4 | `git branch` | List, create, or delete branches | Avoid working directly on `main`. |
| **Branching** | Day 4 | `git switch` | Switch active working branches | `git switch -c` creates and switches. |
| **Remote Sync** | Day 5 | `git remote` | Connect local repo to GitHub | Alias default remote host as `origin`. |
| **Remote Sync** | Day 5 | `git push` | Upload local commits to remote | Use `-u origin main` on initial push. |
| **Remote Sync** | Day 6 | `git pull` | Fetch and merge remote updates | Pull remote updates before starting work. |
| **Workspace** | Day 9 | `git stash` | Shelve uncommitted working edits | Use `stash pop` to restore shelved edits. |
| **Merging** | Day 10 | `git merge` | Integrate feature branch to `main` | Merge into target branch after testing. |
| **Undo Safety** | Day 12 | `git restore` | Discard uncommitted working edits | Restores working files to last commit. |
| **Undo Safety** | Day 12 | `git revert` | Create new commit reversing a past commit | **Safe for public history**: Non-destructive. |
| **Undo Safety** | Day 12 | `git reset` | Move branch tip back in history | **Warning**: Avoid `--hard` on uncommitted edits. |
| **Releases** | Day 14 | `git tag` | Mark release milestones (`v1.0`) | Push tags using `git push origin --tags`. |
| **Advanced** | Day 17 | `git rebase` | Re-apply commits onto new base | **Caution**: Only rebase unpushed commits! |
| **Advanced** | Day 17 | `git cherry-pick` | Apply specific commit from branch | Use to port specific bug fixes. |

---

## 7. 20-DAY CURRICULUM SUMMARY TABLE

| Day | Main Python Topic | Git / GitHub Topic | Practical Classroom Work | Project / Outcome Milestone |
| :---: | :--- | :--- | :--- | :--- |
| **1** | Setup, Interpreter, Syntax, Comments | Git Intro, `git config`, `git init` | Install VS Code, run script, init Git repo | Running Python & Git setup |
| **2** | Variables, Data Types, Casting, I/O | 3-Stage Architecture, `add`, `commit` | User input, type casting, stage & commit | `user_calculator.py` committed |
| **3** | Operators, Strings, Slicing, Methods | `git status`, `git log`, `git diff` | Text transformation, slicing reversal | `string_analyzer.py` tracked |
| **4** | Control Flow: `if`, `elif`, `else`, Logic | Branching Basics, `git branch`, `switch` | Build grading logic system in branch | Branch `feature/conditionals` |
| **5** | Loops: `for`, `while`, `range`, `break` | Remote Repos, `git remote`, `git push` | Iterative logic, link repo to GitHub | **PROJECT 1**: CLI Tool on GitHub |
| **6** | Lists, Tuples, Methods, Custom Sort | Remote Syncing, `git fetch`, `git pull` | Custom tuple sorting, pull remote updates | Custom list sorting & sync |
| **7** | Sets, Dictionaries, Nested Structures | Branch Isolation, `feature/data-structs` | Nested dict store, set operations | `inventory_manager.py` branch |
| **8** | Comprehensions, Performance Benchmark | Repository Docs, `README.md`, `.gitignore` | Memory benchmark, list/dict comprehensions | `.gitignore` & `README.md` |
| **9** | Functions: `def`, Parameters, Returns | Workspace Management, `git stash` | Modular functions, stash temporary work | Modular helper scripts |
| **10** | `*args`, `**kwargs`, Lambda, `map`/`filter` | Branch Merging, `git merge`, `branch -d` | Dynamic logger, merge feature branch | Merged branch & clean repo |
| **11** | Modules, Packages, `venv`, `pip` | Pre-merge Conflict Prevention | Package scaffold, `.venv`, `requirements.txt` | Virtual Env & package |
| **12** | File I/O: TXT, CSV, JSON, Context Manager| Recovery Safety, `restore`, `revert`, `reset`| CSV/JSON file parsing, test `git restore` | Safe file I/O & undo |
| **13** | Exception Handling: `try`/`except`/`finally`| Merge Conflict Resolution | Catch exceptions, resolve merge markers | **PROJECT 2**: File Processor |
| **14** | OOP Basics: Classes, Objects, `__init__` | Version Tagging, `git tag -a` | Define domain classes, tag `v1.0` release | Tagged `v1.0` on GitHub |
| **15** | Advanced OOP: Inheritance, Encapsulation | GitHub Pull Requests & Code Review | Derived classes, `super()`, open PR | Feature PR merged on GitHub |
| **16** | Generators (`yield`), Decorators | Issue Tracking, linking `#issue_id` | Memory generators, timing decorators | Decorators & Issue tracking |
| **17** | Standard Library, Context Managers | Advanced Git: `rebase`, `cherry-pick` | `pathlib`/`datetime`, `@contextmanager` | Advanced Git & stdlib |
| **18** | NumPy Arrays, Vectorization, Indexing | Binary File Ignore (`*.npy`) | Vector math, boolean mask, `.npy` I/O | **PROJECT 3**: OOP + NumPy |
| **19** | Portfolio Architecture, Package Layout | Branch Scaffolding for Portfolio | Scaffold capstone architecture, `setup.py` | Capstone Architecture |
| **20** | Capstone Completion, Optimization | Final Release Tagging (`v3.0`), Release | Finalize app, code review, release | **CAPSTONE**: Live Portfolio |

---

## 8. FINAL STUDENT OUTCOME MATRIX

- **Before Day 1**: Complete beginner, no environment, manual file backups.
- **After Day 5**: **Python Beginner & Git User** — Handles input/output, control flow, loops, and remote GitHub pushes.
- **After Day 10**: **Python Foundation & Git Contributor** — Constructs data structures, comprehensions, modular functions with `*args`/`**kwargs`, feature branches, and stashing.
- **After Day 15**: **Intermediate Python & GitHub Professional** — Creates custom packages, virtual environments, CSV/JSON file handlers, OOP models with inheritance/encapsulation, Pull Requests, and release tags.
- **After Day 20**: **Practical Python Developer & GitHub Portfolio Creator** — Builds memory-efficient generators, decorators, NumPy data analytics engines, multi-module applications, and maintains a production-grade portfolio repository on GitHub.
