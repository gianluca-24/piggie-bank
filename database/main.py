import sys, os
from datetime import datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from database.aux import *

def main():
    conn = get_connection()
    try:
        create_tables(conn)

        # # --- USERS ---
        # insert_user(conn, "Suzy", "suzy2@gmail.com")
        # print(read_users(conn))

        # update_user(conn, 1, name="Suzy B.")
        # print(read_users(conn, 1))

        # # --- BANK ACCOUNTS ---
        # insert_bank_account(conn, 1, "Chase", "Checking", "checking", "USD", 1200.00)
        # print(read_bank_accounts(conn))

        # update_bank_account(conn, 1, balance=1600.00)
        # print(read_bank_accounts(conn, 1))

        # # --- TRANSACTIONS ---
        # insert_transaction(
        #     conn,
        #     account_id=1,
        #     user_id=1,
        #     amount=-5.25,
        #     date=datetime.now().isoformat(),
        #     is_income=False,
        #     merchant_name="Starbucks",
        #     category="Food & Drink",
        #     sub_category="Coffee",
        #     description="Latte"
        # )

        # print(read_transactions(conn))
        # update_transaction(conn, 1, category="Cafes", description="Updated description")
        # print(read_transactions(conn, 1))

        # # Clean up test data 
        # delete_transaction(conn, 1)
        # delete_bank_account(conn, 1)
        # delete_user(conn, 1)

    finally:
        conn.close()

if __name__ == "__main__":
    main()
