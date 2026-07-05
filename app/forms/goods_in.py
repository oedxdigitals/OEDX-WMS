from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SelectField,
    IntegerField,
    DateField,
    SubmitField,
)
from wtforms.validators import DataRequired


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

    submit = SubmitField(
        "Add Item"
    )
