#!/usr/bin/python3
""" This script takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    data_base = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = data_base.cursor()
    cursor.execute("SELECT * FROM states WHERE name = '{}'\
    ORDER BY states.id ASC".format(argv[4]))

    for row in cursor.fetchall():
        if row[1] == argv[4]:
            print(row)

    cursor.close()
    data_base.close()
