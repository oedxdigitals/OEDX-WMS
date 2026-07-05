from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class SupplierForm(FlaskForm):

    company_name = StringField(
        "Company Name",
        validators=[DataRequired()]
    )

    contact_person = StringField(
        "Contact Person"
    )

    phone = StringField(
        "Phone"
    )

    email = StringField(
        "Email"
    )

    address = StringField(
        "Address"
    )

    submit = SubmitField(
        "Save Supplier"
    )
