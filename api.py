from flask import Flask, jsonify, request
from models import engine, Room, Booking, Amenity, sessionmaker

app = Flask(__name__)
Session = sessionmaker(bind=engine)
session = Session()

@app.route('/rooms', methods=['GET'])
def get_rooms():
  rooms = session.query(Room).all()
  return jsonify([room.__dict__ for room in rooms])

@app.route('/bookings', methods=['GET'])
def get_bookings():
  bookings = session.query(Booking).all()
  return jsonify([booking.__dict__ for booking in bookings])

@app.route('/amenities', methods=['GET'])
def get_amenities():
  amenities = session.query(Amenity).all()
  return jsonify([amenity.__dict__ for amenity in amenities])

@app.route('/bookings', methods=['POST'])
def create_booking():
  data = request.get_json()
  booking = Booking(room_id=data['room_id'], guest_name=data['guest_name'], arrival_date=data['arrival_date'], departure_date=data['departure_date'], total_cost=data['total_cost'])
  session.add(booking)
  session.commit()
  return jsonify(booking.__dict__)

@app.route('/rooms/<int:room_id>/amenities', methods=['GET'])
def get_room_amenities(room_id):
  room = session.query(Room).filter_by(id=room_id).first()
  amenities = room.amenities
  return jsonify([amenity.__dict__ for amenity in amenities])

if __name__ == '__main__':
  app.run(debug=True)