#!/usr/bin/python3
"""
 the class definition of a State
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

# Creating an instance of declarative_base
Base = declarative_base()

class State(Base):
    """
    Class State
    """
    __tablename__ = "states"
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
