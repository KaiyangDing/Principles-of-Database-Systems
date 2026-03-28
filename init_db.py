import sqlite3

sql_script = """
-- ==================
-- TABLE CREATION (SQLite)
-- ==================

CREATE TABLE Airport (
    airport_code TEXT PRIMARY KEY,
    name TEXT,
    city TEXT,
    country TEXT
);

CREATE TABLE Aircraft (
    plane_type TEXT PRIMARY KEY,
    capacity INTEGER
);

CREATE TABLE FlightService (
    flight_number TEXT PRIMARY KEY,
    airline_name TEXT,
    origin_code TEXT,
    dest_code TEXT,
    departure_time TEXT,
    duration INTEGER
);

CREATE TABLE Flight (
    flight_number TEXT,
    departure_date TEXT,
    plane_type TEXT,
    PRIMARY KEY (flight_number, departure_date)
);

CREATE TABLE Passenger (
    pid INTEGER PRIMARY KEY,
    passenger_name TEXT
);

CREATE TABLE Booking (
    pid INTEGER,
    flight_number TEXT,
    departure_date TEXT,
    seat_number INTEGER,
    PRIMARY KEY (pid, flight_number, departure_date)
);

-- ==================
-- DATA
-- ==================

INSERT INTO Airport VALUES
('JFK','John F Kennedy International','New York','United States'),
('LAX','Los Angeles International','Los Angeles','United States'),
('ORD','O''Hare International','Chicago','United States'),
('MDW','Midway International','Chicago','United States'),
('LHR','Heathrow Airport','London','United Kingdom'),
('CDG','Charles de Gaulle Airport','Paris','France'),
('ORY','Paris Orly Airport','Paris','France'),
('SFO','San Francisco International','San Francisco','United States'),
('MIA','Miami International','Miami','United States'),
('ATL','Hartsfield-Jackson International','Atlanta','United States'),
('NRT','Narita International','Tokyo','Japan'),
('SIN','Changi Airport','Singapore','Singapore');

INSERT INTO Aircraft VALUES
('CRJ-200',10),
('Boeing 737',20),
('Airbus A320',15),
('Boeing 787',25);

INSERT INTO FlightService VALUES
('AA101','American Airlines','JFK','LAX','08:00:00',210),
('AA205','American Airlines','JFK','LAX','14:00:00',210),
('UA302','United Airlines','SFO','ORD','09:00:00',360),
('DL410','Delta Air Lines','ATL','MIA','10:00:00',150),
('BA178','British Airways','LHR','JFK','10:00:00',180),
('AF023','Air France','CDG','NRT','22:00:00',1140),
('SQ321','Singapore Airlines','SIN','LHR','23:00:00',420),
('AA550','American Airlines','ORD','MIA','07:00:00',240),
('DL620','Delta Air Lines','JFK','ATL','16:00:00',150),
('UA789','United Airlines','LAX','SFO','12:00:00',90);

INSERT INTO Flight VALUES
('AA101','2025-12-29','Boeing 737'),
('AA101','2025-12-31','Boeing 737'),
('AA205','2025-12-31','Boeing 737'),
('UA302','2025-12-31','CRJ-200'),
('DL410','2025-12-31','Airbus A320'),
('BA178','2025-12-31','Boeing 787'),
('AF023','2025-12-30','Boeing 787'),
('SQ321','2025-12-30','Boeing 787'),
('DL620','2025-12-30','Airbus A320'),
('DL620','2025-12-31','Airbus A320'),
('AA550','2025-12-31','CRJ-200'),
('UA789','2025-12-31','Airbus A320');

INSERT INTO Passenger VALUES
(1,'John Adams'),(2,'Sarah Miller'),(3,'Michael Chen'),(4,'Emily Wong'),
(5,'David Park'),(6,'Lisa Johnson'),(7,'James Brown'),(8,'Maria Garcia'),
(9,'Robert Kim'),(10,'Jennifer Lee'),(11,'Thomas Wilson'),(12,'Amanda Clark'),
(13,'Christopher Davis'),(14,'Jessica Martinez'),(15,'Daniel Taylor'),
(16,'Rachel Anderson'),(17,'William Thomas'),(18,'Nicole White'),
(19,'Kevin Harris'),(20,'Stephanie Moore'),(21,'Andrew Jackson'),
(22,'Michelle Robinson'),(23,'Brian Lewis'),(24,'Laura Walker'),
(25,'Steven Hall');

INSERT INTO Booking VALUES
(1,'AA101','2025-12-29',1),(2,'AA101','2025-12-29',2),
(3,'AA101','2025-12-29',3),(4,'AA101','2025-12-29',4),
(5,'AA101','2025-12-29',5),

(1,'AA101','2025-12-31',1),(2,'AA101','2025-12-31',2),
(3,'AA101','2025-12-31',3),(4,'AA101','2025-12-31',4),
(5,'AA101','2025-12-31',5),(6,'AA101','2025-12-31',6),
(7,'AA101','2025-12-31',7),(8,'AA101','2025-12-31',8),
(9,'AA101','2025-12-31',9),(10,'AA101','2025-12-31',10),
(11,'AA101','2025-12-31',11),(12,'AA101','2025-12-31',12),
(13,'AA101','2025-12-31',13),(14,'AA101','2025-12-31',14),
(15,'AA101','2025-12-31',15);
"""

conn = sqlite3.connect("flights.db")
cursor = conn.cursor()
cursor.executescript(sql_script)
conn.commit()
conn.close()

print("Database created successfully!")