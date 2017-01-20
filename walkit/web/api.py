from flask_restful import Resource
from .models import Subreddit


class SubredditResource(Resource):
    def get(self):
        return Subreddit.query.all()
