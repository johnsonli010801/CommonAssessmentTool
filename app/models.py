"""
Database models module defining SQLAlchemy ORM models for the Common Assessment Tool.
Contains the Client model for storing client information in the database.
"""

from sqlalchemy import (
    Column,
    Integer,
    String,
    Boolean,
    ForeignKey,
    Enum,
)
from sqlalchemy.orm import relationship

from app.database import Base
from app.enums import UserRole
from app.validators import (
    age_constraint,
    gender_constraint,
    experience_constraint,
    school_level_constraint,
    scale_constraint,
    housing_constraint,
    income_source_constraint,
    success_rate_constraint,
)


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
    role = Column(Enum(UserRole), nullable=False)

    cases = relationship("ClientCase", back_populates="user")


class Client(Base):
    """
    Represents a Client in the database.
    Stores personal and case-related information for each client.
    """

    __tablename__ = "clients"

    id = Column(Integer, primary_key=True, autoincrement=True)
    age = Column(Integer)
    gender = Column(Integer)
    work_experience = Column(Integer)
    canada_workex = Column(Integer)
    dep_num = Column(Integer)
    canada_born = Column(Boolean)
    citizen_status = Column(Boolean)
    level_of_schooling = Column(Integer)
    fluent_english = Column(Boolean)
    reading_english_scale = Column(Integer)
    speaking_english_scale = Column(Integer)
    writing_english_scale = Column(Integer)
    numeracy_scale = Column(Integer)
    computer_scale = Column(Integer)
    transportation_bool = Column(Boolean)
    caregiver_bool = Column(Boolean)
    housing = Column(Integer)
    income_source = Column(Integer)
    felony_bool = Column(Boolean)
    attending_school = Column(Boolean)
    currently_employed = Column(Boolean)
    substance_use = Column(Boolean)
    time_unemployed = Column(Integer)
    need_mental_health_support_bool = Column(Boolean)

    cases = relationship("ClientCase", back_populates="client")

    # Apply constraints
    __table_args__ = (
        age_constraint(),
        gender_constraint(),
        experience_constraint("work_experience"),
        experience_constraint("canada_workex"),
        experience_constraint("dep_num"),
        school_level_constraint(),
        scale_constraint("reading_english_scale"),
        scale_constraint("speaking_english_scale"),
        scale_constraint("writing_english_scale"),
        scale_constraint("numeracy_scale"),
        scale_constraint("computer_scale"),
        housing_constraint(),
        income_source_constraint(),
        experience_constraint("time_unemployed"),
    )


class ClientCase(Base):
    """
    ClientCase class
    """

    __tablename__ = "client_cases"

    client_id = Column(Integer, ForeignKey("clients.id"), primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"), primary_key=True)

    employment_assistance = Column(Boolean)
    life_stabilization = Column(Boolean)
    retention_services = Column(Boolean)
    specialized_services = Column(Boolean)
    employment_related_financial_supports = Column(Boolean)
    employer_financial_supports = Column(Boolean)
    enhanced_referrals = Column(Boolean)
    success_rate = Column(Integer)

    client = relationship("Client", back_populates="cases")
    user = relationship("User", back_populates="cases")

    # Apply constraint
    __table_args__ = (
        success_rate_constraint(),
    )