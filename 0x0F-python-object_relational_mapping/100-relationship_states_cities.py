#!/usr/bin/python3
"""Creates a State and City relationship"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State, City

if __name__ == "__main__":
    username, password, dbname = sys.argv[1], sys.argv[2], sys.argv[3]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, dbname),
                           pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="California")
    new_city = City(name="San Francisco", state=new_state)
    session.add(new_state)
    session.add(new_city)
    session.commit()
    session.close()
