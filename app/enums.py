"""
Enum definitions for the Common Assessment Tool.
Contains enumerations used across the application.
"""

import enum


class UserRole(str, enum.Enum):
    """
    User Role class defining possible user roles in the system.
    """

    admin = "admin"
    case_worker = "case_worker"
