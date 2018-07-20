#!/usr/bin/python3
""" This script lists all states from database hbtn_0e_0_usa. """

import MySQLdb
from sys import argv

if __name__ == "__main__":
    data_base = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = data_base.cursor()

    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    data_base.close()
