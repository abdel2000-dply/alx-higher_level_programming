#!/usr/bin/python3
"""
 lists all State objects that contain the letter a
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
    session = Session()

    states = session.query(State).filter(
        State.name.like('%a%')).order_by(State.id)

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()
