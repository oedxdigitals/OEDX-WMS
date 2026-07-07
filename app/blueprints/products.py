from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    flash,
)

from sqlalchemy import or_

from app.extensions import db
from app.forms.product import ProductForm
from app.models.product import Product
from app.utils.audit import log_action


products_bp = Blueprint(
    "products",
    __name__,
    url_prefix="/products",
)


@products_bp.route("/")
def index():

    search = request.args.get(
        "search",
        "",
    )

    page = request.args.get(
        "page",
        1,
        type=int,
    )

    query = Product.query

    if search:

        query = query.filter(

            or_(

                Product.name.ilike(f"%{search}%"),

                Product.sku.ilike(f"%{search}%"),

            )

        )

    products = query.order_by(
        Product.name
    ).paginate(
        page=page,
        per_page=10,
    )

    return render_template(
        "products/list.html",
        products=products,
        search=search,
    )


@products_bp.route(
    "/new",
    methods=["GET", "POST"],
)
def new():

    form = ProductForm()

    if form.validate_on_submit():

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

            unit=form.unit.data,

            category_id=None,

            barcode="",

            brand="",

            minimum_stock=0,

            description="",

            status="Active",

        )

        db.session.add(product)

        db.session.commit()

        log_action(

            action="CREATE",

            module="Products",

            description=f"Created product {product.name}",

        )

        flash(
            "Product created successfully.",
            "success",
        )

        return redirect(
            url_for(
                "products.index"
            )
        )

    return render_template(
        "products/form.html",
        form=form,
    )


@products_bp.route(
    "/edit/<int:id>",
    methods=["GET", "POST"],
)
def edit(id):

    product = Product.query.get_or_404(id)

    form = ProductForm(
        obj=product
    )

    if form.validate_on_submit():

        duplicate = Product.query.filter(

            Product.sku == form.sku.data,

            Product.id != product.id,

        ).first()

        if duplicate:

            flash(
                "SKU already exists.",
                "danger",
            )

            return render_template(
                "products/form.html",
                form=form,
            )

        product.name = form.name.data
        product.sku = form.sku.data
        product.unit = form.unit.data

        db.session.commit()

        log_action(

            action="UPDATE",

            module="Products",

            description=f"Updated product {product.name}",

        )

        flash(
            "Product updated successfully.",
            "success",
        )

        return redirect(
            url_for(
                "products.index"
            )
        )

    return render_template(
        "products/form.html",
        form=form,
    )


@products_bp.route(
    "/delete/<int:id>"
)
def delete(id):

    product = Product.query.get_or_404(id)

    name = product.name

    db.session.delete(product)

    db.session.commit()

    log_action(

        action="DELETE",

        module="Products",

        description=f"Deleted product {name}",

    )

    flash(
        "Product deleted.",
        "warning",
    )

    return redirect(
        url_for(
            "products.index"
        )
    )
