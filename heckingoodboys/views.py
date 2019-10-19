from flask import render_template

from heckingoodboys import app, cache
from heckingoodboys.media import get_media, MEDIA_CACHE_KEY


@app.route('/')
@cache.cached(timeout=3600)
def index():
    all_media = cache.get(MEDIA_CACHE_KEY)
    if all_media is None:
        all_media = get_media()
        cache.set(MEDIA_CACHE_KEY, all_media)

    return render_template("base.html", all_media=all_media)
