#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists all cities of that state
"""

import MySQLdb
from sys import argv


if __name__ == "__main__":

    """ Connect to db """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3]
    )

    """ Create cursor """
    cursor = db.cursor()
    cursor.execute(
        """SELECT cities.name
        FROM cities JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC""", (argv[4],)
    )

    for state in cursor.fetchall():
        print(state)

    """ Close cursor and database connection """
    cursor.close()
    db.close()
