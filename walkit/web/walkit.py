from flask import Flask, g
from flask_restful import Api

from .models import db
from .api import SubredditResource
import configparser


def get_config(type='development'):
    config = configparser.ConfigParser()
    config.read('db.ini')
    print(config)
    cfg = config[type]
    return 'postgresql://{0}:{1}@{2}:{3}/{4}'.format(cfg['username'], cfg['password'],
                                                   cfg['hostname'], cfg['port'], cfg['database'])

db_uri = get_config(type='development')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db.init_app(app)

with app.app_context():
    db.create_all()

api = Api(app)

@app.route("/")
def index():
    return ""

api.add_resource(SubredditResource, '/subreddit/')
