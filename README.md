# Python Practice

A structured repository for practicing Python, data structures, OOP, and data science libraries using both **Jupyter notebooks** and **Python scripts**.

## Goals

- Learn Python fundamentals interactively with notebooks.
- Practice problems and reusable code in `.py` scripts.
- Build a clean, navigable portfolio of Python work.
- Prepare for data analysis and machine learning.

## Repository Structure

```text
01-python-basics/
02-data-structures/
03-oop/
04-modules-files-exceptions/
05-numpy/
06-pandas/
07-visualization/
08-machine-learning/
09-mini-projects/
scripts/
```

Each topic folder contains:

- `notebooks/` → `.ipynb` files for learning and exploration.
- `scripts/` → `.py` files for practice problems and utilities.

## Topics

### 01. Python Basics

Notebooks:

- `01-variables-and-data-types.ipynb`
- `02-operators.ipynb`
- `03-if-else.ipynb`
- `04-loops.ipynb`
- `05-functions.ipynb`

Scripts:

- `practice-problems.py`

### 02. Data Structures

Notebooks:

- `01-lists.ipynb`
- `02-tuples-sets-dictionaries.ipynb`

Scripts:

- `list-practice.py`
- `dict-practice.py`

### 03. Object-Oriented Programming

Notebooks:

- `01-classes-and-objects.ipynb`
- `02-inheritance.ipynb`
- `03-polymorphism.ipynb`
- `04-encapsulation.ipynb`
- `05-abstraction.ipynb`

Scripts:

- `bank-account.py`

### 04. Modules, Files, Exceptions

Notebooks:

- `01-modules-and-packages.ipynb`
- `02-file-handling.ipynb`
- `03-exception-handling.ipynb`

Scripts:

- `file-examples.py`

### 05. NumPy

Notebooks:

- `01-numpy-basics.ipynb`
- `02-array-operations.ipynb`

Scripts:

- `exercises.py`

### 06. Pandas

Notebooks:

- `01-pandas-basics.ipynb`
- `02-data-cleaning.ipynb`
- `03-data-analysis.ipynb`

Datasets:

- `datasets/` (small samples only; large datasets linked externally)

### 07. Visualization

Notebooks:

- `01-matplotlib-basics.ipynb`
- `02-seaborn-basics.ipynb`

Scripts:

- `plots-examples.py`

### 08. Machine Learning

Notebooks:

- `01-regression.ipynb`
- `02-classification.ipynb`
- `03-clustering.ipynb`

Models:

- `models/` (no large model files in Git)

### 09. Mini Projects

- `expense-tracker/`
- `csv-data-analyzer/`
- `todo-cli/`

Each mini-project has its own `README.md` explaining how to run it.

## How to Use

1. Clone the repository:
   ```bash
   git clone https://github.com/Chiraggalav0024/python-practice.git
   cd python-practice
   ```

2. (Optional) Create a virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start Jupyter:
   ```bash
   jupyter notebook
   ```

5. Open notebooks from any `notebooks/` folder.
6. Run scripts with:
   ```bash
   python 01-python-basics/scripts/practice-problems.py
   ```

## Notes

- Use notebooks for:
  - Learning concepts
  - Experimenting with code
  - Visualizations and EDA
- Use scripts for:
  - Practice problems
  - Reusable functions
  - Small utilities
- Do not commit:
  - `.ipynb_checkpoints`
  - Virtual environments
  - Large datasets or model files
- Keep notebooks clean:
  - Restart & run all before committing.
  - Clear unnecessary large outputs.

## License

This repository is for personal learning and practice.
