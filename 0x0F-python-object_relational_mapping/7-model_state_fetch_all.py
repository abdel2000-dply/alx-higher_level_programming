#!/usr/bin/python3
"""
lists all State objects from the database hbtn_0e_6_usa
"""

from SQLAlchemy import create_engine
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Connect to the database
    user = argv[1]
    passwd = argv[2]
    db = argv[3]
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.
        format(user, passwd, db), pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id)
    for state in states:
        print("{:d}: {:s}".format(state.id, state.name))

    # Close the session
    session.close()
