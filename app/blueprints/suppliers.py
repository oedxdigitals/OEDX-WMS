from flask import (
    Blueprint,
    render_template,
    redirect,
    url_for,
    request,
    flash,
)

from sqlalchemy import or_

from app.extensions import db
from app.forms.supplier import SupplierForm
from app.models.supplier import Supplier
from app.utils.audit import log_action


suppliers_bp = Blueprint(
    "suppliers",
    __name__,
    url_prefix="/suppliers",
)


@suppliers_bp.route("/")
def index():

    search = request.args.get("search", "")
    page = request.args.get("page", 1, type=int)

    query = Supplier.query

    if search:

        query = query.filter(

            or_(

                Supplier.company_name.ilike(f"%{search}%"),

                Supplier.contact_person.ilike(f"%{search}%"),

                Supplier.phone.ilike(f"%{search}%"),

            )

        )

    suppliers = query.order_by(
        Supplier.company_name
    ).paginate(
        page=page,
        per_page=10,
    )

    return render_template(
        "suppliers/list.html",
        suppliers=suppliers,
        search=search,
    )


@suppliers_bp.route("/new", methods=["GET", "POST"])
def new():

    form = SupplierForm()

    if form.validate_on_submit():

        supplier = Supplier(

            company_name=form.company_name.data,
            contact_person=form.contact_person.data,
            phone=form.phone.data,
            email=form.email.data,
            address=form.address.data,

        )

        db.session.add(supplier)
        db.session.commit()

        log_action(
            "CREATE",
            "Suppliers",
            f"Created supplier {supplier.company_name}",
        )

        flash(
            "Supplier created successfully.",
            "success",
        )

        return redirect(
            url_for("suppliers.index")
        )

    return render_template(
        "suppliers/form.html",
        form=form,
    )


@suppliers_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):

    supplier = Supplier.query.get_or_404(id)

    form = SupplierForm(obj=supplier)

    if form.validate_on_submit():

        form.populate_obj(supplier)

        db.session.commit()

        log_action(
            "UPDATE",
            "Suppliers",
            f"Updated supplier {supplier.company_name}",
        )

        flash(
            "Supplier updated successfully.",
            "success",
        )

        return redirect(
            url_for("suppliers.index")
        )

    return render_template(
        "suppliers/form.html",
        form=form,
    )


@suppliers_bp.route("/delete/<int:id>")
def delete(id):

    supplier = Supplier.query.get_or_404(id)

    name = supplier.company_name

    db.session.delete(supplier)
    db.session.commit()

    log_action(
        "DELETE",
        "Suppliers",
        f"Deleted supplier {name}",
    )

    flash(
        "Supplier deleted.",
        "warning",
    )

    return redirect(
        url_for("suppliers.index")
    )
