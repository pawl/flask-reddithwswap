from logging.config import dictConfig

from flask import Flask
from flask_caching import Cache

app = Flask(__name__)
app.config.from_pyfile("config.py")

# configure root logger to fix gunicorn -> docker logging
dictConfig({
    'version': 1,
    'formatters': {'default': {
        'format': '[%(asctime)s] %(levelname)s in %(module)s: %(message)s',
    }},
    'handlers': {'wsgi': {
        'class': 'logging.StreamHandler',
        'stream': 'ext://flask.logging.wsgi_errors_stream',
        'formatter': 'default'
    }},
    'root': {
        'level': 'INFO',
        'handlers': ['wsgi']
    }
})

cache = Cache(app)

from heckingoodboys import views, commands  # noqa: F401
