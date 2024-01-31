import sqlite3
from datetime import datetime

class Appointment:
    def _init_(self, patient_name, doctor_name, appointment_date):
        self.patient_name = patient_name
        self.doctor_name = doctor_name
        self.appointment_date = appointment_date

def create_table():
    conn = sqlite3.connect('appointments.db')
    cursor = conn.cursor()

    # Creating the 'appointments' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            patient_name TEXT,
            doctor_name TEXT,
            appointment_date DATETIME
        )
    ''')

    conn.commit()
    conn.close()

def display_appointments():
    conn = sqlite3.connect('appointments.db')
    cursor = conn.cursor()

    # Fetching appointments from the database
    cursor.execute('SELECT * FROM appointments')
    appointments = cursor.fetchall()

    conn.close()

    if not appointments:
        print("No appointments scheduled.")
        return

    for idx, appointment in enumerate(appointments, start=1):
        print(f"{idx}. {appointment[1]} with Dr. {appointment[2]} on {appointment[3]}")

def book_appointment():
    patient_name = input("Enter patient name: ")
    doctor_name = input("Enter doctor name: ")
    appointment_date_str = input("Enter appointment date and time (YYYY-MM-DD HH:MM): ")

    try:
        appointment_date = datetime.strptime(appointment_date_str, '%Y-%m-%d %H:%M')
    except ValueError:
        print("Invalid date and time format. Please use the format YYYY-MM-DD HH:MM.")
        return

    conn = sqlite3.connect('appointments.db')
    cursor = conn.cursor()

    # Inserting a new appointment into the database
    cursor.execute('INSERT INTO appointments (patient_name, doctor_name, appointment_date) VALUES (?, ?, ?)',
                   (patient_name, doctor_name, appointment_date))

    conn.commit()
    conn.close()

    print("Appointment booked successfully.")

def main():
    create_table()

    while True:
        print("\nMedical Appointment Booking System")
        print("1. View Appointments")
        print("2. Book Appointment")
        print("3. Exit")

        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            display_appointments()
        elif choice == '2':
            book_appointment()
        elif choice == '3':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()