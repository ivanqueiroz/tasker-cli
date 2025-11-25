# Tasker CLI

A simple command-line interface (CLI) for managing tasks, written in Python.

## Stack

- **Language:** Python 3
- **Libraries:**
    - `argparse` (Standard library) for argument parsing.
    - `json` (Standard library) for data storage.
    - `datetime` (Standard library) for timestamps.
    - `os` (Standard library) for file operations.

## Functionality

This tool allows you to:
- Add new tasks.
- Update existing tasks.
- Delete tasks.
- Mark tasks as "in-progress" or "done".
- List all tasks or filter by status.

## Installation

1. Clone the repository.
2. Ensure you have Python installed.
3. (Optional) Install dependencies if you plan to develop or format code (e.g., `black`):
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Run the application using `python application.py`.

### Examples

**1. Add a new task**
```bash
python application.py add "Buy groceries"
```

**2. List all tasks**
```bash
python application.py list
```

**3. List tasks by status**
```bash
python application.py list todo
python application.py list in-progress
python application.py list done
```

**4. Update a task description**
```bash
python application.py update 1 "Buy groceries and milk"
```
*(Replaces the description of task with ID 1)*

**5. Mark a task as in-progress**
```bash
python application.py mark-in-progress 1
```

**6. Mark a task as done**
```bash
python application.py mark-done 1
```

**7. Delete a task**
```bash
python application.py delete 1
```
