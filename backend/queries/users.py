import uuid

def insert_user(conn, user):
    print(f"🔄 Inserting user '{user.name}' into the database...")
    # Use dictionary-style access
    name = user.name
    surname = user.surname
    birthday = user.birthday
    email = user.email
    password = user.password

    user_id = str(uuid.uuid4())

    conn.execute(
        "INSERT INTO users (user_id, name, surname, birthday, email, password) VALUES (?, ?, ?, ?, ?, ?)",
        (user_id, name, surname, birthday, email, password),
    )
    conn.commit()
    print(f"✅ User '{name}' inserted successfully.")

def create_table_user(conn):
    """Create users table if it does not exist."""
    query ="""
            CREATE TABLE IF NOT EXISTS users (
            user_id TEXT PRIMARY KEY,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            birthday TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
        """
    conn.execute(query)

def get_user_by_email(conn, email):
    """Retrieve a user by email."""
    cursor = conn.execute("SELECT * FROM users WHERE email = ?", (email,))
    row = cursor.fetchone()
    if row:
        return {
            "user_id": row[0],
            "name": row[1],
            "email": row[4],
        }
    return None