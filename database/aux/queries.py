from datetime import datetime

# ===================
# users table queries
# ===================
def insert_user(conn, name: str, email: str):
    conn.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
    print(f"User '{name}' inserted successfully.")

def read_users(conn, user_id: int = None):
    if user_id:
        return conn.execute("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()
    return conn.execute("SELECT * FROM users").fetchall()


def update_user(conn, user_id: int, name: str = None, email: str = None):
    if name:
        conn.execute("UPDATE users SET name = ? WHERE id = ?", (name, user_id))
    if email:
        conn.execute("UPDATE users SET email = ? WHERE id = ?", (email, user_id))
    conn.commit()
    print(f"Updated user ID {user_id}")


def delete_user(conn, user_id: int):
    conn.execute("DELETE FROM users WHERE id = ?", (user_id,))
    conn.commit()
    print(f"Deleted user ID {user_id}")

# ==========================
# bank account table queries
# ==========================
def insert_bank_account(conn, user_id: int, institution_name: str, account_name: str,
                        account_type: str, currency: str, balance: float = 0.0,
                        plaid_account_id: str = None):
    conn.execute("""
        INSERT INTO bank_accounts 
        (user_id, institution_name, account_name, account_type, currency, balance, plaid_account_id)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (user_id, institution_name, account_name, account_type, currency, balance, plaid_account_id))
    print(f"Bank account '{account_name}' inserted successfully.")

def read_bank_accounts(conn, account_id: int = None, user_id: int = None):
    if account_id:
        return conn.execute("SELECT * FROM bank_accounts WHERE id = ?", (account_id,)).fetchone()
    if user_id:
        return conn.execute("SELECT * FROM bank_accounts WHERE user_id = ?", (user_id,)).fetchall()
    return conn.execute("SELECT * FROM bank_accounts").fetchall()


def update_bank_account(conn, account_id: int, balance: float = None, last_sync: str = None):
    if balance is not None:
        conn.execute("UPDATE bank_accounts SET balance = ? WHERE id = ?", (balance, account_id))
    if last_sync:
        conn.execute("UPDATE bank_accounts SET last_sync = ? WHERE id = ?", (last_sync, account_id))
    conn.commit()
    print(f"Updated bank account ID {account_id}")


def delete_bank_account(conn, account_id: int):
    conn.execute("DELETE FROM bank_accounts WHERE id = ?", (account_id,))
    conn.commit()
    print(f"Deleted bank account ID {account_id}")


# ==========================
# transactions table queries
# ==========================
def insert_transaction(conn, account_id: int, user_id: int, amount: float, date: str,
                       is_income: bool, source: str = "manual", description: str = None,
                       category: str = None, sub_category: str = None,
                       merchant_name: str = None, currency: str = None,
                       plaid_transaction_id: str = None):
    conn.execute("""
        INSERT INTO transactions
        (account_id, user_id, amount, date, is_income, source, description,
         category, sub_category, merchant_name, currency, plaid_transaction_id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (account_id, user_id, amount, date, int(is_income), source, description,
          category, sub_category, merchant_name, currency, plaid_transaction_id))
    print(f"Transaction of {amount} inserted successfully.")

def read_transactions(conn, transaction_id: int = None, user_id: int = None, account_id: int = None):
    if transaction_id:
        return conn.execute("SELECT * FROM transactions WHERE id = ?", (transaction_id,)).fetchone()
    if user_id:
        return conn.execute("SELECT * FROM transactions WHERE user_id = ?", (user_id,)).fetchall()
    if account_id:
        return conn.execute("SELECT * FROM transactions WHERE account_id = ?", (account_id,)).fetchall()
    return conn.execute("SELECT * FROM transactions").fetchall()


def update_transaction(conn, transaction_id: int, **fields):
    """Dynamically update one or more fields in a transaction."""
    if not fields:
        print("No fields provided for update.")
        return
    columns = ", ".join([f"{k} = ?" for k in fields])
    values = list(fields.values()) + [transaction_id]
    conn.execute(f"UPDATE transactions SET {columns}, updated_at = CURRENT_TIMESTAMP WHERE id = ?", values)
    conn.commit()
    print(f"Updated transaction ID {transaction_id}")


def delete_transaction(conn, transaction_id: int):
    conn.execute("DELETE FROM transactions WHERE id = ?", (transaction_id,))
    conn.commit()
    print(f"Deleted transaction ID {transaction_id}")
