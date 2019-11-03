from heckingoodboys import app, cache
from heckingoodboys.media import get_media, MEDIA_CACHE_KEY


@app.cli.command()
def populate_cache():
    app.logger.info('populating cache...')
    cache.set(MEDIA_CACHE_KEY, get_media())
    app.logger.info('successfully populated cache')
