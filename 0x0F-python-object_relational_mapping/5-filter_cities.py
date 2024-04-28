#!/usr/bin/python3
"""
lists all cities of that state, using the database
hbtn_0e_4_usa
"""
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name \
    FROM cities JOIN states ON cities.state_id = state.id \
    WHERE states.name = '{}';".format(sys.argv[4]))
    states = cursor.fetchall()

    print(", ".join([state[1] for state in states]))
