#!/usr/bin/python3
"""
script that lists all cities from the database hbtn_0e_4_usa
Result must be sorted in ascending order by states.id
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("""SELECT cities.id, cities.name, states.name
                FROM cities INNER JOIN states
                ON states.id = cities.state_id""")

    query_row = cur.fetchall()
    for row in query_row:
        print(row)
    cur.close()
    db.close()
