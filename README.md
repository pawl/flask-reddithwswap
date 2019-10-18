# heckingoodboys #

Dog slideshow

## Requirements ##

You must get a reddit api client id and secret key. Instructions: https://praw.readthedocs.io/en/latest/getting_started/authentication.html

## Installing ##

    $ python3 -m venv env
    $ source env/bin/activate
    $ pip install -r requirements.txt

## Running locally ##

    REDDIT_CLIENT_ID=<id> REDDIT_CLIENT_SECRET=<secret> FLASK_DEBUG=TRUE FLASK_APP=heckingoodboys flask run

## Running tests ##

    python setup.py test

## Deploying ##
```
    $ npm install -g serverless
    $ npm install
    $ sls deploy
```

## TODO ##

- Support v.redd.it and gfycat.com
- Ensure images are working before displaying or show a better "missing image" icon.
- Add instructions (swipe right!)
- Download and hash images to prevent duplicates.
- Detect dogs
- Add captions and attribution
- Add paginated api for getting slides
- Fetch more slides (when out of slides)
- Improve ordering of slides (currently random, which add some variety)
- Add menu with settings (filter dog breeds?)
- Ensure the user doesn't see images they've already seen on next load.
