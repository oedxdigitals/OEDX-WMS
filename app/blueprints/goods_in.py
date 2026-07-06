from flask import Blueprint, render_template, redirect, url_for

from app.extensions import db

from app.forms.goods_in import (
    GoodsInForm,
    GoodsInItemForm,
)

from app.models.goods_in import GoodsIn, GoodsInItem
from app.models.supplier import Supplier
from app.models.product import Product
from app.models.batch import Batch
from app.models.stock import StockMovement
from app.utils.auth import login_required
from app.utils.roles import roles_required


goods_in_bp = Blueprint(
    "goods_in",
    __name__,
    url_prefix="/goods-in",
)


@goods_in_bp.route("/")
@login_required
@roles_required(
    "Admin",
    "Supervisor",
    "Warehouse Keeper",
)
def index():
    records = GoodsIn.query.order_by(GoodsIn.id.desc()).all()

    return render_template(
        "goods_in/list.html",
        records=records,
    )


@goods_in_bp.route("/new", methods=["GET", "POST"])
@login_required
@roles_required(
    "Admin",
    "Supervisor",
    "Warehouse Keeper",
)
def new():
    form = GoodsInForm()

    form.supplier_id.choices = [
        (supplier.id, supplier.company_name)
        for supplier in Supplier.query.order_by(Supplier.company_name).all()
    ]

    if form.validate_on_submit():

        record = GoodsIn(
            reference_no=form.reference_no.data,
            supplier_id=form.supplier_id.data,
            container_number=form.container_number.data,
            truck_number=form.truck_number.data,
            driver_name=form.driver_name.data,
            remarks=form.remarks.data,
        )

        db.session.add(record)
        db.session.commit()

        # After creating the Goods In header,
        # go directly to adding items.
        return redirect(
            url_for(
                "goods_in.items",
                goods_in_id=record.id,
            )
        )

    return render_template(
        "goods_in/form.html",
        form=form,
    )


@goods_in_bp.route("/<int:goods_in_id>/items", methods=["GET", "POST"])
@login_required
@roles_required(
    "Admin",
    "Supervisor",
    "Warehouse Keeper",
)
def items(goods_in_id):

    goods_in = GoodsIn.query.get_or_404(goods_in_id)

    form = GoodsInItemForm()

    form.product_id.choices = [
        (product.id, product.name)
        for product in Product.query.order_by(Product.name).all()
    ]

    if form.validate_on_submit():

        batch = Batch(
            product_id=form.product_id.data,
            supplier_id=goods_in.supplier_id,
            batch_number=form.batch_number.data,
            manufacture_date=form.manufacture_date.data,
            expiry_date=form.expiry_date.data,
            quantity=form.quantity.data,
            warehouse_location=form.warehouse_location.data,
        )

        db.session.add(batch)
        db.session.flush()

        item = GoodsInItem(
            goods_in_id=goods_in.id,
            product_id=form.product_id.data,
            batch_id=batch.id,
            quantity=form.quantity.data,
        )

        db.session.add(item)

        movement = StockMovement(
            batch_id=batch.id,
            movement_type="IN",
            reference_type="GoodsIn",
            reference_id=goods_in.id,
            quantity=form.quantity.data,
            balance=form.quantity.data,
            user_id=1,
        )

        db.session.add(movement)
        db.session.commit()

        return redirect(
            url_for(
                "goods_in.items",
                goods_in_id=goods_in.id,
            )
        )

    items = GoodsInItem.query.filter_by(
        goods_in_id=goods_in.id
    ).all()

    return render_template(
        "goods_in/items.html",
        form=form,
        goods_in=goods_in,
        items=items,
    )
