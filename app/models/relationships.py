# app/models/relationships.py
"""
Relationship models for the Common Assessment Tool.
Contains models that connect other entities in the system.
"""

from sqlalchemy import Column, Integer, Boolean, ForeignKey
from sqlalchemy.orm import relationship

from app.database import Base
from app.validators import success_rate_constraint

class ClientCase(Base):
    """
    Represents the relationship between a client and a case worker.
    Stores service information and outcomes for each client-user relationship.
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

    # Apply constraints
    __table_args__ = (
        success_rate_constraint(),
    )