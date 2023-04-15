#!/usr/bin/python3
import MySQLdb
"""Get all states module"""


db = MySQLdb.connect(user='root', password='password', db='hbtn_0e_0_usa')
cur = db.cursor()
cur.execute('SELECT * FROM states')
results = cur.fetchall()
for row in results:
    print(row)
