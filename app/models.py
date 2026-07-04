from datetime import datetime

from .extensions import db

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    username = db.Column(db.String(80), unique=True, nullable=False)

    password = db.Column(db.String(255), nullable=False)

    fullname = db.Column(db.String(150))

    role = db.Column(db.String(30), default="warehouse")

    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(150), nullable=False)

    sku = db.Column(db.String(50), unique=True)

    category = db.Column(db.String(100))

    unit = db.Column(db.String(30))

    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    batches = db.relationship("Batch", backref="product", lazy=True)


class Batch(db.Model):
    __tablename__ = "batches"

    id = db.Column(db.Integer, primary_key=True)

    batch_number = db.Column(db.String(100), unique=True, nullable=False)

    quantity = db.Column(db.Integer, default=0)

    expiry_date = db.Column(db.Date)

    product_id = db.Column(
        db.Integer,
        db.ForeignKey("products.id"),
        nullable=False,
    )

    created_at = db.Column(db.DateTime, default=datetime.utcnow)
