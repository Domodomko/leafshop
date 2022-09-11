FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIPENV_CACHE_DIR=/web/app/pipenv_cache

WORKDIR /web/app
COPY requirements.txt /web/app/
RUN pip install -r requirements.txt
RUN apt-get update && apt-get install postgresql-client -y && apt-get install -y binutils libproj-dev gdal-bin gettext libcairo2
COPY . .