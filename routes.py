from flask import Flask, request, jsonify
from models import session, User, Room, Booking

app = Flask(__name__)

@app.route('/users', methods=['GET', 'POST'])
def handle_users():
  if request.method == 'GET':
    users = session.query(User).all()
    return jsonify([user.username for user in users])
  elif request.method == 'POST':
    data = request.get_json()
    new_user = User(username=data['username'], email=data['email'], password=data['password'])
    session.add(new_user)
    session.commit()
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/rooms', methods=['GET', 'POST'])
def handle_rooms():
  if request.method == 'GET':
    rooms = session.query(Room).all()
    return jsonify([room.room_number for room in rooms])
  elif request.method == 'POST':
    data = request.get_json()
    new_room = Room(room_number=data['room_number'], room_type=data['room_type'], price=data['price'], description=data['description'])
    session.add(new_room)
    session.commit()
    return jsonify({'message': 'Room created successfully'}), 201

@app.route('/bookings', methods=['GET', 'POST'])
def handle_bookings():
  if request.method == 'GET':
    bookings = session.query(Booking).all()
    return jsonify([booking.id for booking in bookings])
  elif request.method == 'POST':
    data = request.get_json()
    new_booking = Booking(user_id=data['user_id'], room_id=data['room_id'], check_in=data['check_in'], check_out=data['check_out'], total_cost=data['total_cost'])
    session.add(new_booking)
    session.commit()
    return jsonify({'message': 'Booking created successfully'}), 201

if __name__ == '__main__':
  app.run(debug=True)