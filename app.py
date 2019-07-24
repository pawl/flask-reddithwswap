import praw
from flask import Flask, render_template
from flask_caching import Cache

import config

# Flask app
app = Flask(__name__)
app.config.from_pyfile("config.py")

cache_config = {
    'CACHE_TYPE': 'filesystem',
    'CACHE_DIR': 'app_cache'}
cache = Cache(app, config=cache_config)


def parse_image_url(url):
    image_url = None
    if url.endswith(".jpg") or url.endswith(".png"):
        image_url = url
    elif ("imgur.com" in url) and ("/a/" not in url):
        if url.endswith("/new"):
            url = url.rsplit("/", 1)[0]
        imgur_post_id = url.rsplit("/", 1)[1].rsplit(".", 1)[0]
        image_url = "http://i.imgur.com/" + imgur_post_id + ".jpg"
    return image_url


def get_images():
    reddit = praw.Reddit(
        client_id=config.REDDIT_CLIENT_ID,
        client_secret=config.REDDIT_CLIENT_SECRET,
        user_agent='praw')

    reddit_posts = reddit \
        .multireddit('heckingoodboys', 'heckingoodboys') \
        .hot(limit=1000)

    image_urls = set()
    for item in reddit_posts:
        image_url = parse_image_url(item.url)
        if image_url:
            image_urls.add(image_url)
    return image_urls


@app.route('/')
@cache.cached(timeout=86400)
def index():
    image_urls = get_images()
    return render_template("index.html", image_urls=image_urls)


if __name__ == "__main__":
    app.run()
