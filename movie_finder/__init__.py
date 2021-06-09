from flask import Flask


def create_app():
    movie_finder = Flask(__name__)

    from movie_finder.views.main_views import main_bp
    movie_finder.register_blueprint(main_bp)

    return movie_finder


app = create_app()
