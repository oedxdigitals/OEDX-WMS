from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class ProductForm(FlaskForm):
    name = StringField("Product Name", validators=[DataRequired()])
    sku = StringField("SKU")
    category = StringField("Category")
    unit = StringField("Unit")

    submit = SubmitField("Save Product")
