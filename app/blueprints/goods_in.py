from flask import Blueprint
from flask import render_template

goods_in_bp = Blueprint(
    "goods_in",
    __name__,
    url_prefix="/goods-in"
)


@goods_in_bp.route("/")
def index():

    return render_template(
        "goods_in/list.html"
    )

@goods_in_bp.route("/new")
def new():

    return "<h2>Goods In Form - Coming Next Step</h2>"
