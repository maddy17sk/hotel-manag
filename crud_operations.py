# crud_operations.py
from database import get_connection

def create_reservation(guest_name, room_type, check_in_date, check_out_date):
    """Create a new reservation in the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO reservations (guest_name, room_type, check_in_date, check_out_date)
        VALUES (?, ?, ?, ?)
    ''', (guest_name, room_type, check_in_date, check_out_date))
    conn.commit()
    conn.close()
    print("Reservation created successfully.")

def read_reservations():
    """Retrieve all reservations from the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM reservations")
    rows = cursor.fetchall()
    conn.close()
    return rows

def update_reservation(reservation_id, guest_name, room_type, check_in_date, check_out_date):
    """Update an existing reservation."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE reservations
        SET guest_name = ?, room_type = ?, check_in_date = ?, check_out_date = ?
        WHERE id = ?
    ''', (guest_name, room_type, check_in_date, check_out_date, reservation_id))
    conn.commit()
    conn.close()
    print("Reservation updated successfully.")

def delete_reservation(reservation_id):
    """Delete a reservation from the database."""
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM reservations WHERE id = ?", (reservation_id,))
    conn.commit()
    conn.close()
    print("Reservation deleted successfully.")
