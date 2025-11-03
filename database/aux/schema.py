def create_table_user(conn):
    """Create users table if it does not exist."""
    query ="""
            CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            surname TEXT NOT NULL,
            birthday TIMESTAMP NOT NULL,
            email TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL
        )
        """
    conn.execute(query)

def create_table_bank_account(conn):
    """Create bankaccounts table if it does not exist."""
    query = """
        CREATE TABLE IF NOT EXISTS bank_accounts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            institution_name TEXT NOT NULL,
            account_name TEXT NOT NULL,
            plaid_account_id TEXT,
            account_type TEXT NOT NULL,
            balance REAL NOT NULL DEFAULT 0,
            currency TEXT NOT NULL,
            last_sync TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users (id)
        )
        """
    conn.execute(query)

def create_table_transactions(conn):
    """Create the transactions table if it does not exist."""
    query = """
    CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        account_id INTEGER NOT NULL,
        user_id INTEGER NOT NULL,
        plaid_transaction_id TEXT,
        date TIMESTAMP NOT NULL,
        amount REAL NOT NULL,
        currency TEXT,
        merchant_name TEXT,
        description TEXT,
        category TEXT,
        sub_category TEXT,
        is_income BOOLEAN NOT NULL CHECK (is_income IN (0, 1)),
        source TEXT NOT NULL DEFAULT 'manual',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (account_id) REFERENCES bank_accounts (id),
        FOREIGN KEY (user_id) REFERENCES users (id)
    );
    """
    conn.execute(query)

def create_tables(conn):
    """Create all tables in the database."""
    create_table_user(conn)
    create_table_bank_account(conn)
    create_table_transactions(conn)
