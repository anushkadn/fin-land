from flask import Flask, render_template, request, redirect, url_for
from models import init_db, add_transaction, get_transactions, get_transaction_by_id, update_transaction, delete_transaction

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

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_transaction_route(id):
    if request.method == 'POST':
        description = request.form['description']
        amount = request.form['amount']
        date = request.form['date']
        update_transaction(id, description, amount, date)
        return redirect(url_for('index'))
    transaction = get_transaction_by_id(id)
    return render_template('edit_transaction.html', transaction=transaction)

@app.route('/delete/<int:id>')
def delete_transaction_route(id):
    delete_transaction(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
