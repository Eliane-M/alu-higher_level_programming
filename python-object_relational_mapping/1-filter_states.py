#!/usr/bin/python3
"""
lists all states starting with 'N'
states are in database hbtn_0e_0_usa
order in ascendin order
"""
from sys import argv
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
    cursor.execute(query)

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    connection.close()

    except MySQLdb.Error as e:
        print("Error:", e)


if __name__ == "__main__":
    if len(sys.argv) == 4:
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]
        list_states_with_n(username, password, db_name)
    else:
        print("Usage: python script.py <username> <password> <db_name>")
