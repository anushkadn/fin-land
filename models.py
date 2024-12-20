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
