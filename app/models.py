from datetime import datetime

from app.extensions import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    fullname = db.Column(db.String(150))
    role = db.Column(db.String(50), default="Warehouse Keeper")
    is_active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    description = db.Column(db.String(255))


class Supplier(db.Model):
    __tablename__ = "suppliers"

    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(150), nullable=False)
    contact_person = db.Column(db.String(100))
    phone = db.Column(db.String(50))
    email = db.Column(db.String(100))
    address = db.Column(db.Text)

    goods_in = db.relationship(
        "GoodsIn",
        backref="supplier",
        lazy=True
    )

class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)
    company_name = db.Column(db.String(150), nullable=False)
    contact_person = db.Column(db.String(100))
    phone = db.Column(db.String(50))
    email = db.Column(db.String(100))
    address = db.Column(db.Text)


class Product(db.Model):
    __tablename__ = "products"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), nullable=False)
    sku = db.Column(db.String(100), unique=True)
    barcode = db.Column(db.String(100))
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))
    brand = db.Column(db.String(100))
    unit = db.Column(db.String(30))
    minimum_stock = db.Column(db.Integer, default=0)
    description = db.Column(db.Text)
    status = db.Column(db.String(20), default="Active")
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    batches = db.relationship("Batch", backref="product", lazy=True)


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

    manufacture_date = db.Column(db.Date)

    expiry_date = db.Column(db.Date)

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

    stock_movements = db.relationship(
        "StockMovement",
        backref="batch",
        lazy=True
    )

class GoodsIn(db.Model):
    __tablename__ = "goods_in"

    id = db.Column(db.Integer, primary_key=True)
    reference_no = db.Column(db.String(100), unique=True)
    container_number = db.Column(db.String(100))
    truck_number = db.Column(db.String(100))
    driver_name = db.Column(db.String(100))
    supplier_id = db.Column(db.Integer, db.ForeignKey("suppliers.id"))
    received_by = db.Column(db.String(100))
    received_date = db.Column(db.DateTime, default=datetime.utcnow)
    remarks = db.Column(db.Text)

    items = db.relationship(
        "GoodsInItem",
        backref="goods_in",
        cascade="all, delete-orphan",
        lazy=True
    )


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

    product = db.relationship(
        "Product",
        lazy=True
    )

    batch = db.relationship(
        "Batch",
        lazy=True
    )

class GoodsOut(db.Model):
    __tablename__ = "goods_out"

    id = db.Column(db.Integer, primary_key=True)
    reference_no = db.Column(db.String(100), unique=True)
    customer_id = db.Column(db.Integer, db.ForeignKey("customers.id"))
    truck_number = db.Column(db.String(100))
    driver_name = db.Column(db.String(100))
    issued_by = db.Column(db.String(100))
    issued_date = db.Column(db.DateTime, default=datetime.utcnow)
    remarks = db.Column(db.Text)

    items = db.relationship(
        "GoodsOutItem",
        backref="goods_out",
        cascade="all, delete-orphan",
        lazy=True
    )


class GoodsOutItem(db.Model):
    __tablename__ = "goods_out_items"

    id = db.Column(db.Integer, primary_key=True)
    goods_out_id = db.Column(db.Integer, db.ForeignKey("goods_out.id"))
    batch_id = db.Column(db.Integer, db.ForeignKey("batches.id"))
    quantity = db.Column(db.Integer, default=0)


class StockMovement(db.Model):
    __tablename__ = "stock_movements"

    id = db.Column(db.Integer, primary_key=True)
    batch_id = db.Column(db.Integer, db.ForeignKey("batches.id"))
    movement_type = db.Column(db.String(20))
    reference_type = db.Column(db.String(50))
    reference_id = db.Column(db.Integer)
    quantity = db.Column(db.Integer)
    balance = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
