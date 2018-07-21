#!/usr/bin/python3
"""
This script lists all City objects from the database hbtn_0e_6_usa.
"""

from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(argv[1], argv[2], argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    Base.metadata.create_all(engine)

    city_objects = session.query(City, State).join(State).\
        order_by(City.id).all()

    for cities, state in session.query(City, State).join(State).\
            order_by(City.id).all():
        print("{}: ({}) {}".format(state.name, cities.id, cities.name))

    session.close()
