from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, FloatField, FileField, SubmitField
from wtforms.validators import DataRequired


class AddMovieForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired("Title is required, hommie!")])
    description = TextAreaField("Description")
    duration = FloatField("Duration")
    image = FileField("Cover")
    created = DateField("Created")
    submit = SubmitField("Add")
