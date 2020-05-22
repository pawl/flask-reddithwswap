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

## Deploying (serverless) ##
```
    $ npm install -g serverless
    $ npm install
    $ sls deploy
```
