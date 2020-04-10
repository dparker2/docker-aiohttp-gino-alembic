FROM python:3.7.7-slim

ARG requirements=common

ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH /code

RUN mkdir /code
WORKDIR /code

COPY requirements /code/requirements
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    python3-dev \
    && pip install --no-cache-dir -r requirements/${requirements}.txt \
    && rm -rf /var/lib/apt/lists/*

COPY . /code
