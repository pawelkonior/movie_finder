from flask import Blueprint, render_template, redirect, url_for
from movie_finder.forms.movie_forms import AddMovieForm
from flask_wtf.file import FileRequired

from datetime import datetime
from movie_finder import db

from movie_finder.models.movie_models import Movie
from movie_finder.utils.utils import save_image_upload

movie_bp = Blueprint("movie", __name__, url_prefix="/movie")


@movie_bp.route("/<int:movie_id>")
def movie(movie_id):
    movie = Movie.query.get(movie_id)

    if movie:
        return render_template('movie.html', movie=movie)

    return redirect(url_for('main.index'))


@movie_bp.route("/add", methods=["GET", "POST"])
def add_movie():
    form = AddMovieForm()

    if form.validate_on_submit() and form.image.validate(form, extra_validators=(FileRequired(),)):
        filename = save_image_upload(form.image)

        title = form.title.data
        description = form.description.data
        duration = form.duration.data
        created = datetime.now()

        movie = Movie(title=title, description=description, duration=duration, created=created, image=filename)

        db.session.add(movie)
        db.session.commit()

        return redirect(url_for("main.index"))

    return render_template("add_movie.html", form=form)
