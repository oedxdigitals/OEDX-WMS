from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    flash,
)

from app.extensions import db
from app.forms.product import ProductForm
from app.models.product import Product

from app.utils.auth import login_required
from app.utils.roles import roles_required
from app.utils.audit import log_action


products_bp = Blueprint(
    "products",
    __name__,
    url_prefix="/products",
)


@products_bp.route("/")
@login_required
@roles_required("Admin", "Supervisor")
def index():

    products = Product.query.order_by(
        Product.name
    ).all()

    return render_template(
        "products/list.html",
        products=products,
    )


@products_bp.route("/new", methods=["GET", "POST"])
@login_required
@roles_required("Admin")
def new():

    form = ProductForm()

    if form.validate_on_submit():

        # Check duplicate SKU
        existing = Product.query.filter_by(
            sku=form.sku.data
        ).first()

        if existing:

            flash(
                "SKU already exists.",
                "danger",
            )

            return render_template(
                "products/form.html",
                form=form,
            )

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

        log_action(
            action="CREATE",
            module="Products",
            description=f"Created product '{product.name}' (SKU: {product.sku})",
        )

        flash(
            "Product created successfully.",
            "success",
        )

        return redirect(
            url_for("products.index")
        )

    return render_template(
        "products/form.html",
        form=form,
    )
