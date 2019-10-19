from flask import Flask
from flask_caching import Cache

app = Flask(__name__)
app.config.from_pyfile("config.py")

cache = Cache(app)

from heckingoodboys import views  # noqa: F401
