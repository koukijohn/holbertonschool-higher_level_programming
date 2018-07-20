#!/usr/bin/python3
""" This script takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
---SAFE FROM MYSQL INJECTIONS
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    data_base = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cursor = data_base.cursor()
    cursor.execute("SELECT * FROM states WHERE name = %s\
    ORDER BY states.id ASC", (argv[4], ))

    for row in cursor.fetchall():
            print(row)

    cursor.close()
    data_base.close()
