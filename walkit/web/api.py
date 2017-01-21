from flask_restful import Resource, reqparse, abort
from .models import Subreddit


class SubredditResource(Resource):
    def get(self, name):
        sub = Subreddit.query.filter_by(name=name).first()
        if sub:
            return sub
        else:
            return {}


parser = reqparse.RequestParser()
parser.add_argument('name')


class SubredditList(Resource):
    def get(self):
        return Subreddit.query.all()

    def post(self):
        args = parser.parse_args()
        # TODO add subreddit to db
