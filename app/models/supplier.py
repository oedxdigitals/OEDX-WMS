from app.extensions import db


class Supplier(db.Model):
    __tablename__ = "suppliers"

    id = db.Column(db.Integer, primary_key=True)

    company_name = db.Column(
        db.String(150),
        nullable=False
    )

    contact_person = db.Column(db.String(100))

    phone = db.Column(db.String(50))

    email = db.Column(db.String(100))

    address = db.Column(db.Text)

    goods_in = db.relationship(
        "GoodsIn",
        backref="supplier",
        lazy=True
    )

    batches = db.relationship(
        "Batch",
        backref="supplier",
        lazy=True
    )

    def __repr__(self):
        return f"<Supplier {self.company_name}>"
