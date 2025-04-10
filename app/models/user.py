# app/models/user.py
"""
User-related database models for the Common Assessment Tool.
Contains models related to system users and authentication.
"""

from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.orm import relationship

from app.database import Base
from app.enums import UserRole
from app.validators import username_length_constraint, email_format_constraint


class User(Base):
    """
    Represents a User in the database.
    Stores user details including authentication and roles.
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    hashed_password = Column(String(200), nullable=False)
    role = Column(Enum(UserRole), nullable=False)  # type: ignore

    cases = relationship("ClientCase", back_populates="user")

    # Apply User-specific constraints
    __table_args__ = (
        username_length_constraint(),
        email_format_constraint(),
    )
