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


class Media:
    """Image or video to be displayed on a slide."""
    title = None
    image_url = None
    video_url = None
    permalink = None

    def __init__(self, reddit_post):
        self.title = reddit_post.title
        self.permalink = reddit_post.permalink

        # determine the reddit post's image or video url, if it has one
        # TODO: support https://v.redd.it/i1058cwgfac31
        # TODO: support https://gfycat.com/welldocumentedunderstatedchevrotain
        url = reddit_post.url
        if ("imgur.com" in url) and url.endswith(".gifv"):
            # imgur gifv
            # just removing "v" from gifv doesn't work, need to use mp4 video
            self.video_url = url[:-4] + 'mp4'
        elif ("imgur.com" not in url) and url.endswith((".jpg", ".png", ".jpeg")):
            # non-imgur images (example: https://i.redd.it/f52s327v59c31.jpg)
            # only support images with previews
            if hasattr(reddit_post, "preview"):
                self.image_url = reddit_post.preview['images'][0]['source']['url']
        elif ("imgur.com" in url) and ("/a/" not in url):
            # imgur images (example: https://imgur.com/X5Jl2xd)
            if url.endswith("/new"):
                url = url.rsplit("/", 1)[0]
            imgur_post_id = url.rsplit("/", 1)[1].rsplit(".", 1)[0]
            # h = Huge Thumbnail (1024x1024)
            self.image_url = "http://i.imgur.com/" + imgur_post_id + "h.jpg"

    def __hash__(self):
        """Makes this class unique in a set()."""
        return hash((self.title,))


def get_media():
    """Gets image and video urls from reddit."""
    reddit = praw.Reddit(
        client_id=config.REDDIT_CLIENT_ID,
        client_secret=config.REDDIT_CLIENT_SECRET,
        user_agent='praw')

    limit = 100 if app.debug else 1000
    reddit_posts = reddit \
        .multireddit('heckingoodboys', 'heckingoodboys') \
        .hot(limit=limit)

    all_media = set()
    for reddit_post in reddit_posts:
        media = Media(reddit_post)
        if media.video_url or media.image_url:
            all_media.add(media)
    return all_media


@app.route('/')
@cache.cached(timeout=3600)
def index():
    all_media = get_media()
    return render_template("index.html", all_media=all_media)


if __name__ == "__main__":
    app.run()
