from flask import Blueprint, render_template, redirect, url_for
from movie_finder.forms.movie_forms import AddMovieForm

from datetime import datetime
from movie_finder import db

from movie_finder.models.movie_models import Movie

movie_bp = Blueprint("movie", __name__, url_prefix="/movie")


@movie_bp.route("/add", methods=["GET", "POST"])
def add_movie():
    form = AddMovieForm()

    if form.validate_on_submit():
        title = form.title.data
        description = form.description.data
        duration = form.duration.data
        created = datetime.now()

        movie = Movie(title=title, description=description, duration=duration, created=created)

        db.session.add(movie)
        db.session.commit()

        return redirect(url_for("main.index"))

    return render_template("add_movie.html", form=form)
