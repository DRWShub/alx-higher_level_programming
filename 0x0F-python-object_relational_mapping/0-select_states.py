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
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM `states`")
    [print(state) for state in c.fetchall()]