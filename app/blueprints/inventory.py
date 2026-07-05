from datetime import date

from flask import Blueprint, render_template, request
from sqlalchemy import or_

from app.models.batch import Batch
from app.models.product import Product

inventory_bp = Blueprint(
    "inventory",
    __name__,
    url_prefix="/inventory"
)


@inventory_bp.route("/")
def index():

    search = request.args.get(
        "search",
        ""
    ).strip()

    query = Batch.query.join(Product)

    if search:

        query = query.filter(

            or_(

                Product.name.ilike(f"%{search}%"),

                Batch.batch_number.ilike(f"%{search}%"),

                Batch.warehouse_location.ilike(f"%{search}%")

            )

        )

    batches = query.order_by(
        Batch.expiry_date
    ).all()

    today = date.today()

    return render_template(

        "inventory/list.html",

        batches=batches,

        search=search,

        today=today

    )
