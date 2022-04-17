from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE IF EXISTS Recipe;
    ''')

    cursor.execute('''
        DROP TABLE IF EXISTS Category;
    ''')

    cursor.execute('''
        DROP TABLE IF EXISTS Recipe_category
    ''')

    connection.commit()

def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE Recipe (
            id INTEGER PRIMARY KEY,
            name TEXT,
            url TEXT
        );
    ''')

    cursor.execute('''
        CREATE TABLE Category (
            id INTEGER PRIMARY KEY,
            name TEXT
        );
    ''')

    cursor.execute('''
        CREATE TABLE Recipe_category (
            recipe_id INTEGER REFERENCES Recipe,
            category_id INTEGER REFERENCES Category
        );
    ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)
