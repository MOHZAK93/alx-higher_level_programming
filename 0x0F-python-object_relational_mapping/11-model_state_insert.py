#!/usr/bin/python3
"""Adds a new state to the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State

from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


if __name__ == "__main__":
    """Make a connection to database"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3], poop_pre_ping=True))

    """Create a session object"""
    session = Session(engine)

    new_state = State(name='Louisiana')
    session.add(new_state)

    states = session.query(State).filter_by(name='Louisiana').first()

    print(states.id)
