from flask import Blueprint, render_template, redirect, url_for
from movie_finder.forms.movie_forms import AddMovieForm

movie_bp = Blueprint("movie", __name__, url_prefix="/movie")


@movie_bp.route("/add", methods=["GET", "POST"])
def add_movie():
    form = AddMovieForm()

    if form.validate_on_submit():
        print(form.title.data)
        print(form.description.data)
        print(form.duration.data)

        return redirect(url_for("main.index"))

    return render_template("add_movie.html", form=form)
