from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, RadioField, SelectField, SubmitField, PasswordField
from wtforms.validators import DataRequired, Length, Email

class UserForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max=50)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    subscribe = BooleanField('Subscribe to Newsletter')
    gender = RadioField('Gender', choices=[('male', 'Male'), ('female', 'Female')])
    country = SelectField('Country', choices=[('us', 'United States'), ('ca', 'Canada'), ('uk', 'United Kingdom')])
    submit = SubmitField('Submit')
