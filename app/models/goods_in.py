from datetime import datetime

from app.extensions import db


class GoodsIn(db.Model):
    __tablename__ = "goods_in"

    id = db.Column(db.Integer, primary_key=True)

    reference_no = db.Column(
        db.String(100),
        unique=True,
        nullable=False
    )

    supplier_id = db.Column(
        db.Integer,
        db.ForeignKey("suppliers.id"),
        nullable=False
    )

    container_number = db.Column(db.String(100))

    truck_number = db.Column(db.String(100))

    driver_name = db.Column(db.String(100))

    received_by = db.Column(db.String(100))

    received_date = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    remarks = db.Column(db.Text)

    items = db.relationship(
        "GoodsInItem",
        backref="goods_in",
        lazy=True,
        cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"<GoodsIn {self.reference_no}>"


class GoodsInItem(db.Model):
    __tablename__ = "goods_in_items"

    id = db.Column(db.Integer, primary_key=True)

    goods_in_id = db.Column(
        db.Integer,
        db.ForeignKey("goods_in.id"),
        nullable=False
    )

    product_id = db.Column(
        db.Integer,
        db.ForeignKey("products.id"),
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
        return f"<GoodsInItem {self.id}>"
