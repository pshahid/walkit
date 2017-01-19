from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Subreddit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20))
    created = db.Column(db.Date())
    subscribers = db.Column(db.Integer)
