from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

def get_db():
    return sqlite3.connect("flights.db")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    origin = request.form['origin']
    dest = request.form['dest']
    start = request.form['start_date']
    end = request.form['end_date']

    with get_db() as conn:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT f.flight_number, f.departure_date, 
                fs.origin_code, fs.dest_code, fs.departure_time
            FROM Flight f
            JOIN FlightService fs ON f.flight_number = fs.flight_number
            WHERE fs.origin_code=? AND fs.dest_code=? 
            AND f.departure_date BETWEEN ? AND ?
        """, (origin, dest, start, end))

        flights = cursor.fetchall()

    return render_template('flights.html', flights=flights)

@app.route('/flight/<flight_number>/<departure_date>')
def flight_detail(flight_number, departure_date):
    with get_db() as conn:
        cursor = conn.cursor()

        cursor.execute("""
            SELECT a.capacity - COUNT(b.seat_number), a.capacity
            FROM Flight f
            JOIN Aircraft a ON f.plane_type = a.plane_type
            LEFT JOIN Booking b
            ON f.flight_number=b.flight_number
            AND f.departure_date=b.departure_date
            WHERE f.flight_number=? AND f.departure_date=?
            GROUP BY a.capacity
        """, (flight_number, departure_date))

        result = cursor.fetchone()

    return render_template('flight_detail.html',
                           available=result[0],
                           capacity=result[1])

if __name__ == '__main__':
    app.run(debug=True)