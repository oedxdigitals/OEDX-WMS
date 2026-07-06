from flask_wtf import FlaskForm

from wtforms import (
    StringField,
    PasswordField,
    SelectField,
    BooleanField,
    SubmitField,
)

from wtforms.validators import DataRequired


class UserForm(FlaskForm):

    fullname = StringField(
        "Full Name",
        validators=[DataRequired()],
    )

    username = StringField(
        "Username",
        validators=[DataRequired()],
    )

    password = PasswordField(
        "Password",
        validators=[DataRequired()],
    )

    role = SelectField(
        "Role",
        choices=[
            ("Admin", "Admin"),
            ("Supervisor", "Supervisor"),
            ("Warehouse Keeper", "Warehouse Keeper"),
        ],
    )

    is_active = BooleanField(
        "Active",
        default=True,
    )

    submit = SubmitField(
        "Save User",
    )
