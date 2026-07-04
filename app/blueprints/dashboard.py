from flask import Blueprint, render_template

from app.models import Product, Batch

dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/")
def index():
    return render_template(
        "dashboard.html",
        total_products=Product.query.count(),
        total_batches=Batch.query.count(),
        goods_in_today=0,
        goods_out_today=0,
    )
