#!/usr/bin/python3
"""
lists all states starting with 'N'
"""
import sys
import MySQLdb


def list_starting_with_N(username, passwordd, db_name):
    """
    list states starting with n in ascending order by states_id
    """
    db = MySQLdb.connect(
            host='localhost'
            user=username
            passwd=password
            db=db_name
            port=3306)
    cursor = db.cursor()

    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY ASC 'id'"

