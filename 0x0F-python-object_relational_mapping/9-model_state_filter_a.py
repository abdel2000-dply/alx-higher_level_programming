#!/usr/bin/python3
"""Prints the first State object from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username, password, db_name = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    states = session.query(State).filter(
        state.name.like('%a%')).order_by(State.id)

    for state in states:
        print(f"{state.id}: {state.name}")
