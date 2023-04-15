#!/usr/bin/python3
"""Takes in the name of a state as an argument and lists all
cities of that state, using the database hbtn_0e_4_usa"""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM cities\
            INNER JOIN states ON states.id = cities.state_id\
            ORDER BY cities.id")

    print(", ".join([rw[2] for rw in cur.fetchall() if rw[4] == sys.argv[4]]))
