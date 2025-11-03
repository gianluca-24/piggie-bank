import os
import sqlite3

def get_connection(db_name="piggie.db"):
    """Return a connection to the database located in the /database folder at the project root."""
    # Get the project root (one level above 'backend')
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    # Build path to /database/piggie.db
    db_dir = os.path.join(root_dir, "database")
    os.makedirs(db_dir, exist_ok=True)  # Create folder if it doesn't exist

    db_path = os.path.join(db_dir, db_name)

    connection = sqlite3.connect(db_path)
    return connection