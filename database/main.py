import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.aux import *

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
