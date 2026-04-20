# 100-days-of-ai-projects
A 100-day challenge to build AI, Machine Learning, and Python projects focused on real-world applications and placement readiness.
# Code Quality Checker 🚀

A Python-based Code Quality Checker that performs static code analysis on Python files. It helps detect syntax errors, style violations, formatting issues, and generates a final code quality score.

This project is useful for improving code readability, maintainability, and writing cleaner Python programs.

---

## Features

* Syntax Error Detection using AST
* PEP 8 Style Checking
* Missing Spaces Detection
* Long Line Detection
* Code Quality Score Generation
* Simple and Clean Python Project Structure

---

## Technologies Used

* Python
* AST (Abstract Syntax Tree)
* Basic Static Code Analysis
* PEP 8 Style Rules

---

## Project Structure

```text
Day-07-Code-Quality-Checker/
│
├── main.py
├── analyzer.py
├── style_checker.py
├── score_generator.py
├── sample_code.py
├── requirements.txt
└── README.md
```

---

## How It Works

### Step 1 — Input File

The project reads a Python file (`sample_code.py`) containing code to analyze.

### Step 2 — Syntax Analysis

Using Python AST, the system checks whether the code contains syntax errors.

### Step 3 — Style Analysis

The project checks:

* spaces around `=`
* long lines (>79 characters)
* formatting issues

### Step 4 — Score Generation

A final score out of 100 is generated based on detected issues.

---

## Example Input

```python
a=10
b=20

def calc():
 print(a+b)

for i in range(5):
 print(i)

calc()
```

---

## Example Output

```text
🚀 Python Code Quality Checker

Syntax Analysis:
✅ No Syntax Errors Found

Style Analysis:
Line 1: Missing spaces around '='
Line 2: Missing spaces around '='

⭐ Final Code Quality Score: 90/100
```

---

## Installation

### Clone the Repository

```bash
git clone your-github-link
cd Day-07-Code-Quality-Checker
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Run the Project

```bash
python main.py
```

---

## Future Improvements

* Variable Naming Analysis
* Function Complexity Detection
* Duplicate Code Detection
* Automatic Code Suggestions
* GitHub Integration
* Streamlit Web UI
* AI-Powered Code Review using LLMs

---

## Why This Project?

This project demonstrates:

* Python fundamentals
* Static code analysis
* Problem-solving
* Real-world developer tool building
* Placement-ready project development

It is a strong resume project for Python, AI, and software engineering roles.

---

## Author

**Sayanth**

MSc Artificial Intelligence and Machine Learning
Building 100 Days of Placement-Ready AI Projects 🔥
