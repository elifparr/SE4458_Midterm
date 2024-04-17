from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import bcrypt

db = SQLAlchemy()

class Subscriber(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    user_type = db.Column(db.String(10), nullable=False)  # 'normal' or 'admin'
    subscriber_number = db.Column(db.String(20), unique=True, nullable=False)
    hashed_password = db.Column(db.String(300), nullable=False)

class Bill(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subscriber_id = db.Column(db.Integer, db.ForeignKey('subscriber.id'), nullable=False)  # Change subscriber_number to subscriber_id
    month = db.Column(db.String(20), nullable=False)
    bill_total = db.Column(db.Float, nullable=False)
    payment_status = db.Column(db.String(20), nullable=False)


