import sqlite3

def init_db():
    conn = sqlite3.connect('finance_tracker.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions
                      (id INTEGER PRIMARY KEY AUTOINCREMENT, description TEXT, amount REAL, date TEXT)''')
    conn.commit()
    conn.close()

def add_transaction(description, amount, date):
    conn = sqlite3.connect('finance_tracker.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO transactions (description, amount, date) VALUES (?, ?, ?)",
                   (description, amount, date))
    conn.commit()
    conn.close()

def get_transactions():
    conn = sqlite3.connect('finance_tracker.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions")
    transactions = cursor.fetchall()
    conn.close()
    return transactions

def get_transaction_by_id(id):
    conn = sqlite3.connect('finance_tracker.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM transactions WHERE id = ?", (id,))
    transaction = cursor.fetchone()
    conn.close()
    return transaction

def update_transaction(id, description, amount, date):
    conn = sqlite3.connect('finance_tracker.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE transactions SET description = ?, amount = ?, date = ? WHERE id = ?",
                   (description, amount, date, id))
    conn.commit()
    conn.close()

def delete_transaction(id):
    conn = sqlite3.connect('finance_tracker.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM transactions WHERE id = ?", (id,))
    conn.commit()
    conn.close()
