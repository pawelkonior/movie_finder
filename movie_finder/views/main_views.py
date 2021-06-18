from flask import Blueprint, render_template, send_from_directory, request
from movie_finder.models.movie_models import Movie
from movie_finder.forms.movie_forms import FilterForm

from movie_finder.utils.utils import upload_path

main_bp = Blueprint("main", __name__, url_prefix="/")


@main_bp.route("/uploads/<filename>")
def uploads(filename):
    return send_from_directory(upload_path, filename)


@main_bp.route("/")
def index():
    form = FilterForm(request.args, meta={"csrf": False})
    print()

    movies = Movie.query.filter(Movie.title.like(f"%{form.data.get('title')}%")).all()

    return render_template("index.html", movies=movies, form=form)
