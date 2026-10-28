# Git Gud 

A hands-on introduction to Git, GitHub, and Python for first-year engineering students. No prior experience needed. You'll go from your very first `git init` to opening pull requests, and from `print("hello")` to writing your own classes, one concept at a time.

## What is Git?

Git is a version control system. Think of it as an unlimited undo button for your entire project, with a full history of who changed what and when. GitHub is the website where you store your Git repositories online so you can back them up, share them, and work on them with other people.

Python is the language we'll use to practice all of this. It's beginner-friendly, widely used in engineering, and perfect for getting comfortable with programming fundamentals.

This workshop covers the foundations: how to track and manage your code with Git, how to collaborate with others on GitHub, and how to write clean Python from variables all the way to object-oriented programming.

## Folder Structure

```
git-gud-workshop/
├── module-1-git-fundamentals/     # Version control, Git/GitHub, setup, VS Code
├── module-2-repository-basics/    # Fork, clone, init, status, staging
├── module-3-workflow-branches/    # Commit, push, pull, branching
├── module-4-collaboration/        # Merging, PRs, conflicts, undoing changes
├── module-5-python-fundamentals/  # Variables, types, strings, conditionals, loops
│   ├── 1variables_datatypes.py
│   ├── 2strings.py
│   ├── 3conditionals.py
│   └── 4loops.py
├── module-6-python-collections/   # Collections, functions, recursion, files
│   ├── 1lists_tuples.py
│   ├── 2dictionaries_sets.py
│   ├── 3functions.py
│   ├── 4recursion.py
│   └── 5file_handling.py
├── module-7-python-oop/           # The four pillars of OOP
│   ├── 1abstraction.py
│   ├── 2encapsulation.py
│   ├── 3inheritance.py
│   └── 4polymorphism.py
├── arena/                            # Interactive Python arena (puzzles, tasks & testcases)
│   ├── basics/                       # Variables, I/O, conditionals, loops & boss challenge
│   ├── intermediate/                 # Collections, lambdas, handlers, OOP & boss challenge
│   ├── advanced/                     # NumPy, Pandas, Matplotlib, Scikit-learn & ML app boss
│   ├── miscellaneous/                # Algos, data structures, CP problems, ciphers, chatbot
│   └── assets/                       # Datasets, synthetic tests & dataset generator
├── SOLUTIONS/                        # Participant solution directories (<username>_solutions/)
├── my_dir_setup.py                   # Setup script to initialize your personal solutions space
├── CONTRIBUTORS.md                   # You'll add your name here in Module 4
├── CODE_OF_CONDUCT.md                # Be cool, have fun, don't panic
├── LICENSE                           # The "Have Fun & Don't Break Things" license
└── README.md
```

## Modules: What Each One Covers

| Module | Title | Topics Covered |
|--------|-------|----------------|
| 1 | Git Fundamentals & Setup | Version control, Git and GitHub introductions, Git setup, configuration, VS Code |
| 2 | Repository Basics | Forking, cloning, init, status, local vs. remote repositories, staging and `git add` |
| 3 | Git Workflow & Branches | Commit, push, pull, workflow, branches and branch commands |
| 4 | Git Collaboration | Merging, pull requests, merge conflicts, undoing changes, contributors and collaborators |
| 5 | Python Fundamentals | Variables, data types, strings, conditional statements and loops |
| 6 | Python Collections & Functions | Lists, tuples, dictionaries, sets, functions, recursion and file handling |
| 7 | Python OOP | Abstraction, encapsulation, inheritance and polymorphism |

### Module Breakdown

| Module | Concept | Description |
|--------|---------|-------------|
| 1 | Version Control | Why we track changes, and how Git saves snapshots of your work |
| 1 | Git vs. GitHub | Git is the tool on your laptop; GitHub is the home for your repos online |
| 1 | Setup and Config | Install Git, set your name and email, and get comfortable in VS Code |
| 2 | Fork and Clone | Make your own copy of a repo on GitHub, then bring it to your machine |
| 2 | Init and Status | Start a brand new repo and check what Git currently sees |
| 2 | Local vs. Remote | Your computer's copy versus the one on GitHub, and how they connect |
| 2 | Staging | Pick exactly which changes go into your next snapshot with `git add` |
| 3 | Commit, Push, Pull | Save a snapshot, send it to GitHub, and fetch what others have sent |
| 3 | Branches | Work on new ideas safely without touching the main code |
| 4 | Merging and PRs | Combine branches and propose changes through pull requests |
| 4 | Merge Conflicts | What to do when two people edit the same line |
| 4 | Undoing Changes | Take back mistakes with `restore`, `reset`, and `revert` |
| 4 | Contributors and Collaborators | Who can do what in a shared repo |
| 5 | Variables and Data Types | Store values and understand ints, floats, strings, and booleans |
| 5 | Strings | Slice, format, and manipulate text |
| 5 | Conditionals and Loops | Make decisions with `if` and repeat tasks with `for` and `while` |
| 6 | Lists, Tuples, Dicts, Sets | Python's built-in ways of grouping data |
| 6 | Functions and Recursion | Reusable blocks of code, including functions that call themselves |
| 6 | File Handling | Read from and write to files on disk |
| 7 | Abstraction and Encapsulation | Hide complexity and protect data inside classes |
| 7 | Inheritance and Polymorphism | Reuse code across classes and let different objects share one interface |

## Setup

> 📖 **Detailed Setup Documentation:**
> If you need a comprehensive, step-by-step walkthrough with screenshots and common troubleshooting, check out our [Workshop Setup Documentation (Google Docs)](https://docs.google.com/document/d/1nDuZn9sbfjJ4TPC2o8TRZJtEoPRuj-0ULh0H-9mH49g/edit?tab=t.abytm8ncm7d4#heading=h.66mk3vnumgty).

### 1. Create a GitHub account

Head to [github.com](https://github.com/) and sign up. Pick a username you won't be embarrassed to put on a resume.

### 2. Install Git

Check if you already have it:

```bash
git --version
```

Don't have it? Download from [git-scm.com](https://git-scm.com/downloads).

- **Windows:** Run the installer and keep the default options. This also gives you Git Bash.
- **Mac:** Run `git --version` in Terminal and it will offer to install for you, or use `brew install git`.
- **Linux:** `sudo apt install git` (Debian/Ubuntu) or `sudo dnf install git` (Fedora).

### 3. Configure Git

Tell Git who you are. This gets attached to every commit you make. Use the same email as your GitHub account.

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
git config --global init.defaultBranch main
```

Check that it worked:

```bash
git config --list
```

### 4. Install VS Code

Download from [code.visualstudio.com](https://code.visualstudio.com/). Once installed, add these extensions:

- **Python** (by Microsoft)
- **GitLens** (optional, but great for seeing history)

VS Code has Git built in, so you can see changes, stage files, and commit from the Source Control tab on the left.

### 5. Install Python 3.12

```bash
python --version
```

Don't have it? Download from [python.org](https://www.python.org/downloads/). On Windows, tick **Add Python to PATH** during installation.

### 6. Connect Git to GitHub

You need a way to prove to GitHub that you are you. The easiest option for beginners:

1. Go to GitHub, then **Settings**, then **Developer settings**, then **Personal access tokens**.
2. Generate a new token with the `repo` scope.
3. When Git asks for a password on your first push, paste the token instead.

Prefer SSH? Follow GitHub's [guide to connecting with SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh).

### 7. Fork and clone this repo

1. Click **Fork** at the top right of this page to make your own copy.
2. Clone your fork:

```bash
git clone https://github.com/<your-username>/git-gud-workshop.git
cd git-gud-workshop
```

Replace `<your-username>` with your GitHub username. You'll do this properly in Module 2, but having it ready means you can follow along from the start.

## The Python Arena (Puzzles, Tasks & Boss Battles)

Once you're comfortable with Git and ready to put your Python skills to the test, jump into the **`arena/`**!

The arena is divided into 5 specialized divisions packed with coding puzzles, intentional bugs with hints, real datasets, and testcases:
- **`basics/`**: Variables, operations, input/output typecasting, conditionals, loops, and a multi-operator Calculator Boss (`boss.py`).
- **`intermediate/`**: List, tuple, dict, and set operations, math helpers (`fibonacci`, `factorial`, `is_prime`), lambdas, file handlers (txt, csv, json, sqlite), OOP classes, inheritance, and a Student Management System Boss (`boss.py`).
- **`advanced/`**: NumPy arrays & linear algebra, Pandas data manipulation & feature engineering, Matplotlib visualizations, Scikit-learn pipelines, and an interactive Tkinter Machine Learning App Boss (`boss.py`).
- **`miscellaneous/`**: Classic algorithms (binary search, two-pointer), core data structures (stacks, queues, linked lists), competitive programming challenges (two-sum, Kadane's max subarray), substitution ciphers (Caesar, Vigenère), terminal chatbot simulation, and lightweight Flask routing.
- **`assets/`**: Ready-to-use CSV/JSON datasets (sales, weather, attendance, student records) and generator scripts.

### ⚔️ How to Participate in the Arena:

1. **Initialize your personal solutions folder:**
   Run the setup script from the repository root:
   ```bash
   python my_dir_setup.py
   ```
   This automatically detects your GitHub username from your git remote origin and creates `SOLUTIONS/<your-username>_solutions/` with a clean copy of all the arena challenges.

2. **Solve the challenges:**
   Open the files inside `SOLUTIONS/<your-username>_solutions/`, follow the comments and hints, fix the bugs, and run the scripts to test your solutions.

3. **Submit your work:**
   Commit your changes to a new branch and open a Pull Request back to the main repository!

## How to Run

### Git modules (1 to 4)

These are hands-on. Open a terminal inside the repo folder (in VS Code: **Terminal**, then **New Terminal**) and follow the instructions in each module's folder. Type the commands yourself rather than copy-pasting, because that's how they stick.

### Python modules (5 to 7)

Run each script from inside its module folder, in order:

```bash
cd module-5-python-fundamentals
python 1variables_datatypes.py
```

### Quick Reference

| Module | Folder | Command | Notes |
|--------|--------|---------|-------|
| 1 | `module-1-git-fundamentals/` | Follow the module notes | Setup and config, nothing to run |
| 2 | `module-2-repository-basics/` | Follow the module notes | You'll create and clone repos |
| 3 | `module-3-workflow-branches/` | Follow the module notes | Make commits and branches as you go |
| 4 | `module-4-collaboration/` | Follow the module notes | You'll open a real pull request |
| 5 | `module-5-python-fundamentals/` | `python 1variables_datatypes.py` | Edit the values and rerun to see what changes |
| 6 | `module-6-python-collections/` | `python 3functions.py` | `5file_handling.py` creates a file in the same folder |
| 7 | `module-7-python-oop/` | `python 3inheritance.py` | Read the comments, then break things on purpose |

> If `python` doesn't work, try `python3`. Some systems use that name instead.

### Git Cheat Sheet

| Command | What it does |
|---------|--------------|
| `git init` | Start a new repository in the current folder |
| `git clone <url>` | Copy a remote repository to your machine |
| `git status` | See what's changed and what's staged |
| `git add <file>` | Stage a file for the next commit |
| `git commit -m "message"` | Save a snapshot with a message |
| `git push` | Send your commits to GitHub |
| `git pull` | Fetch and merge changes from GitHub |
| `git branch` | List branches |
| `git switch -c <name>` | Create and move to a new branch |
| `git merge <branch>` | Merge a branch into your current one |
| `git log --oneline` | View a compact commit history |
| `git restore <file>` | Discard unstaged changes to a file |

## Troubleshooting

- **"git is not recognized"**: Restart your terminal after installing. On Windows, make sure Git was added to PATH during installation.
- **Push asks for a password and rejects it**: GitHub no longer accepts account passwords. Use a personal access token or SSH.
- **Merge conflict markers (`<<<<<<<`) in my file**: Don't panic. That's Module 4. Open the file, pick which version to keep, delete the markers, then stage and commit.
- **I committed something by mistake**: Also Module 4. Nothing in Git is truly lost if you've committed it.
- **Python opens the Microsoft Store (Windows)**: Reinstall from python.org and tick **Add Python to PATH**.

## Prerequisites

You don't need to know Git or programming. You do need to be comfortable with:
- Using a computer: creating folders, moving files, installing software
- A little patience with the terminal. It looks scary, but we'll only use a handful of commands

## Contributing

Yes, you'll actually contribute to this repo. In Module 4 you'll add your name to `CONTRIBUTORS.md` using the full fork, branch, commit, push, and pull request flow. It's the exact process used on real open-source projects.

## What's Next?

Once you're through all seven modules, you can:
- **Contribute to open source**: Look for issues labelled `good first issue` on GitHub
- **Build a project**: Start a new repo, use branches for each feature, and track it properly from day one
- **Explore more Git**: Rebasing, stashing, tags, and GitHub Actions are all worth a look
- **Go deeper with Python**: Libraries like NumPy and OpenCV are a natural next step

Good luck, and remember: everyone has force-pushed something they shouldn't have. Commit early, commit often.
