CREATE TABLE rooms (
  id INT PRIMARY KEY,
  room_number INT,
  room_type VARCHAR(255),
  price DECIMAL(10, 2),
  description TEXT
);

CREATE TABLE bookings (
  id INT PRIMARY KEY,
  room_id INT,
  guest_name VARCHAR(255),
  arrival_date DATE,
  departure_date DATE,
  total_cost DECIMAL(10, 2),
  FOREIGN KEY (room_id) REFERENCES rooms(id)
);

CREATE TABLE amenities (
  id INT PRIMARY KEY,
  name VARCHAR(255),
  description TEXT
);

CREATE TABLE room_amenities (
  room_id INT,
  amenity_id INT,
  FOREIGN KEY (room_id) REFERENCES rooms(id),
  FOREIGN KEY (amenity_id) REFERENCES amenities(id)
);