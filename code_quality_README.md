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
2. `flake8 app/ > flake8_report.txt`
3. `black --check --diff app/ > black_report.txt`
4. `mypy app/ > mypy_report.txt`

## Installation of Dependency on Main Code:
`pip install -r ./app/requirements.txt`

## To check the code using pre-commit:
```
pre-commit autoupdate
pre-commit run --all-files
```

## Refactoring for SOLID Principles

### Completed Refactorings:
- Extracted UserRole enum to a separate file (Single Responsibility Principle)
  - Created app/enums.py for all enumeration types
  - Improved code organization and reusability

- Extracted validation logic from models (Single Responsibility Principle)
  - Created app/validators.py with dedicated validation functions
  - Defined constants for validation boundaries
  - Made validation rules more maintainable and consistent
  - Simplified model classes to focus on structure, not validation

- Split database models into domain-specific files (Single Responsibility Principle)
  - Created separate files for User, Client, and relationship models
  - Organized models by domain area in app/models/ directory
  - Fixed imports to maintain compatibility with existing code
  - Improved code organization and maintainability
  - Made domain model boundaries clearer