#!/usr/bin/python3
"""
contains the class definition of a State and an instance Base = declarative_base():
"""
import MySQLdb
from sys import argv
from model_state import Base, State
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    class state that inherits from base
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True)
    name =  Column(String(128))
def list_states_starting_with_N(user, passwd, db):
    '''List all states ordered by id in
    ascending order that start with "N"'''
    db = MySQLdb.connect(
        host="localhost",
        user=user,
        passwd=passwd,
        db=db,
        port=3306)
