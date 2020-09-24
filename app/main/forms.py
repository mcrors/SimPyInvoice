from flask_wtf import FlaskForm
from wtforms import (
    StringField, PasswordField, BooleanField, SubmitField, ValidationError
)
from wtforms.validators import (
    DataRequired, Length, Email, EqualTo, Regexp
)
from ..models import Client

