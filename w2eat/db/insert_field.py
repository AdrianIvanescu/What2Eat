import sqlite3
import os
from colorama.ansi import Fore, Style


def insert_field(table_name, colum_name, file_name):

    try:
        rel_path = "input"
        file_text = open(
            f"{os.path.join(os.path.dirname(__file__), rel_path)}/{file_name}",
            "r",
        )

        # connecting to sqlite
        conn = sqlite3.connect("food.db")

        # creating a cursor object using the cursor() method
        cursor = conn.cursor()

        # truncate the table if already exists
        cursor.execute(f"DELETE from {table_name}")

        # create table as per requirement
        sql = f"""INSERT INTO {table_name}({colum_name})
               VALUES
                    {file_text.read()}
            """
        cursor.executescript(sql)
        print(
            f">> The field {Fore.GREEN}{colum_name}{Style.RESET_ALL} inserted into {Fore.GREEN}{table_name}{Style.RESET_ALL} successfully..."
        )

        # commit your changes in the database
        conn.commit()

        # closing the connection
        file_text.close()
        conn.close()

    except Exception as e:
        print(f"{file_name} does not exist!")
