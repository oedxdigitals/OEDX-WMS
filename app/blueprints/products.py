from flask import Blueprint, render_template, redirect, url_for

from app.extensions import db
from app.forms.product import ProductForm
from app.models.product import Product
from app.utils.auth import login_required

products_bp = Blueprint(
    "products",
    __name__,
    url_prefix="/products",
)


@products_bp.route("/")
@login_required
def index():
    products = Product.query.order_by(Product.id.desc()).all()

    return render_template(
        "products/list.html",
        products=products,
    )


@products_bp.route("/new", methods=["GET", "POST"])
@login_required
def new():
    form = ProductForm()

    if form.validate_on_submit():
        product = Product(
            name=form.name.data,
            sku=form.sku.data,
            barcode="",
            category_id=None,
            brand="",
            unit=form.unit.data,
            minimum_stock=0,
            description="",
            status="Active",
        )

        db.session.add(product)
        db.session.commit()

        return redirect(url_for("products.index"))

    return render_template(
        "products/form.html",
        form=form,
    )
