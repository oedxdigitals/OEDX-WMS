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
from app.forms.customer import CustomerForm
from app.models.customer import Customer
from app.utils.audit import log_action


customers_bp = Blueprint(
    "customers",
    __name__,
    url_prefix="/customers",
)


@customers_bp.route("/")
def index():

    search = request.args.get("search", "")
    page = request.args.get("page", 1, type=int)

    query = Customer.query

    if search:

        query = query.filter(

            or_(

                Customer.company_name.ilike(f"%{search}%"),

                Customer.contact_person.ilike(f"%{search}%"),

                Customer.phone.ilike(f"%{search}%"),

            )

        )

    customers = query.order_by(
        Customer.company_name
    ).paginate(
        page=page,
        per_page=10,
    )

    return render_template(
        "customers/list.html",
        customers=customers,
        search=search,
    )


@customers_bp.route("/new", methods=["GET", "POST"])
def new():

    form = CustomerForm()

    if form.validate_on_submit():

        customer = Customer(

            company_name=form.company_name.data,
            contact_person=form.contact_person.data,
            phone=form.phone.data,
            email=form.email.data,
            address=form.address.data,

        )

        db.session.add(customer)
        db.session.commit()

        log_action(
            "CREATE",
            "Customers",
            f"Created customer {customer.company_name}",
        )

        flash(
            "Customer created successfully.",
            "success",
        )

        return redirect(
            url_for("customers.index")
        )

    return render_template(
        "customers/form.html",
        form=form,
    )


@customers_bp.route("/edit/<int:id>", methods=["GET", "POST"])
def edit(id):

    customer = Customer.query.get_or_404(id)

    form = CustomerForm(obj=customer)

    if form.validate_on_submit():

        form.populate_obj(customer)

        db.session.commit()

        log_action(
            "UPDATE",
            "Customers",
            f"Updated customer {customer.company_name}",
        )

        flash(
            "Customer updated successfully.",
            "success",
        )

        return redirect(
            url_for("customers.index")
        )

    return render_template(
        "customers/form.html",
        form=form,
    )


@customers_bp.route("/delete/<int:id>")
def delete(id):

    customer = Customer.query.get_or_404(id)

    name = customer.company_name

    db.session.delete(customer)
    db.session.commit()

    log_action(
        "DELETE",
        "Customers",
        f"Deleted customer {name}",
    )

    flash(
        "Customer deleted.",
        "warning",
    )

    return redirect(
        url_for("customers.index")
    )
