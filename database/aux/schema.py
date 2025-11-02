def create_tables(conn):
    """Create all required tables if they don't exist."""
    queries = [
        """
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
        """,
        # we'll add the other two tables here next
    ]
    for query in queries:
        conn.execute(query)
