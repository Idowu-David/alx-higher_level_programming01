#!/usr/bin/python3
""" This script displays all values in the states table where namr matches
the argument from the database `hbtn_0e_0_usa`:
    => This script takes 4 arguments:
    mysql username, mysql password, database name and state name searched.
    => This script connects to a MySQL server running on localhost at port 3306
    => Results are sorted in ascending order by states.id
"""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    pwd = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost",
                         user=username,
                         password=pwd,
                         database=database,
                         port=3306)
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name = '{}' \
            ORDER BY states.id".format(state_name)
    cur.execute(query)
    states = cur.fetchall()
    for state in states:
        print(state)
    db.close()
