from flask import Blueprint, render_template
from movie_finder.models.movie_models import Movie

main_bp = Blueprint("main", __name__, url_prefix="/")


@main_bp.route("/")
def index():
    movies = Movie.query.all()

    return render_template("index.html", movies=movies)
