import logging

from flask import Flask
from flask_caching import Cache

app = Flask(__name__)
app.config.from_pyfile("config.py")

# fix gunicorn -> docker logging
gunicorn_logger = logging.getLogger('gunicorn.error')
app.logger.handlers = gunicorn_logger.handlers
app.logger.setLevel(gunicorn_logger.level)

cache = Cache(app)

from heckingoodboys import views, commands  # noqa: F401
