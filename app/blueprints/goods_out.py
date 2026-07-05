from flask import Blueprint, render_template, redirect, url_for

from app.extensions import db

from app.forms.goods_out import GoodsOutForm
from app.forms.goods_out_item import GoodsOutItemForm

from app.models.goods_out import GoodsOut
from app.models.goods_out_item import GoodsOutItem
from app.models.customer import Customer
from app.models.batch import Batch
from app.models.stock import StockMovement
from app.utils.auth import login_required


goods_out_bp = Blueprint(
    "goods_out",
    __name__,
    url_prefix="/goods-out"
)


@goods_out_bp.route("/")
@login_required
def index():

    records = GoodsOut.query.order_by(
        GoodsOut.id.desc()
    ).all()

    return render_template(
        "goods_out/list.html",
        records=records
    )


@goods_out_bp.route(
    "/new",
    methods=["GET", "POST"]
)
@login_required
def new():

    form = GoodsOutForm()

    form.customer_id.choices = [

        (c.id, c.company_name)

        for c in Customer.query.order_by(
            Customer.company_name
        ).all()

    ]

    if form.validate_on_submit():

        record = GoodsOut(

            reference_no=form.reference_no.data,

            customer_id=form.customer_id.data,

            truck_number=form.truck_number.data,

            driver_name=form.driver_name.data,

            remarks=form.remarks.data

        )

        db.session.add(record)
        db.session.commit()

        return redirect(
            url_for(
                "goods_out.items",
                goods_out_id=record.id
            )
        )

    return render_template(
        "goods_out/form.html",
        form=form
    )


@goods_out_bp.route(
    "/<int:goods_out_id>/items",
    methods=["GET", "POST"]
)
@login_required
def items(goods_out_id):

    goods_out = GoodsOut.query.get_or_404(goods_out_id)

    form = GoodsOutItemForm()

    batches = Batch.query.filter(
        Batch.quantity > 0
    ).order_by(
        Batch.batch_number
    ).all()

    form.batch_id.choices = [

        (
            b.id,
            f"{b.product.name} | {b.batch_number} | Qty: {b.quantity}"
        )

        for b in batches

    ]

    if form.validate_on_submit():

        batch = Batch.query.get_or_404(
            form.batch_id.data
        )

        if form.quantity.data <= batch.quantity:

            batch.quantity -= form.quantity.data

            item = GoodsOutItem(

                goods_out_id=goods_out.id,

                batch_id=batch.id,

                quantity=form.quantity.data

            )

            db.session.add(item)

            movement = StockMovement(

                batch_id=batch.id,

                movement_type="OUT",

                reference_type="GoodsOut",

                reference_id=goods_out.id,

                quantity=form.quantity.data,

                balance=batch.quantity,

                user_id=1

            )

            db.session.add(movement)

            db.session.commit()

        return redirect(
            url_for(
                "goods_out.items",
                goods_out_id=goods_out.id
            )
        )

    items = GoodsOutItem.query.filter_by(
        goods_out_id=goods_out.id
    ).all()

    return render_template(
        "goods_out/items.html",
        form=form,
        goods_out=goods_out,
        items=items
    )
