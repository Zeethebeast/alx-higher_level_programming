#!/usr/bin/python3
import MySQLdb

def list_states(mysql_username, mysql_password, database_name, state_name):
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name,
    )

    cursor = db.cursor()
    state_names = "SELECT * FROM states WHERE name LIKE %s ORDER BY id ASC"
    cursor.execute(state_names, (state_name + '%',))

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()

if __name__ == "__main__":
    import sys
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]


    list_states(mysql_username, mysql_password, database_name, state_name)
