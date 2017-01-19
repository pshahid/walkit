from flask import Flask, g

from .models import db

app = Flask(__name__)
db.init_app(app)

@app.route("/")
def index():
    return ""
