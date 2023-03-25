#!/usr/bin/python3
"""
Script that deletes all State objects with a name containing the letter
a from the database hbtn_0e_6_usa
"""
from model_state import Base, State
from model_city import City
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    session.commit()
    inst = session.query(State.name, City.id, City.name).filter(
            State.id == City.state_id).all()
    for state in inst:
        print("{}: ({}) {}".format(state[0], state[1], state[2]))
