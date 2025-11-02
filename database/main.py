import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.connection import get_connection
from database.schema import create_tables
from database.queries import insert_user, query_all_users

def main():
    conn = get_connection()
    try:
        create_tables(conn)
        insert_user(conn, "Zanlu", "zanlu@gmail.com")

        print("\nAll users in the database:")
        for user in query_all_users(conn):
            print(user)
    finally:
        conn.commit()
        conn.close()

if __name__ == "__main__":
    main()
