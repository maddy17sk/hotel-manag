# app.py
from flask import Flask, render_template, request, redirect, url_for
from database import create_database
from crud_operations import create_reservation, read_reservations, update_reservation, delete_reservation

app = Flask(__name__)

# Ensure the database and tables are created
create_database()

@app.route('/')
def index():
    reservations = read_reservations()
    return render_template('index.html', reservations=reservations)

@app.route('/add', methods=['POST'])
def add_reservation():
    guest_name = request.form['guest_name']
    room_type = request.form['room_type']
    check_in_date = request.form['check_in_date']
    check_out_date = request.form['check_out_date']
    create_reservation(guest_name, room_type, check_in_date, check_out_date)
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['POST'])
def update_reservation_route(id):
    guest_name = request.form['guest_name']
    room_type = request.form['room_type']
    check_in_date = request.form['check_in_date']
    check_out_date = request.form['check_out_date']
    update_reservation(id, guest_name, room_type, check_in_date, check_out_date)
    return redirect(url_for('index'))

@app.route('/test', methods=['POST'])
def test_route():
    print("Test route triggered")
    return "Test successful", 200


@app.route('/delete/<int:id>')
def delete_reservation_route(id):
    delete_reservation(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
