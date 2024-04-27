#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""
import MySqldb
import sys


def list_states(username, password, dbname):

    db = MySQLdb.connect(host="localhost", user=username,
                         passwd=password, db=dbname, port=3306)

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY is ASC")

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()


if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    list_states(username, password, dbname)
