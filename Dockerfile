FROM python:3.9-slim-bullseye

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code

CMD ["gunicorn", "heckingoodboys:app", "-c", "gunicorn_config.py"]
