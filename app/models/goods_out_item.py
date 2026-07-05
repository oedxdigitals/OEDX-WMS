from app.extensions import db


class GoodsOutItem(db.Model):
    __tablename__ = "goods_out_items"

    id = db.Column(
        db.Integer,
        primary_key=True
    )

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
