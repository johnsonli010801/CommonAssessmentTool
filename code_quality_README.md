# Code Quality Analysis

## Setup
1. Create a virtual environment:
   `python -m venv venv`

2. Activate the virtual environment:
   - Windows: `venv\Scripts\activate`
   - Mac/Linux: `source venv/bin/activate`

## Installation
Install development tools with:
`pip install -r requirements-dev.txt`

## Running Analysis
Run these commands to analyze code quality:
1. `pylint app/ > pylint_report.txt`
2. `flake8 app/ > flake8_report.txt`
3. `black --check --diff app/ > black_report.txt`
4. `mypy app/ > mypy_report.txt`
