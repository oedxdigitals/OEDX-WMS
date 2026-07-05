from datetime import datetime

from app.extensions import db


class GoodsOut(db.Model):
    __tablename__ = "goods_out"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

    reference_no = db.Column(
        db.String(100),
        unique=True
    )

    customer_id = db.Column(
        db.Integer,
        db.ForeignKey("customers.id"),
        nullable=False
    )

    truck_number = db.Column(
        db.String(100)
    )

    driver_name = db.Column(
        db.String(100)
    )

    issued_by = db.Column(
        db.String(100)
    )

    issued_date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    remarks = db.Column(
        db.Text
    )

    items = db.relationship(
        "GoodsOutItem",
        backref="goods_out",
        cascade="all, delete-orphan",
        lazy=True
    )
