# Python + Git Class

This repository is a hands-on Python and Git learning workspace for beginners. It includes daily lesson notes, Jupyter notebooks, small practice projects, and supporting documentation.

## What is inside

- [class](class) — daily lessons and notebooks from Day 1 to Day 20
- [docs](docs) — extra notes and learning reports
- [notebooks](notebooks) — additional notebook practice files
- [projects](projects) — small practical projects such as the Nepal weather CLI and the QR generator
- [requirements.txt](requirements.txt) — Python dependencies for the workspace
- [test.py](test.py) — quick local testing script

## Daily lesson files

These links open the lesson notes and notebooks for each day of the course.

- Day 1: [Markdown](class/day1.md) | [Notebook](class/day1.ipynb)
- Day 2: [Markdown](class/day2.md) | [Notebook](class/day2.ipynb)
- Day 3: [Markdown](class/day3.md) | [Notebook](class/day3.ipynb)
- Day 4: [Markdown](class/day4.md) | [Notebook](class/day4.ipynb)
- Day 5: [Markdown](class/day5.md) | [Notebook](class/day5.ipynb)
- Day 6: [Markdown](class/day6.md) | [Notebook](class/day6.ipynb)
- Day 7: [Markdown](class/day7.md) | [Notebook](class/day7.ipynb)
- Day 8: [Markdown](class/day8.md) | [Notebook](class/day8.ipynb)
- Day 9: [Markdown](class/day9.md) | [Notebook](class/day9.ipynb)
- Day 10: [Markdown](class/day10.md) | [Notebook](class/day10.ipynb)
- Day 11: [Markdown](class/day11.md) | [Notebook](class/day11.ipynb)
- Day 12: [Markdown](class/day12.md) | [Notebook](class/day12.ipynb)
- Day 13: [Markdown](class/day13.md) | [Notebook](class/day13.ipynb)
- Day 14: [Markdown](class/day14.md) | [Notebook](class/day14.ipynb)
- Day 15: [Markdown](class/day15.md) | [Notebook](class/day15.ipynb)
- Day 16: [Markdown](class/day16.md) | [Notebook](class/day16.ipynb)
- Day 17: [Markdown](class/day17.md) | [Notebook](class/day17.ipynb)
- Day 18: [Markdown](class/day18.md) | [Notebook](class/day18.ipynb)
- Day 19: [Markdown](class/day19.md) | [Notebook](class/day19.ipynb)
- Day 20: [Markdown](class/day20.md) | [Notebook](class/day20.ipynb)

## Curriculum map

This section gives a quick overview of the course flow from beginner Python topics to Git practices and milestone projects.

| Day | Python topic                                | Git / GitHub topic               | Deliverables                                                  |
| --- | ------------------------------------------- | -------------------------------- | ------------------------------------------------------------- |
| 01  | Python setup, interpreter, syntax, comments | git config, git init             | [day1.md](class/day1.md) · [day1.ipynb](class/day1.ipynb)     |
| 02  | Variables, data types, casting, input()     | 3-stage model (add, commit)      | [day2.md](class/day2.md) · [day2.ipynb](class/day2.ipynb)     |
| 03  | Operators, strings, slicing, methods        | git status, git log, git diff    | [day3.md](class/day3.md) · [day3.ipynb](class/day3.ipynb)     |
| 04  | Control flow, logic, if/elif/else           | Branching basics                 | [day4.md](class/day4.md) · [day4.ipynb](class/day4.ipynb)     |
| 05  | Loops and control statements                | Remote setup (git push)          | Project 1: CLI Tool                                           |
| 06  | Lists, tuples, custom sort keys             | Remote syncing (git pull)        | [day6.md](class/day6.md) · [day6.ipynb](class/day6.ipynb)     |
| 07  | Sets, dictionaries, nested structures       | Feature branch isolation         | [day7.md](class/day7.md) · [day7.ipynb](class/day7.ipynb)     |
| 08  | Comprehensions and memory basics            | .gitignore and repository docs   | [day8.md](class/day8.md) · [day8.ipynb](class/day8.ipynb)     |
| 09  | Functions, parameters, scope                | Workspace management (git stash) | [day9.md](class/day9.md) · [day9.ipynb](class/day9.ipynb)     |
| 10  | \*args, \*\*kwargs, lambdas, map/filter     | Branch merging                   | [day10.md](class/day10.md) · [day10.ipynb](class/day10.ipynb) |
| 11  | Modules and main guard                      | Virtual environments             | [day11.md](class/day11.md) · [day11.ipynb](class/day11.ipynb) |
| 12  | File I/O, CSV, JSON, context managers       | Recovery with restore and revert | [day12.md](class/day12.md) · [day12.ipynb](class/day12.ipynb) |
| 13  | Exception handling                          | Conflict resolution markers      | Project 2: File Processor                                     |
| 14  | OOP basics: classes and objects             | Version tagging                  | [day14.md](class/day14.md) · [day14.ipynb](class/day14.ipynb) |
| 15  | Advanced OOP: inheritance and encapsulation | GitHub pull request workflows    | [day15.md](class/day15.md) · [day15.ipynb](class/day15.ipynb) |
| 16  | Generators and decorators                   | Issue tracking                   | [day16.md](class/day16.md) · [day16.ipynb](class/day16.ipynb) |
| 17  | Standard library and pathlib                | Advanced Git (rebase)            | [day17.md](class/day17.md) · [day17.ipynb](class/day17.ipynb) |
| 18  | NumPy arrays, vectorization, indexing       | Binary file ignore               | Project 3: Analytics Engine                                   |
| 19  | Portfolio architecture and package layout   | Branch scaffolding               | [day19.md](class/day19.md) · [day19.ipynb](class/day19.ipynb) |
| 20  | Capstone completion and optimization        | Production release tag           | Final capstone: PAAMS CLI                                     |

## Key files

These links point to the most important files in the repository.

- [README.md](README.md)
- [LICENSE](LICENSE)
- [projects/nepal-weather/README.md](projects/nepal-weather/README.md)
- [projects/nepal-weather/main.py](projects/nepal-weather/main.py)
- [projects/qr_generator.py](projects/qr_generator.py)

## Quick start

1. Create a virtual environment

   ```bash
   python -m venv .venv
   ```

2. Activate it
   - Windows PowerShell:
     ```bash
     .venv\Scripts\Activate.ps1
     ```
   - Bash / macOS / Linux:
     ```bash
     source .venv/bin/activate
     ```

3. Install dependencies

   ```bash
   pip install -r requirements.txt
   ```

4. Open notebooks or run a project
   - Jupyter:
     ```bash
     jupyter notebook
     ```
   - QR generator example:
     ```bash
     python projects/qr_generator.py "https://example.com"
     ```

## Project highlights

- Daily Python lessons in [class](class)
- Practice notebooks in [notebooks](notebooks)
- A Nepal weather CLI in [projects/nepal-weather](projects/nepal-weather)
- A QR code generator in [projects/qr_generator.py](projects/qr_generator.py)

## License

This project is licensed under the MIT License.
