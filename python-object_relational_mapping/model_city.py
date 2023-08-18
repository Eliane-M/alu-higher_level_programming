#!/usr/bin/python3
"""
same as model_states
but contains the class definition for city
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import ForeignKey
from model_state import Base, State

Base = declarative_base()


class City(Base):
    '''links to the MySQL table `cities`'''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey('states.id'))
