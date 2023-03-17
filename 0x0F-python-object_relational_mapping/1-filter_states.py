#!/usr/bin/python3
"""
script that lists all states with name starting from N from db hbtn_0e_0usa
Result must be sorted in ascending order by states.id
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    cur.execute("""SELECT * FROM states WHERE name LIKE BINARY 'N%'
                ORDER BY states.id""")
    query_row = cur.fetchall()
    for row in query_row:
        print(row)
    cur.close()
    db.close()
