from flask import Blueprint, render_template

from app.models.product import Product
from app.models.supplier import Supplier
from app.models.customer import Customer
from app.models.batch import Batch
from app.models.goods_in import GoodsIn
from app.models.goods_out import GoodsOut
from app.utils.auth import login_required

dashboard_bp = Blueprint(
    "dashboard",
    __name__
)


@dashboard_bp.route("/")
@login_required
def index():

    stats = {

        "products": Product.query.count(),

        "suppliers": Supplier.query.count(),

        "customers": Customer.query.count(),

        "batches": Batch.query.count(),

        "goods_in": GoodsIn.query.count(),

        "goods_out": GoodsOut.query.count(),

        "stock": sum(
            batch.quantity
            for batch in Batch.query.all()
        )

    }

    return render_template(
        "dashboard.html",
        stats=stats
    )
