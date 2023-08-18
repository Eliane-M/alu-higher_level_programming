#!/usr/bin/python3
"""
lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa
"""
from sys import argv

from sqlalchemy import (create_engine)
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine(
        f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost/{argv[3]}')
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).order_by(State.id):
        if 'a' in instance.name:
            print(f"{instance.id}: {instance.name}")
