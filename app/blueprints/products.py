from flask import Blueprint, render_template, redirect, url_for

from app.forms import ProductForm
from app.models import Product
from app.extensions import db

products_bp = Blueprint(
    "products",
    __name__,
    url_prefix="/products"
)


@products_bp.route("/")
def index():

    products = Product.query.order_by(Product.id.desc()).all()

    return render_template(
        "products/list.html",
        products=products
    )


@products_bp.route("/new", methods=["GET", "POST"])
def new():

    form = ProductForm()

    if form.validate_on_submit():

        product = Product(
            name=form.name.data,
            sku=form.sku.data,
            category=form.category.data,
            unit=form.unit.data,
        )

        db.session.add(product)
        db.session.commit()

        return redirect(url_for("products.index"))

    return render_template(
        "products/form.html",
        form=form
    )
