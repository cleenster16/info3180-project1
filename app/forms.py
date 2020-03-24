from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, TextAreaField
from wtforms.validators import InputRequired, DataRequired, Email, Length
from flask_wtf.file import FileField, FileRequired, FileAllowed

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