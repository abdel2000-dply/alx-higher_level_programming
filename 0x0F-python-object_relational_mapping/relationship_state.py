#!/usr/bin/python3
"""
 the class definition of a State
"""
from sqlalchemy import Column, Integer, String
from relationship_city import Base, City
from sqlalchemy.orm import relationship


class State(Base):
    """
    Class State
    """
    __tablename__ = "states"
    id = Column(Integer, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship(
        'City', backref='state', cascade='all, delete-orphan')
