#!/usr/bin/python3
"""
deletes all State objects with a name containing the letter a
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username, password, db_name = argv[1], argv[2], argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state_del = session.query(State).filter(State.name.like('%a%')).all()
    for s in state_del:
        session.delete(s)

    session.commit()
    session.close()
