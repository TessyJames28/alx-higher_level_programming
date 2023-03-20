#!/usr/bin/python3
"""
script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""
from model_state import Base, State
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    new_inst = State(name='Louisiana')
    session.add(new_inst)
    ins = session.query(State).filter_by(name == 'Louisiana').first()
    print(ins.id)
    session.commit()
