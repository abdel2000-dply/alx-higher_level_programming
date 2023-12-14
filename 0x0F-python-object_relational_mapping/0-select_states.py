#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """

import MySQLdb
from sys import argv


if __name__ == "__main__":

	""" Connect to db """
	db = MySQLdb.connect(host="localhost",
                         port=3306,
			             user=argv[1],
			             passwd=argv[2],
			             db=argv[3])

    """ Create cursor """
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    for state in cursor.fetchall():
        print(state)

    """ Close cursor and database connection """
    cursor.close()
    db.close()
