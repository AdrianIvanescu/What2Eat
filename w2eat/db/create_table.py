import sqlite3

from colorama.ansi import Fore, Style


def create_table(table_name, column_name):
    # connecting to sqlite
    conn = sqlite3.connect("food.db")

    # creating a cursor object using the cursor() method
    cursor = conn.cursor()

    # drop food table if already exists.
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

    # create table as per requirement
    sql = f"""CREATE TABLE {table_name}(
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      {column_name} CHAR(30) NOT NULL
   )"""
    cursor.execute(sql)
    print(
        f">> The table {Fore.GREEN}{table_name}{Style.RESET_ALL} created successfully..."
    )

    # commit your changes in the database
    conn.commit()

    # closing the connection
    conn.close()
