from flask_wtf import FlaskForm
from wtforms import (
    SelectField,
    IntegerField,
    SubmitField,
)
from wtforms.validators import DataRequired, NumberRange


class GoodsOutItemForm(FlaskForm):

    batch_id = SelectField(
        "Batch",
        coerce=int,
        validators=[DataRequired()]
    )

    quantity = IntegerField(
        "Quantity",
        validators=[
            DataRequired(),
            NumberRange(min=1)
        ]
    )

    submit = SubmitField(
        "Issue Stock"
    )
