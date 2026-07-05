from datetime import datetime

from app.extensions import db


class GoodsOut(db.Model):
    __tablename__ = "goods_out"

    id = db.Column(db.Integer, primary_key=True)

    reference_no = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    customer_id = db.Column(
        db.Integer,
        db.ForeignKey("customers.id"),
        nullable=False
    )

    truck_number = db.Column(db.String(100))

    driver_name = db.Column(db.String(100))

    issued_by = db.Column(db.String(100))

    issued_date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    remarks = db.Column(db.Text)

    items = db.relationship(
        "GoodsOutItem",
        backref="goods_out",
        lazy=True,
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<GoodsOut {self.reference_no}>"


class GoodsOutItem(db.Model):
    __tablename__ = "goods_out_items"

    id = db.Column(db.Integer, primary_key=True)

    goods_out_id = db.Column(
        db.Integer,
        db.ForeignKey("goods_out.id"),
        nullable=False
    )

    batch_id = db.Column(
        db.Integer,
        db.ForeignKey("batches.id"),
        nullable=False
    )

    quantity = db.Column(
        db.Integer,
        nullable=False
    )

    def __repr__(self):
        return f"<GoodsOutItem {self.id}>"
