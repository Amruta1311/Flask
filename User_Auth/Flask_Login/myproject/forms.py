from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo     #EqualTo is used for password confirmation
from wtforms import ValidationError

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log in', validators=[DataRequired()])


class RegistrationForm(FlaskForm):
    email = StringField('Email', validators = [DataRequired(), Email()])
    username = StringField('Username', validators = [DataRequired()])
    password = PasswordField('Password', validators = [DataRequired(), EqualTo('pass_confirm', message = 'Passwrds must match!')])
    pass_confirm = PasswordField('Confirm Password', validators = [DataRequired()])
    submit = SubmitField('Register!')

    def check_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Your Email has been already registered!')

    def check_username(self, field):
        if User.query.filter_by(username=field.data).first():
            raise ValidationError('Username is taken!')



