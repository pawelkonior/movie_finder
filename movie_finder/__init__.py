from flask import Flask
import os

from movie_finder.extensions import *

base_dir = os.path.abspath(os.path.dirname(__file__))


def create_app():
    movie_finder = Flask(__name__)
    movie_finder.config["SECRET_KEY"] = "secret"
    movie_finder.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{os.path.join(base_dir, 'movie_finder.db')}"

    init_extensions(movie_finder)

    from movie_finder.views.main_views import main_bp
    from movie_finder.views.movie_views import movie_bp

    movie_finder.register_blueprint(main_bp)
    movie_finder.register_blueprint(movie_bp)

    return movie_finder


app = create_app()
