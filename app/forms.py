# forms.py

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, DataRequired, Email

class RegisterForm(FlaskForm):
    username = StringField(label='User Name', validators=[Length(min=3, max=15), DataRequired()])
    email_address = StringField(label='Email Address', validators=[Email()])
    password1 = PasswordField(label='Password', validators=[Length(min=2), DataRequired()])
    password2 = PasswordField(label='Confirm Password', validators=[EqualTo('password1'), DataRequired()])
    submit = SubmitField(label='Submit')

class LoginForm(FlaskForm):
    username = StringField(label='User Name', validators=[DataRequired()])
    password = PasswordField(label='Password', validators=[DataRequired()])
    submit = SubmitField(label='Login')