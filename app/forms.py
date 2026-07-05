from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
from wtforms import SelectField
from wtforms import IntegerField, DateField

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

class CustomerForm(FlaskForm):

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
        "Save Customer"
    )

class GoodsInForm(FlaskForm):

    reference_no = StringField(
        "Reference No",
        validators=[DataRequired()]
    )

    supplier_id = SelectField(
        "Supplier",
        coerce=int,
        validators=[DataRequired()]
    )

    container_number = StringField(
        "Container Number"
    )

    truck_number = StringField(
        "Truck Number"
    )

    driver_name = StringField(
        "Driver Name"
    )

    remarks = StringField(
        "Remarks"
    )

    submit = SubmitField(
        "Save Goods In"
    )

class GoodsInItemForm(FlaskForm):

    product_id = SelectField(
        "Product",
        coerce=int,
        validators=[DataRequired()]
    )

    batch_number = StringField(
        "Batch Number",
        validators=[DataRequired()]
    )

    manufacture_date = DateField(
        "Manufacture Date",
        format="%Y-%m-%d"
    )

    expiry_date = DateField(
        "Expiry Date",
        format="%Y-%m-%d"
    )

    quantity = IntegerField(
        "Quantity",
        validators=[DataRequired()]
    )

    warehouse_location = StringField(
        "Warehouse Location"
    )
