from sqlalchemy import create_engine, Column, Integer, String, Date, Decimal, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('postgresql://user:password@host:port/dbname')
Base = declarative_base()

class Room(Base):
  __tablename__ = 'rooms'
  id = Column(Integer, primary_key=True)
  room_number = Column(Integer)
  room_type = Column(String)
  price = Column(Decimal)
  description = Column(Text)
  bookings = relationship('Booking', backref='room')
  amenities = relationship('Amenity', secondary='room_amenities', backref='rooms')

class Booking(Base):
  __tablename__ = 'bookings'
  id = Column(Integer, primary_key=True)
  room_id = Column(Integer, ForeignKey('rooms.id'))
  guest_name = Column(String)
  arrival_date = Column(Date)
  departure_date = Column(Date)
  total_cost = Column(Decimal)

class Amenity(Base):
  __tablename__ = 'amenities'
  id = Column(Integer, primary_key=True)
  name = Column(String)
  description = Column(Text)

Base.metadata.create_all(engine)