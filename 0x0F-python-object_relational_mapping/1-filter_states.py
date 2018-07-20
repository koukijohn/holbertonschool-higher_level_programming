#!/usr/bin/python3
""" This script lists all states with a name starting with N  """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    data_base = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = data_base.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY
                   states.id ASC")

    for name in cursor.fetchall():
        print(name)

    cursor.close()
    data_base.close()
