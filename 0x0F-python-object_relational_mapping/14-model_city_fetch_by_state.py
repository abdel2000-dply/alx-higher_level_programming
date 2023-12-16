#!/usr/bin/python3
"""
Lists all City objects from the database hbtn_0e_14_usa
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import City

if __name__ == "__main__":
    username, password, db_name = argv[1], argv[2], argv[3]

    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}',
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(State, City).filter(
        State.id == City.state_id).order_by(City.id)
    for s, c in cities:
        print(f"{s.name}: ({c.id}) {c.name}")

    session.close()
