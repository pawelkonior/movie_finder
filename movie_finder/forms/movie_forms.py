from flask_wtf import FlaskForm
from wtforms import StringField, DateField, TextAreaField, FloatField, FileField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length
from flask_wtf.file import FileAllowed


class MovieForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired("Title is required, hommie!"),
                                             Length(min=3, max=50,
                                                    message="Input must be between 3 and 40 characters long")])
    description = TextAreaField("Description")
    image = FileField("Cover", validators=[FileAllowed(["jpg", "jpeg", "png"], "Images only")])


class AddMovieForm(MovieForm):
    duration = FloatField("Duration")
    created = DateField("Created")
    submit = SubmitField("Add")


class EditMovieForm(MovieForm):
    submit = SubmitField("Edit")


class FilterForm(FlaskForm):
    title = StringField("Title", validators=[Length(max=20)])
    duration = SelectField("Duration", coerce=int, choices=[(0, '---'), (1, "Long to short"), (2, "Short to long")])
    submit = SubmitField("Filter")
