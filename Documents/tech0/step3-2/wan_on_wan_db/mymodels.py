from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text, DateTime, Boolean, Enum
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.sql import func
from datetime import datetime

# ベースクラスの定義
class Base(DeclarativeBase):
    pass

# テーブル定義
class User(Base):
    __tablename__ = 'user'
    user_id: Mapped[int] = mapped_column(primary_key=True)
    user_type: Mapped[str] = mapped_column(Enum('owner', 'visitor', name='user_types'))
    name: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()
    password: Mapped[str] = mapped_column()
    image: Mapped[str] = mapped_column()
    bio: Mapped[str] = mapped_column(Text)

    dogs = relationship("Dog", back_populates="owner", foreign_keys="[Dog.owner_user_id]")
    requests = relationship("Request", back_populates="owner", foreign_keys="[Request.owner_user_id]")
    visits = relationship("Request", back_populates="visitor", foreign_keys="[Request.visitor_user_id]")
    sent_feedbacks = relationship("Feedback", back_populates="sender", foreign_keys="[Feedback.sender_user_id]")
    received_feedbacks = relationship("Feedback", back_populates="receiver", foreign_keys="[Feedback.receiver_user_id]")

class Dog(Base):
    __tablename__ = 'dog'
    dog_id: Mapped[int] = mapped_column(primary_key=True)
    owner_user_id: Mapped[int] = mapped_column(ForeignKey('user.user_id'))
    image: Mapped[str] = mapped_column()
    dog_name: Mapped[str] = mapped_column()
    breed: Mapped[str] = mapped_column()
    dog_age: Mapped[int] = mapped_column()
    dog_sex: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column(Text)

    owner = relationship("User", back_populates="dogs")
    walks = relationship("Walk", back_populates="dog")

class Location(Base):
    __tablename__ = 'location'
    location_id: Mapped[int] = mapped_column(primary_key=True)
    location_name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column(Text)

    walks = relationship("Walk", back_populates="location")

class Walk(Base):
    __tablename__ = 'walk'
    walk_id: Mapped[int] = mapped_column(primary_key=True)
    owner_user_id: Mapped[int] = mapped_column(ForeignKey('user.user_id'))
    description: Mapped[str] = mapped_column(Text)
    time_start: Mapped[datetime] = mapped_column(DateTime)
    time_end: Mapped[datetime] = mapped_column(DateTime)
    location_id: Mapped[int] = mapped_column(ForeignKey('location.location_id'))

    owner = relationship("User", back_populates="walks")
    location = relationship("Location", back_populates="walks")
    messages = relationship("Message", back_populates="walk")
    feedbacks = relationship("Feedback", back_populates="walk")
    requests = relationship("Request", back_populates="walk")

class Request(Base):
    __tablename__ = 'request'
    request_id: Mapped[int] = mapped_column(primary_key=True)
    walk_id: Mapped[int] = mapped_column(ForeignKey('walk.walk_id'))
    owner_user_id: Mapped[int] = mapped_column(ForeignKey('user.user_id'))
    visitor_user_id: Mapped[int] = mapped_column(ForeignKey('user.user_id'))
    requested_time: Mapped[datetime] = mapped_column(DateTime)
    confirmed: Mapped[bool] = mapped_column(Boolean)
    timestamp: Mapped[datetime] = mapped_column(DateTime, default=func.now())

    walk = relationship("Walk", back_populates="requests")
    owner = relationship("User", foreign_keys=[owner_user_id], back_populates="requests")
    visitor = relationship("User", foreign_keys=[visitor_user_id], back_populates="visits")

class Message(Base):
    __tablename__ = 'message'
    message_id: Mapped[int] = mapped_column(primary_key=True)
    walk_id: Mapped[int] = mapped_column(ForeignKey('walk.walk_id'))
    sender_user_id: Mapped[int] = mapped_column(ForeignKey('user.user_id'))
    receiver_user_id: Mapped[int] = mapped_column(ForeignKey('user.user_id'))
    message: Mapped[str] = mapped_column(Text)
    timestamp: Mapped[datetime] = mapped_column(DateTime, default=func.now())

    walk = relationship("Walk", back_populates="messages")
    sender = relationship("User", foreign_keys=[sender_user_id])
    receiver = relationship("User", foreign_keys=[receiver_user_id])

class Feedback(Base):
    __tablename__ = 'feedback'
    feedback_id: Mapped[int] = mapped_column(primary_key=True)
    sender_user_id: Mapped[int] = mapped_column(ForeignKey('user.user_id'))
    receiver_user_id: Mapped[int] = mapped_column(ForeignKey('user.user_id'))
    walk_id: Mapped[int] = mapped_column(ForeignKey('walk.walk_id'))
    rating: Mapped[int] = mapped_column()
    comments: Mapped[str] = mapped_column(Text)
    timestamp: Mapped[datetime] = mapped_column(DateTime, default=func.now())

    sender = relationship("User", foreign_keys=[sender_user_id], back_populates="sent_feedbacks")
    receiver = relationship("User", foreign_keys=[receiver_user_id], back_populates="received_feedbacks")
    walk = relationship("Walk", back_populates="feedbacks")
