#!/usr/bin/python3
""" This script lists all states from database hbtn_0e_0_usa. """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    data_base = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = data_base.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name FROM\
    cities INNER JOIN states ON cities.state_id = states.id WHERE\
    states.name = %s ORDER BY cities.id ASC", (argv[4], ))

    cities = []
    for row in cursor.fetchall():
        cities.append(row[1])
    print(", ".join(cities))

    cursor.close()
    data_base.close()
