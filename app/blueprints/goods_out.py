from flask import Blueprint, render_template, redirect, url_for

from app.extensions import db

from app.forms.goods_out import GoodsOutForm

from app.models.goods_out import GoodsOut
from app.models.customer import Customer


goods_out_bp = Blueprint(
    "goods_out",
    __name__,
    url_prefix="/goods-out"
)


@goods_out_bp.route("/")
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
            url_for("goods_out.index")
        )

    return render_template(
        "goods_out/form.html",
        form=form
    )
