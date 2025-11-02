import os
import sqlite3

# Setup/ initialize the database 
def get_connection(db_name="app_database.db"): 
     # get the directory of this script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # move up one level (to project root)
    root_dir = os.path.dirname(script_dir)
    # join root path with database name
    db_path = os.path.join(root_dir, db_name)

    conn = sqlite3.connect(db_path)
    return conn

# Create tables in the database (user table)
def create_tables(connection):
    query = """ 
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE
    )
    """
    connection.execute(query)

# Insert user
def insert_user(connection, name:str, email:str):
    query = "INSERT INTO users (name, email) VALUES (?, ?)"
    connection.execute(query, (name, email))
    print(f"User {name} inserted successfully.")


# Query all Users in the database
def query_all_users(connection, condition:str=None) -> list[tuple]:
    query = "SELECT * FROM users"
    if condition:
        query += f" WHERE {condition}"
    users = connection.execute(query).fetchall()
    return users



# Main function wrapper
def main():
    connection = get_connection()

    try:
        create_tables(connection)
        name = "Suzy"
        email = "Suzy@gmail.com"
        insert_user(connection, name, email)

        # Query all users
        print("All users in the database:")
        for user in query_all_users(connection):
            print(user)
    finally:
        connection.close()


if __name__ == "__main__":
    main()