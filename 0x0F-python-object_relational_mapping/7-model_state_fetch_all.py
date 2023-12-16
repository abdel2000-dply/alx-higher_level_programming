#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""

from SQLAlchemy import create_engine, select
from sys import argv
from model_state import Base, State

if __name__ == "__main__":
    # Connect to the database
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'
        .format(user, passwd, db)
    )

    conn = engine.connect()
    query = select(State).order_by(State.id)
    states = conn.execute(query)
    for state in states:
        print("{:d}: {:s}".format(state.id, state.name))

    # Close the session
    session.close()
