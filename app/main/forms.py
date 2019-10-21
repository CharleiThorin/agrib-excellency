from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import InputRequired, Length, Email
from wtforms.fields.html5 import TelField


class ContactForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Length(1, 64), Email()])
    phone = TelField('phone', validators=[InputRequired()])
    message = TextAreaField('Message', validators=[InputRequired()])
    submit = SubmitField('Send Message')


class RegistrationForm(FlaskForm):
    first_name = StringField('Name', validators=[InputRequired()])
    last_name = StringField('Name', validators=[InputRequired()])
    email = StringField('Email', validators=[InputRequired(), Length(1, 64), Email()])
    phone = TelField('phone', validators=[InputRequired()])
    message = TextAreaField('Message', validators=[InputRequired()])
    submit = SubmitField('Submit Form')
