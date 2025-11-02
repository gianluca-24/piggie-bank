def insert_user(conn, name: str, email: str):
    conn.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    print(f"User '{name}' inserted successfully.")

def query_all_users(conn, condition: str = None):
    query = "SELECT * FROM users"
    if condition:
        query += f" WHERE {condition}"
    return conn.execute(query).fetchall()
