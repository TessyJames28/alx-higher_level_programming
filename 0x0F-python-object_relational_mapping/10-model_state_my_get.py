#!/usr/bin/python3
"""
script that prints the State object with the name passed as argument from the
database hbtn_0e_6_usa
"""
from model_state import Base, State
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    ins = session.query(State).filter(State.name == sys.argv[4])
    try:
        print(ins[0].id)
    except IndexError:
        print("Not found")
