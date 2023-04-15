#!/usr/bin/python3
import sys
import MySQLdb

"""Get all states module"""


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], password=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute('SELECT * FROM states')
    results = cur.fetchall()
    for row in results:
        print(row)
