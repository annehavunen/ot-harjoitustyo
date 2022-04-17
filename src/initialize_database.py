from database_connection import get_database_connection


def drop_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        DROP TABLE IF EXISTS Recipe;
    ''')

    #testausta
    cursor.execute('''
        DROP TABLE IF EXISTS Category;
    ''')

    connection.commit()

def create_tables(connection):
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE Recipe (
            name TEXT,
            url TEXT
        );
    ''')

# Testaa ensin: kategoria ilman mitään muuta
    cursor.execute('''
        CREATE TABLE Category (
            name TEXT
        );
    ''')

    # cursor.execute('''
    #     CREATE TABLE Recipe (
    #         id INTEGER PRIMARY KEY,
    #         name TEXT,
    #         url TEXT
    #     );
    # ''')

    connection.commit()


def initialize_database():
    connection = get_database_connection()

    drop_tables(connection)
    create_tables(connection)
