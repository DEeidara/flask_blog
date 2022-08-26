from flask_login import current_user
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_blog.models import User


class RegistrationForm(FlaskForm):
    username = StringField(
        "Username:", validators=[DataRequired(), Length(min=2, max=20)]
    )
    email = StringField("Email:", validators=[DataRequired(), Email()])
    password = PasswordField("Password:", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm your password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Sign up")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError(
                "This username is already taken. Please, choose another one."
            )

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                "This email is already taken. Please, choose another one."
            )


class LoginForm(FlaskForm):
    email = StringField("Email:", validators=[DataRequired(), Email()])
    password = PasswordField("Password:", validators=[DataRequired()])
    remember = BooleanField("Stay signed in")
    submit = SubmitField("Sign in")


class UpdateAccountForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=20)]
    )
    email = StringField("Email", validators=[DataRequired(), Email()])
    picture = FileField(
        "Update the profile picture", validators=[FileAllowed(["jpg", "png"])]
    )
    submit = SubmitField("Save")

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(
                    "This username is already taken. Please, choose another one."
                )

    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError(
                    "This email is already taken. Please, choose another one."
                )


class RequestResetForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    submit = SubmitField("Send a request to change the password")

    @staticmethod
    def validate_email(email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError(
                "This email is already taken. Please, choose another one."
            )


class ResetPasswordForm(FlaskForm):
    password = PasswordField("Password:", validators=[DataRequired()])
    confirm_password = PasswordField(
        "Confirm your password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Change the password")
