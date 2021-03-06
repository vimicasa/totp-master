from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class VerifyForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    token = StringField('Token', validators=[DataRequired()])
    submit = SubmitField('Verify')