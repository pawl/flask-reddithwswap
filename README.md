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

## Deploying (docker-compose) ##
[Install docker](https://docs.docker.com/get-docker/) and run:
1. `cp .env.acme-companion.example .env.acme-companion`
1. In the new `.env.acme-companion` file, fill in your `DEFAULT_EMAIL`
1. `cp .env.example .env`
1. In the new `.env` file, fill in your `REDDIT_CLIENT_ID` and `REDDIT_CLIENT_SECRET`.
1. `docker-compose up`
