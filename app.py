import praw
from flask import Flask, render_template
from flask_caching import Cache

import config

app = Flask(__name__)
app.config.from_pyfile("config.py")


cache_config = {'CACHE_DIR': 'app_cache'}
if app.debug:
    cache_config['CACHE_TYPE'] = 'null'
else:
    cache_config['CACHE_TYPE'] = 'filesystem'
cache = Cache(app, config=cache_config)


def parse_image_url(item):
    """Parses the reddit post url and return an image url if it's an image"""
    url = item.url

    image_url = None
    if hasattr(item, "preview"):
        image_url = item.preview['images'][0]['source']['url']
    # disable non-reddit/imgur urls for now (to optimize mobile load speed)
    # elif url.endswith((".jpg", ".png", ".jpeg")):
    #     image_url = url
    elif ("imgur.com" in url) and ("/a/" not in url):
        if url.endswith("/new"):
            url = url.rsplit("/", 1)[0]
        imgur_post_id = url.rsplit("/", 1)[1].rsplit(".", 1)[0]
        # h = Huge Thumbnail (1024x1024)
        image_url = "http://i.imgur.com/" + imgur_post_id + "h.jpg"
    return image_url


def get_images():
    """Gets image urls from reddit."""
    reddit = praw.Reddit(
        client_id=config.REDDIT_CLIENT_ID,
        client_secret=config.REDDIT_CLIENT_SECRET,
        user_agent='praw')

    limit = 100 if app.debug else 1000
    reddit_posts = reddit \
        .multireddit('heckingoodboys', 'heckingoodboys') \
        .hot(limit=limit)

    image_urls = set()
    for item in reddit_posts:
        image_url = parse_image_url(item)
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
