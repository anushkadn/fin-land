from flask import Flask, render_template, request, redirect, url_for
from models import init_db, add_transaction, get_transactions

app = Flask(__name__)

@app.route('/')
def index():
    transactions = get_transactions()
    return render_template('index.html', transactions=transactions)

@app.route('/add', methods=['GET', 'POST'])
def add_transaction_route():
    if request.method == 'POST':
        description = request.form['description']
        amount = request.form['amount']
        date = request.form['date']
        add_transaction(description, amount, date)
        return redirect(url_for('index'))
    return render_template('add_transaction.html')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
