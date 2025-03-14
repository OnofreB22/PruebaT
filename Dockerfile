FROM python:3.13.0-alpine3.20
LABEL maintainer="oabenjumev@gmail.com"

ENV PYTHONUBUFFERED=1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

RUN apk add --no-cache \
        postgresql-client \
        postgresql-dev \
        postgis \
        gdal \
        gdal-dev \
        geos \
        geos-dev \
    && python -m venv /py \
    && /py/bin/pip install --upgrade pip \
    && /py/bin/pip install -r /tmp/requirements.txt \
    && rm -rf /tmp \
    && adduser \
        --disabled-password \
        --no-create-home \
        django-user

ENV PATH="/py/bin:$PATH"

USER django-user