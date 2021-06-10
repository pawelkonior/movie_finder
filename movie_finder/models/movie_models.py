from movie_finder import db


class Movie(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(120), nullable=False)
    description = db.Column(db.Text())
    duration = db.Column(db.Integer())
    image = db.Column(db.String(80))
    created = db.Column(db.DateTime(), nullable=False)
    test = db.Column(db.String(10))
