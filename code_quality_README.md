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

Run these commands to analyze code quality: 2. `flake8 app/ > flake8_report.txt` 3. `black --check --diff app/ > black_report.txt` 4. `mypy app/ > mypy_report.txt`

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

- Refactored ML model implementation (Story 2 preparation)

  - Created a base model interface following the Interface Segregation Principle
  - Implemented multiple concrete model classes (Random Forest, Gradient Boosting, Linear Regression)
  - Added a model registry implementing the Open/Closed Principle for easy model extension
  - Separated data processing from model logic following Single Responsibility Principle
  - Created a test script to verify model switching functionality

- Refactored ClientService into two focused service classes: ClientQueryService and ClientMutationService

  - Applied the Single Responsibility Principle (SRP) to separate read and write operations
  - Followed Separation of Concerns to isolate query logic from mutation logic
  - Removed duplicated filtering code with a shared criteria filter method

- Refactored the authentication system using modular service classes
  - Applied the Single Responsibility Principle by isolating password logic (SecurityService), token logic (TokenService), and user operations (UserService)
  - Followed Separation of Concerns to decouple route handlers from business logic
  - Prepared the architecture for future enhancements such as role-based access control, refresh tokens, and password policies

## Testing the ML Models

To test the machine learning model implementation and model switching capability:

1. Ensure you have installed the required dependencies:
   pip install numpy pandas scikit-learn

2. Run the test script:
   python -m app.ml.test_models

3. The test will:

- Initialize the model registry
- Register three different model types
- Display available models
- Switch between models
- Train each model with sample data
- Make predictions with each model

## Story 2 Implementation: Multiple ML Model Support

### Completed Features:

- Implemented a flexible ML model architecture with model switching capability
- Created a base model interface that all model types implement
- Developed three different model implementations:
  - Random Forest (default model)
  - Gradient Boosting
  - Linear Regression
- Created a model registry to manage different model types and switching
- Implemented API endpoints for model management

### API Endpoints for Model Management

The following endpoints are now available for interacting with ML models:

1. **Get Current Model**

   - Endpoint: `GET /models/current`
   - Description: Returns the name of the currently active model
   - Response example: `{"name": "RandomForest"}`
   - Test command: `curl -X GET "http://127.0.0.1:8000/models/current"`

2. **List Available Models**

   - Endpoint: `GET /models/available`
   - Description: Returns all available models and indicates the current model
   - Response example: `{"models": ["RandomForest", "GradientBoosting", "LinearRegression"], "current_model": "RandomForest"}`
   - Test command: `curl -X GET "http://127.0.0.1:8000/models/available"`

3. **Switch Model**
   - Endpoint: `POST /models/switch/{model_name}`
   - Description: Changes the active model to the specified model
   - Response example: `{"name": "GradientBoosting"}`
   - Test command: `curl -X POST "http://127.0.0.1:8000/models/switch/GradientBoosting"`

### Testing the Model Switching Functionality

You can test the model switching functionality in two ways:

#### 1. Using the Swagger UI:

- Start the application: `uvicorn app.main:app --reload`
- Navigate to: `http://127.0.0.1:8000/docs`
- Scroll to the "models" section
- Try each endpoint by clicking "Try it out" and "Execute"

#### 2. Using the ML Test Script:

- Run: `python -m app.ml.test_models`
- This will test model registration, switching, and prediction capability

### Implementation Details

- **Model Registry Pattern**: Used a singleton registry to manage models
- **Strategy Pattern**: Each model implementation follows the same interface
- **Dependency Injection**: High-level components use abstractions rather than concrete implementations
- **Open for Extension**: New models can be added without modifying existing code

This implementation satisfies all requirements for Story 2 while following SOLID principles.
