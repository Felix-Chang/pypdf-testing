# pypdf Project

A Python project using the pypdf library for PDF manipulation.

## Prerequisites

- Python 3.11 or higher

## Setup Instructions

### 1. Create a Virtual Environment

A virtual environment keeps your project dependencies isolated from other Python projects.

```bash
python3 -m venv venv
```

### 2. Activate the Virtual Environment

**On macOS/Linux:**

```bash
source venv/bin/activate
```

**On Windows:**

```bash
venv\Scripts\activate
```

You should see `(venv)` appear in your terminal prompt, indicating the virtual environment is active.

### 3. Install Dependencies

With the virtual environment activated, install the required packages:

```bash
pip install pypdf
```

Or install from requirements.txt (if available):

```bash
pip install -r requirements.txt
```

### 4. Deactivate the Virtual Environment

When you're done working, you can deactivate the virtual environment:

```bash
deactivate
```

## Development

### Installing New Packages

Always activate your virtual environment before installing new packages:

```bash
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install package-name
```

### Updating requirements.txt

After installing new packages, update the requirements.txt file:

```bash
pip freeze > requirements.txt
```
