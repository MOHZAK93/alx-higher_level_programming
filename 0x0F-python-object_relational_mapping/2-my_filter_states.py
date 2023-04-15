#!/usr/bin/python3
"""Takes an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument"""


import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute('SELECT * FROM states')
    results = cur.fetchall()
    for row in results:
        if row[1] == sys.argv[4]:
            print(row)
