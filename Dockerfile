FROM python:3.9.18-alpine3.19

LABEL maintainer="Spikey"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /requirements.txt
COPY ./TaskManager /TaskManager

WORKDIR /TaskManager
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /requirements.txt && \
    adduser --disable-password --no-create-home app

ENV PATH="/py/bin:$PATH"

USER app

