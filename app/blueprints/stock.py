from flask import Blueprint, render_template

from app.models.stock import StockMovement
from app.utils.auth import login_required

stock_bp = Blueprint(
    "stock",
    __name__,
    url_prefix="/stock"
)


@stock_bp.route("/")
@login_required
def index():

    movements = (
        StockMovement.query
        .order_by(
            StockMovement.created_at.desc()
        )
        .all()
    )

    return render_template(
        "stock/list.html",
        movements=movements
    )
