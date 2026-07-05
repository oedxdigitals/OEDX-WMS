from flask import Blueprint, render_template

from app.models.product import Product
from app.models.goods_in import GoodsIn
from app.models.goods_out import GoodsOut
from app.models.stock import StockMovement
from app.models.batch import Batch
from app.utils.auth import login_required

report_bp = Blueprint(
    "report",
    __name__,
    url_prefix="/report"
)


@report_bp.route("/")
@login_required
def index():

    return render_template(
        "report/index.html",
        products=Product.query.count(),
        inventory=Batch.query.count(),
        goods_in=GoodsIn.query.count(),
        goods_out=GoodsOut.query.count(),
        movements=StockMovement.query.count(),
    )
