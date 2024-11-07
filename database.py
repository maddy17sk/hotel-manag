# database.py
import sqlite3

def get_connection():
    """Establish a connection to the SQLite database."""
    return sqlite3.connect('hotel_management.db')

def create_database():
    """Create the reservations table if it does not already exist."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reservations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            guest_name TEXT NOT NULL,
            room_type TEXT NOT NULL,
            check_in_date TEXT NOT NULL,
            check_out_date TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()
