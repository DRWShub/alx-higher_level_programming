#!/usr/bin/python3
"""Lists all states from database"""
import MySQLdb
import sys

if __name__ == "__main__":

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    exact = sys.argv[4]
    cur.execute("SELECT * FROM states WHERE name LIKE %s", (exact, ))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()