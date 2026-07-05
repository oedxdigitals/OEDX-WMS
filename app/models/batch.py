from datetime import datetime

from app.extensions import db


class Batch(db.Model):
    __tablename__ = "batches"

    id = db.Column(db.Integer, primary_key=True)

    product_id = db.Column(
        db.Integer,
        db.ForeignKey("products.id"),
        nullable=False
    )

    supplier_id = db.Column(
        db.Integer,
        db.ForeignKey("suppliers.id")
    )

    batch_number = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    manufacture_date = db.Column(
        db.Date
    )

    expiry_date = db.Column(
        db.Date
    )

    quantity = db.Column(
        db.Integer,
        nullable=False,
        default=0
    )

    warehouse_location = db.Column(
        db.String(100)
    )

    status = db.Column(
        db.String(30),
        default="Available"
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    goods_in_items = db.relationship(
        "GoodsInItem",
        backref="batch",
        lazy=True
    )

    goods_out_items = db.relationship(
        "GoodsOutItem",
        backref="batch",
        lazy=True
    )

    stock_movements = db.relationship(
        "StockMovement",
        backref="batch",
        lazy=True,
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<Batch {self.batch_number}>"
