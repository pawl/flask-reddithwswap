# heckingoodboys #

Dog slideshow

## Requirements ##

You must get a reddit api client id and secret key. Instructions: https://praw.readthedocs.io/en/latest/getting_started/authentication.html

## Installing ##

    $ python3 -m venv env
    $ source env/bin/activate
    $ pip install -r requirements.txt

## Running locally ##

    REDDIT_CLIENT_ID=<id> REDDIT_CLIENT_SECRET=<secret> FLASK_DEBUG=TRUE flask run

## TODO ##

- Add instructions (swipe right!)
- Download and hash images to prevent duplicates.
- Detect dogs
- Make periodic background task for populating cache.
- Add captions and attribution
- Add paginated api for getting slides
- Fetch more slides (when out of slides)
- Improve ordering of slides (currently random)
- Add tests
- Add menu with settings (filter dog breeds?)
