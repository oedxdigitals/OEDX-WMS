from app.extensions import db


class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)

    company_name = db.Column(
        db.String(150),
        nullable=False
    )

    contact_person = db.Column(db.String(100))

    phone = db.Column(db.String(50))

    email = db.Column(db.String(100))

    address = db.Column(db.Text)

    goods_out = db.relationship(
        "GoodsOut",
        backref="customer",
        lazy=True
    )

    def __repr__(self):
        return f"<Customer {self.company_name}>"
