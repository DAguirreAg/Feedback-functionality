from sqlalchemy import Column, Integer, String, DateTime, Boolean, ForeignKey, Sequence, MetaData, Date, PrimaryKeyConstraint
from sqlalchemy.sql import func

from .database import Base, engine

class Feedback(Base):
    __tablename__ = 'feedback'

    id = Column(Integer, primary_key=True, unique=True)
    email = Column(String, nullable=True, unique=False)
    feedback = Column(String, nullable=False)
