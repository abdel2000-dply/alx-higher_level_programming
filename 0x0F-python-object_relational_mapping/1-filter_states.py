#!/usr/bin/python3
"""  lists all states with a name starting with N """

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
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    for state in cursor.fetchall():
        if row[1][0] == 'N':
            print(state)

    """ Close cursor and database connection """
    cursor.close()
    db.close()
