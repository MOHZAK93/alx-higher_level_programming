#!/usr/bin/python3
"""Lists all states with a name starting
with N from the database hbtn_0e_0_usa"""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute('SELECT * FROM states')
    results = cur.fetchall()
    for row in results:
        if row[1][0] == 'N':
            print(row)