#!/usr/bin/python3
"""
Create states table in hbtn_0e_0_usa with some data
Usage: ./0-select_states.py <mysql username> \
                             <mysql password> \
                             <database name>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
cur = conn.cursor()
cur.execute("SELECT * FROM states ORDER BY state.Id ASC") # HERE I have to know SQL to grab all states in my database
query_rows = cur.fetchall()
for row in query_rows:
    print(row)
cur.close()
conn.close()
