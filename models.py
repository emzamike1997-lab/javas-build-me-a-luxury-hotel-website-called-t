from sqlalchemy import create_engine, Column, Integer, String, Float, Date, Text, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('postgresql://user:password@localhost/dbname')
Base = declarative_base()

class User(Base):
  __tablename__ = 'users'
  id = Column(Integer, primary_key=True)
  username = Column(String, nullable=False)
  email = Column(String, nullable=False)
  password = Column(String, nullable=False)
  bookings = relationship('Booking', backref='user')

class Room(Base):
  __tablename__ = 'rooms'
  id = Column(Integer, primary_key=True)
  room_number = Column(Integer, nullable=False)
  room_type = Column(String, nullable=False)
  price = Column(Float, nullable=False)
  description = Column(Text, nullable=False)
  bookings = relationship('Booking', backref='room')

class Booking(Base):
  __tablename__ = 'bookings'
  id = Column(Integer, primary_key=True)
  user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
  room_id = Column(Integer, ForeignKey('rooms.id'), nullable=False)
  check_in = Column(Date, nullable=False)
  check_out = Column(Date, nullable=False)
  total_cost = Column(Float, nullable=False)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()