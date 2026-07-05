from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SelectField,
    SubmitField,
)
from wtforms.validators import DataRequired


class GoodsOutForm(FlaskForm):

    reference_no = StringField(
        "Reference No",
        validators=[DataRequired()]
    )

    customer_id = SelectField(
        "Customer",
        coerce=int,
        validators=[DataRequired()]
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
        "Save Goods Out"
    )
