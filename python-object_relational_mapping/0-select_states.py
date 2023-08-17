#!/usr/bin/python3
"""
lists all states from the database hbtn_0e_0_usa
"""
import sys
import MYSQLdb


def list_states(username, password, db_name):
    """
    listing all states
    """
    connection_object = MYSQLdb.connect(
            host="localhost",
            user=user,
            passwd=passwd,
            db=db,
            port=3306)
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states ORDER BY states.id ASC;')
    for result in cursor.fetchall():
        print(result)


if __name__ == '__main__':
    list_states(argv[1], argv[2], argv[3])
