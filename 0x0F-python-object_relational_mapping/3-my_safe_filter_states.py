#!/usr/bin/python3
"""
script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
It should be free from MySQL injection
Result must be sorted in ascending order by states.id
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE %s""", (sys.argv[4],))

    query_row = cur.fetchall()
    for row in query_row:
        print(row)
    cur.close()
    db.close()
