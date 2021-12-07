from w2eat.db.create_table import create_table
from w2eat.db.insert_field import insert_field
import os


def main():
    # print ("Testing...")
    pass


create_table("food_type", "name")
insert_field("food_type", "name", "food_category.txt")
