# app/models/client.py
"""
Client-related database models for the Common Assessment Tool.
Contains models for storing client information.
"""

from sqlalchemy import Column, Integer, Boolean
from sqlalchemy.orm import relationship

from app.database import Base
from app.validators import (
    age_constraint,
    gender_constraint,
    experience_constraint,
    school_level_constraint,
    scale_constraint,
    housing_constraint,
    income_source_constraint,
)

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