"""
Validation utilities for the Common Assessment Tool.
Contains functions and constants for validating model data.
"""

from sqlalchemy import CheckConstraint

# Constants for validation
MIN_AGE = 18
GENDER_VALUES = [1, 2]
MIN_SCALE_VALUE = 0
MAX_SCALE_VALUE = 10
MIN_SCHOOLING_LEVEL = 1
MAX_SCHOOLING_LEVEL = 14
MIN_HOUSING_LEVEL = 1
MAX_HOUSING_LEVEL = 10
MIN_INCOME_SOURCE = 1
MAX_INCOME_SOURCE = 11
MIN_SUCCESS_RATE = 0
MAX_SUCCESS_RATE = 100

# Constraint creation functions
def age_constraint():
    """Create a constraint to ensure age is at least 18."""
    return CheckConstraint(f"age >= {MIN_AGE}")

def gender_constraint():
    """Create a constraint to ensure gender is a valid value."""
    return CheckConstraint("gender = 1 OR gender = 2")

def experience_constraint(field_name):
    """Create a constraint to ensure experience is not negative."""
    return CheckConstraint(f"{field_name} >= 0")

def school_level_constraint():
    """Create a constraint to ensure schooling level is within valid range."""
    return CheckConstraint(
        f"level_of_schooling >= {MIN_SCHOOLING_LEVEL} AND "
        f"level_of_schooling <= {MAX_SCHOOLING_LEVEL}"
    )

def scale_constraint(field_name):
    """Create a constraint to ensure scale values are within 0-10 range."""
    return CheckConstraint(
        f"{field_name} >= {MIN_SCALE_VALUE} AND "
        f"{field_name} <= {MAX_SCALE_VALUE}"
    )

def housing_constraint():
    """Create a constraint to ensure housing value is valid."""
    return CheckConstraint(
        f"housing >= {MIN_HOUSING_LEVEL} AND "
        f"housing <= {MAX_HOUSING_LEVEL}"
    )

def income_source_constraint():
    """Create a constraint to ensure income source value is valid."""
    return CheckConstraint(
        f"income_source >= {MIN_INCOME_SOURCE} AND "
        f"income_source <= {MAX_INCOME_SOURCE}"
    )

def success_rate_constraint():
    """Create a constraint to ensure success rate is within valid range."""
    return CheckConstraint(
        f"success_rate >= {MIN_SUCCESS_RATE} AND "
        f"success_rate <= {MAX_SUCCESS_RATE}"
    )

def username_length_constraint():
    """Create a constraint to ensure username has a minimum length."""
    MIN_USERNAME_LENGTH = 3
    return CheckConstraint(f"LENGTH(username) >= {MIN_USERNAME_LENGTH}")

def email_format_constraint():
    """Create a constraint to ensure email contains @ symbol."""
    return CheckConstraint("email LIKE '%@%'")