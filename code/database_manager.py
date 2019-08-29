import sqlite3
import os
from sqlite3 import Error


def create_connection(db_file):
    """creates a database connection to SQLite database
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return None


def create_table(conn, create_table_sql):
    """create a table from the sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
    except Error as e:
        print(e)


def add_move(conn, move):
    """
    add a new dance move to the table
    :param conn: Connection object
    :param move: tuple, with dance move details
    :return:
    """
    tags = ';'.join(move.tags) if move.tags else None
    dance_move = (move.name, move.category, tags, move.description)

    if move_exists(conn, move):
        print("move already exists!!")
        return

    sql_cmd = """ INSERT INTO moves(name, category, tags, description) 
                  VALUES (?,?,?,?)
    """
    cursor = conn.cursor()
    cursor.execute(sql_cmd, dance_move)

    # cursor.commit()
    return cursor.lastrowid


def move_exists(conn, move):
    """
    checks if the move to be added exists
    :param conn: Connection object
    :param move: a Dance Move object
    :return: Boolean: Returns True if move exists in database. Returns False otherwise
    """
    cursor = conn.cursor()
    cursor.execute("SELECT name, category FROM moves")
    moves = cursor.fetchall()
    return (move.name, move.category) in moves


def delete_move(conn):
    """
    deletes all moves that match the given name. Expected that only one move has that name
    :param conn: Connection object
    :param name: String: dance move name
    :return: 
    """
    sql_cmd = "DELETE FROM moves WHERE name='' "
    cursor = conn.cursor()
    cursor.execute(sql_cmd)
    cursor.commit()


def delete_all_moves(conn):
    """
    deletes all the moves from the moves table
    :param conn: Connection object
    :return: 
    """
    sql_cmd = "DELETE FROM moves"
    cursor = conn.cursor()
    cursor.execute(sql_cmd)
    cursor.commit()
    

def update_move(conn, move):
    """
    update dance move name
    :param conn: Connection object
    :param move: tuple, w/ move name
    :return:
    """
    sql_cmd = """ UPDATE moves
                  SET name = ?
                  WHERE name = ?
              """

    cursor = conn.cursor()
    cursor.execute(sql_cmd, move)


def select_all_moves(conn):
    """
    selects all the dance moves from the database
    :param conn: Connection object
    :return: list:
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM moves")

    rows = cursor.fetchall()
    # for row in rows:
    #     print(type(row))
    #     print(row)
    # print(type(rows))

    return rows


def select_by_x(conn, **kwargs):
    """
    selects some moves based on certain attributes
    :param conn: Connection object
    :param kwargs: dictionary of keyword arguments
    :return: list of selected rows
    """
    print(str(kwargs))
    condition = []
    for key, val in kwargs.items():
        condition.append(str(key) + " = " + str(val))
    print(condition)


def print_entries(conn):
    """
    prints the table entries
    :param conn: Connection object
    :return:
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM moves")
    ans = cursor.fetchall()

    for i in ans:
        print(i)


def main():
    pass
    database = os.path.abspath("./dance.db")

    sql_create_dance_table = """ CREATE TABLE IF NOT EXISTS moves (
                                    name text,
                                    category text
                                );
    """

    conn = create_connection(database)
    if conn is not None:
        create_table(conn, sql_create_dance_table)
    else:
        print("Error! Can't create the database connection")
