from flask_login import current_user
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Length, Email
from app.models import Client


class AddClientForm(FlaskForm):
    name = StringField('Client Name', validators=[DataRequired(), Length(1, 64)])
    contact_name = StringField('Contact Name', validators=[DataRequired(), Length(1, 64)])
    contact_email = StringField('Contact Email', validators=[DataRequired(), Length(1, 64), Email()])
    submit = SubmitField('Add Client')

    def validate_name(self, field):
        if Client.query.filter_by(user=current_user).filter_by(name=field.data).first():
            raise ValidationError('You already have a client with that name')
