from flask import Blueprint, render_template, redirect, url_for

from app.extensions import db
from app.forms.customer import CustomerForm
from app.models.customer import Customer

customers_bp = Blueprint(
    "customers",
    __name__,
    url_prefix="/customers"
)


@customers_bp.route("/")
def index():

    customers = Customer.query.order_by(
        Customer.company_name
    ).all()

    return render_template(
        "customers/list.html",
        customers=customers
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
            address=form.address.data
        )

        db.session.add(customer)
        db.session.commit()

        return redirect(url_for("customers.index"))

    return render_template(
        "customers/form.html",
        form=form
    )
