from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, DataRequired, ValidationError, Email, Length
from flask_wtf.file import FileField, FileRequired, FileAllowed
from . import db
from app.models import UserProfile

class ProfileForm(FlaskForm):
    first_name = StringField('First Name', validators=[DataRequired()])
    last_name = StringField('Last Name', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    gender = SelectField('Gender', choices=[('Female', 'Female'), ('Male', 'Male')])
    location = StringField('Location', validators=[DataRequired()])
    biography = TextAreaField('Biography', render_kw={"rows": 5, "cols": 40}, validators=[DataRequired()] )
    photo = FileField('Profile Picture', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'Images only!'])])
    submit = SubmitField()

    def validate_email(self, email):
        user = db.session.query(UserProfile).filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('This email is already used.')