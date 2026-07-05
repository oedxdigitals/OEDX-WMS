from datetime import datetime

from app.extensions import db


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(
        db.String(150),
        nullable=False
    )

    sku = db.Column(
        db.String(100),
        unique=True
    )

    barcode = db.Column(
        db.String(100),
        unique=True
    )

    category_id = db.Column(
        db.Integer,
        db.ForeignKey("categories.id")
    )

    brand = db.Column(
        db.String(100)
    )

    unit = db.Column(
        db.String(30)
    )

    minimum_stock = db.Column(
        db.Integer,
        default=0
    )

    description = db.Column(
        db.Text
    )

    status = db.Column(
        db.String(20),
        default="Active"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    batches = db.relationship(
        "Batch",
        backref="product",
        lazy=True,
        cascade="all, delete-orphan"
    )

    goods_in_items = db.relationship(
        "GoodsInItem",
        backref="product",
        lazy=True
    )

    def __repr__(self):
        return f"<Product {self.name}>"
