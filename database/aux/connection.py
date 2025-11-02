import os
import sqlite3

def get_connection(db_name="piggie.db"):
    """Return a connection to the database located in the project root."""
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    db_path = os.path.join(root_dir, db_name)
    connection = sqlite3.connect(db_path)
    return connection