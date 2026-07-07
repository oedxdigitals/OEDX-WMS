from flask import Blueprint, render_template, redirect, url_for

from app.extensions import db
from app.forms.supplier import SupplierForm
from app.models.supplier import Supplier
from app.utils.auth import login_required
from app.utils.roles import roles_required
from app.utils.audit import log_action


suppliers_bp = Blueprint(
    "suppliers",
    __name__,
    url_prefix="/suppliers"
)


@suppliers_bp.route("/")
@login_required
@roles_required("Admin", "Supervisor")
def index():

    suppliers = Supplier.query.order_by(
        Supplier.company_name
    ).all()

    return render_template(
        "suppliers/list.html",
        suppliers=suppliers
    )


@suppliers_bp.route("/new", methods=["GET", "POST"])
@login_required
@roles_required("Admin")
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

        log_action(
            action="CREATE",
            module="Suppliers",
            description=f"Created supplier: {supplier.company_name}",
        )

        return redirect(
            url_for("suppliers.index")
        )

    return render_template(
        "suppliers/form.html",
        form=form
    )
