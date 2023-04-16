#!/usr/bin/python3
"""Prints all City objects from the database hbtn_0e_6_usa"""

import sys
from model_state import Base, State
from model_city import City

from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


if __name__ == "__main__":
    """Make a connection to database"""
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3], poop_pre_ping=True))

    """Create a session object"""
    session = Session(engine)

    for state, city in session.query(State, City).filter(
            State.id == City.state_id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))
