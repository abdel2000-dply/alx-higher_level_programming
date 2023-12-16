#!/usr/bin/python3
"""
 adds the State object “Louisiana” to the database hbtn_0e_6_usa
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

    state_up = session.query(State).filter_by(id=2).first()
    if state_up:
        state_up.name = 'New Mexico'
        session.commit()

    session.close()
