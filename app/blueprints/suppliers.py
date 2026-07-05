from flask import Blueprint
from flask import render_template
from flask import redirect
from flask import url_for

from app.extensions import db
from app.forms import SupplierForm
from app.models import Supplier

suppliers_bp = Blueprint(
    "suppliers",
    __name__,
    url_prefix="/suppliers"
)


@suppliers_bp.route("/")
def index():

    suppliers = Supplier.query.order_by(
        Supplier.company_name
    ).all()

    return render_template(
        "suppliers/list.html",
        suppliers=suppliers
    )


@suppliers_bp.route(
    "/new",
    methods=["GET", "POST"]
)
def new():

    form = SupplierForm()

    if form.validate_on_submit():

        supplier = Supplier(
            company_name=form.company_name.data,
            contact_person=form.contact_person.data,
            phone=form.phone.data,
            email=form.email.data,
            address=form.address.data
        )

        db.session.add(supplier)
        db.session.commit()

        return redirect(
            url_for("suppliers.index")
        )

    return render_template(
        "suppliers/form.html",
        form=form
    )
