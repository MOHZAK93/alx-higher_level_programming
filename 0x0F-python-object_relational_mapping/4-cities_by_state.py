#!/usr/bin/python3
"""Takes an argument, validate it and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument"""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
            INNER JOIN states ON states.id = cities.state_id")

    results = cur.fetchall()
    for row in results:
        print(row)
