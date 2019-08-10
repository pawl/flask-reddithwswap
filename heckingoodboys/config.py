import os

REDDIT_CLIENT_ID = os.environ.get('REDDIT_CLIENT_ID')
REDDIT_CLIENT_SECRET = os.environ.get('REDDIT_CLIENT_SECRET')

CACHE_REDIS_URL = os.environ.get('REDIS_URL')
CACHE_TYPE = 'redis' if CACHE_REDIS_URL else 'null'
