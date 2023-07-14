from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    location = StringField('Location', validators=[DataRequired()])
    college = StringField('College', validators=[DataRequired()])
    major = StringField('Major', validators=[DataRequired()])
    career = StringField('Career', validators=[DataRequired()])
    dream_company = StringField('Dream Company', validators=[DataRequired()])
    linkedin = StringField('LinkedIn', validators=[DataRequired()])
    projects = StringField('Projects', validators=[DataRequired()])
    submit = SubmitField('Sign Up')
