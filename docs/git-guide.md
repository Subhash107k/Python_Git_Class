# Git Command Reference

A practical reference for the Git commands covered throughout the Python + Git/GitHub class. Commands are organized progressively from basic repository management to collaboration and advanced history management.

---

## 1. Repository Setup

### `git init`

**Purpose:** Initializes a new local Git repository.

```bash
git init
```

**Example:**

```bash
mkdir my-project
cd my-project
git init
```

---

### `git clone`

**Purpose:** Creates a local copy of an existing remote repository.

```bash
git clone <repository-url>
```

**Example:**

```bash
git clone https://github.com/username/project.git
```

---

### `git remote`

**Purpose:** Manages connections to remote repositories.

```bash
git remote -v
```

**Add a remote:**

```bash
git remote add origin <repository-url>
```

---

## 2. Checking Repository Status

### `git status`

**Purpose:** Shows the current state of the working directory and staging area.

```bash
git status
```

Use this frequently before committing changes.

---

### `git log`

**Purpose:** Displays the commit history.

```bash
git log
```

**Compact history:**

```bash
git log --oneline
```

**Visual branch history:**

```bash
git log --oneline --graph --decorate --all
```

---

## 3. Tracking Changes

### `git add`

**Purpose:** Adds changes to the staging area.

Add a specific file:

```bash
git add README.md
```

Add multiple files:

```bash
git add file1.py file2.py
```

Add all changes:

```bash
git add .
```

---

### `git restore`

**Purpose:** Restores files and can remove changes from the working directory.

```bash
git restore <file>
```

**Example:**

```bash
git restore main.py
```

> ⚠️ This can discard uncommitted changes to the specified file.

---

### `git diff`

**Purpose:** Shows changes that have not yet been staged.

```bash
git diff
```

Compare staged changes:

```bash
git diff --staged
```

---

## 4. Creating Commits

### `git commit`

**Purpose:** Records staged changes in the repository history.

```bash
git commit -m "Initial commit"
```

A good commit message should describe what changed.

**Good:**

```bash
git commit -m "Add weather API integration"
```

**Avoid:**

```bash
git commit -m "changes"
```

---

### `git commit --amend`

**Purpose:** Modifies the most recent commit.

```bash
git commit --amend -m "Updated commit message"
```

Use carefully when the commit has already been pushed to a shared repository.

---

## 5. Branches

### `git branch`

**Purpose:** Lists, creates, or deletes branches.

List branches:

```bash
git branch
```

Create a branch:

```bash
git branch feature/weather-api
```

Delete a branch:

```bash
git branch -d feature/weather-api
```

---

### `git switch`

**Purpose:** Switches between branches or creates and switches to a new branch.

Switch branch:

```bash
git switch main
```

Create and switch:

```bash
git switch -c feature/weather-api
```

---

### `git checkout`

**Purpose:** Older command used for switching branches and restoring files.

```bash
git checkout main
```

Create and switch:

```bash
git checkout -b feature/test
```

> Modern Git generally recommends `git switch` and `git restore` for these operations because their purposes are clearer.

---

## 6. Working With Remote Repositories

### `git push`

**Purpose:** Uploads local commits to a remote repository.

```bash
git push origin main
```

First push of a new branch:

```bash
git push -u origin feature/weather-api
```

---

### `git pull`

**Purpose:** Fetches changes from a remote repository and integrates them into the current branch.

```bash
git pull
```

Explicit form:

```bash
git pull origin main
```

---

### `git fetch`

**Purpose:** Downloads remote changes without automatically merging them.

```bash
git fetch origin
```

This is useful when you want to inspect remote changes before integrating them.

---

## 7. Merging Branches

### `git merge`

**Purpose:** Combines changes from one branch into another.

First switch to the target branch:

```bash
git switch main
```

Then merge:

```bash
git merge feature/weather-api
```

If conflicts occur, resolve them manually and then:

```bash
git add .
git commit
```

---

## 8. Temporarily Saving Work

### `git stash`

**Purpose:** Temporarily stores uncommitted changes so you can work on something else.

```bash
git stash
```

List stashes:

```bash
git stash list
```

Restore the latest stash:

```bash
git stash pop
```

Apply a stash without removing it:

```bash
git stash apply
```

Delete a stash:

```bash
git stash drop
```

---

## 9. Removing Files From Git

### `git rm`

**Purpose:** Removes a tracked file from the working directory and staging area.

```bash
git rm old_file.py
```

---

### `git mv`

**Purpose:** Moves or renames a tracked file.

```bash
git mv old_name.py new_name.py
```

---

## 10. Tags and Releases

### `git tag`

**Purpose:** Creates labels for important points in repository history, commonly used for releases.

Create a tag:

```bash
git tag v1.0.0
```

List tags:

```bash
git tag
```

Create an annotated tag:

```bash
git tag -a v1.0.0 -m "First stable release"
```

Push a tag:

```bash
git push origin v1.0.0
```

Push all tags:

```bash
git push origin --tags
```

---

## 11. Undoing Changes

### `git reset`

**Purpose:** Moves the current branch pointer and can modify the staging area or working tree depending on the option used.

Unstage a file:

```bash
git reset HEAD <file>
```

Move back one commit while keeping changes staged:

```bash
git reset --soft HEAD~1
```

> ⚠️ Be careful with `git reset`, especially when working with commits that have already been pushed.

---

### `git revert`

**Purpose:** Creates a new commit that reverses the changes introduced by an earlier commit.

```bash
git revert <commit-hash>
```

For shared/public history, `git revert` is generally safer than rewriting history.

---

## 12. Inspecting Individual Commits

### `git show`

**Purpose:** Displays information and changes introduced by a commit.

```bash
git show <commit-hash>
```

Example:

```bash
git show a1b2c3d
```

---

### `git blame`

**Purpose:** Shows which commit and author last modified each line of a file.

```bash
git blame main.py
```

Useful for understanding the history of a particular section of code.

---

## 13. Rebase

### `git rebase`

**Purpose:** Reapplies commits on top of another base commit or branch.

Example:

```bash
git switch feature/weather-api
git rebase main
```

This can produce a cleaner, linear project history.

### Important Warning

> ⚠️ **Do not rebase commits that have already been shared with others unless you understand the consequences.** Rebase rewrites commit history.

For a private/local feature branch, rebasing can be useful before opening a pull request.

---

## 14. Cherry-Pick

### `git cherry-pick`

**Purpose:** Applies a specific commit from another branch to the current branch.

```bash
git cherry-pick <commit-hash>
```

Example:

```bash
git cherry-pick a1b2c3d
```

Useful when you need one particular fix without merging an entire branch.

---

## 15. Finding Commits

### `git reflog`

**Purpose:** Shows movements of `HEAD` and references, which can help recover commits after certain mistakes.

```bash
git reflog
```

This is especially useful when a commit appears to have disappeared after a reset or rebase.

---

## 16. Git Configuration

### `git config`

**Purpose:** Configures Git settings.

Set username:

```bash
git config --global user.name "Your Name"
```

Set email:

```bash
git config --global user.email "you@example.com"
```

View configuration:

```bash
git config --list
```

---

# Common Git Workflow

For normal daily development:

```bash
git status
git pull
```

Make your changes, then:

```bash
git status
git diff
git add .
git commit -m "Describe the changes"
git push
```

---

# Feature Branch Workflow

For a new feature:

```bash
git switch main
git pull

git switch -c feature/new-feature
```

Work on the feature:

```bash
git add .
git commit -m "Add new feature"
```

Push the branch:

```bash
git push -u origin feature/new-feature
```

After the feature is reviewed and merged:

```bash
git switch main
git pull
git branch -d feature/new-feature
```

---

# Useful Command Summary

| Command           | Purpose                           |
| ----------------- | --------------------------------- |
| `git init`        | Create a local repository         |
| `git clone`       | Copy a remote repository          |
| `git status`      | Check repository state            |
| `git add`         | Stage changes                     |
| `git commit`      | Save changes to history           |
| `git log`         | View commit history               |
| `git diff`        | View changes                      |
| `git branch`      | Manage branches                   |
| `git switch`      | Switch/create branches            |
| `git merge`       | Combine branches                  |
| `git fetch`       | Download remote changes           |
| `git pull`        | Fetch and integrate changes       |
| `git push`        | Upload commits                    |
| `git stash`       | Temporarily save changes          |
| `git restore`     | Restore files                     |
| `git reset`       | Move/reset repository state       |
| `git revert`      | Safely reverse a commit           |
| `git tag`         | Mark releases                     |
| `git show`        | Inspect a commit                  |
| `git blame`       | Track line history                |
| `git rebase`      | Reapply commits onto another base |
| `git cherry-pick` | Apply a specific commit           |
| `git reflog`      | Recover/inspect reference history |
| `git remote`      | Manage remote repositories        |
| `git rm`          | Remove tracked files              |
| `git mv`          | Move/rename tracked files         |
| `git config`      | Configure Git                     |

---

# Recommended Learning Order

Students should learn Git progressively:

```text
1. git init
2. git status
3. git add
4. git commit
5. git log
6. git diff
7. git clone
8. git remote
9. git push
10. git pull
11. git fetch
12. git branch
13. git switch
14. git merge
15. git stash
16. git restore
17. git reset
18. git revert
19. git tag
20. git show
21. git blame
22. git rebase
23. git cherry-pick
24. git reflog
```

This progression moves from **basic local Git → GitHub collaboration → branching → recovery → advanced history management**.
