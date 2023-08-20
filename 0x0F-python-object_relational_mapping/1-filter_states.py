#!/usr/bin/python3
""" This script lists all states with a name starting with N(upper)
    from the database `hbtn_0e_0_usa`:
    => This script takes 3 arguments:
    mysql username, mysql password and database name.
    => This script connects to a MySQL server running on localhost at port 3306
    => Results are sorted in ascending order by states.id
"""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    pwd = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost",
                         user=username,
                         password=pwd,
                         database=database,
                         port=3306)
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY states.id"
    cur.execute(query)
    states = cur.fetchall()
    for state in states:
        print(state)
    db.close()
