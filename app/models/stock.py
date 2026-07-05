from datetime import datetime

from app.extensions import db


class StockMovement(db.Model):
    __tablename__ = "stock_movements"

    id = db.Column(db.Integer, primary_key=True)

    batch_id = db.Column(
        db.Integer,
        db.ForeignKey("batches.id"),
        nullable=False
    )

    movement_type = db.Column(
        db.String(20),
        nullable=False
    )  # IN, OUT, ADJUSTMENT

    reference_type = db.Column(
        db.String(50)
    )

    reference_id = db.Column(
        db.Integer
    )

    quantity = db.Column(
        db.Integer,
        nullable=False
    )

    balance = db.Column(
        db.Integer,
        nullable=False
    )

    user_id = db.Column(
        db.Integer,
        db.ForeignKey("users.id")
    )

    created_at = db.Column(
        db.DateTime,
        default=datetime.utcnow
    )

    def __repr__(self):
        return (
            f"<StockMovement "
            f"{self.movement_type} "
            f"{self.quantity}>"
        )
