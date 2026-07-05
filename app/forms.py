from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ProductForm(FlaskForm):
    name = StringField("Product Name", validators=[DataRequired()])
    sku = StringField("SKU")
    category = StringField("Category")
    unit = StringField("Unit")

    submit = SubmitField("Save Product")


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
