#!/usr/bin/python3
"""First state model"""


import sys
import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

"""Parent class"""
Base = declarative_base()


class State(Base):
    """Derived class"""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
