from flask import Blueprint, render_template

from app.models.batch import Batch

inventory_bp = Blueprint(
    "inventory",
    __name__,
    url_prefix="/inventory"
)


@inventory_bp.route("/")
def index():

    batches = Batch.query.order_by(
        Batch.product_id,
        Batch.batch_number
    ).all()

    return render_template(
        "inventory/list.html",
        batches=batches
    )
