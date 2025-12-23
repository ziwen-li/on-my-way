from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class TravelOffer(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    from_country = db.Column(db.String(50), nullable=False)
    from_city = db.Column(db.String(50), nullable=True)

    to_country = db.Column(db.String(50), nullable=False)
    to_city = db.Column(db.String(50), nullable=True)

    travel_date = db.Column(db.String(50), nullable=False)

    available_weight = db.Column(db.Float, nullable=False)
    item_type = db.Column(db.String(100), nullable=False)

    reward = db.Column(db.String(100), nullable=False)

    contact = db.Column(db.String(100), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class DeliveryRequest(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    from_country = db.Column(db.String(50), nullable=False)
    to_country = db.Column(db.String(50), nullable=False)

    item_description = db.Column(db.String(200), nullable=False)
    weight = db.Column(db.Float, nullable=False)

    desired_date = db.Column(db.String(50), nullable=False)
    budget = db.Column(db.String(100), nullable=False)

    contact = db.Column(db.String(100), nullable=False)

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
