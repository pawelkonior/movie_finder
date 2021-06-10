from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, FloatField, FileField, SubmitField


class AddMovieForm(FlaskForm):
    title = StringField("Title")
    description = TextAreaField("Description")
    duration = FloatField("Duration")
    image = FileField("Cover")
    created = DateField("Created")
    submit = SubmitField("Add")
