#!/usr/bin/python3
"""Changes the name of a state object from the database hbtn_0e_6_usa"""

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

    states = session.query(State).all()

    for state in states:
        if state.id == 2:
            state.name = 'New Mexico'
            session.commit()
