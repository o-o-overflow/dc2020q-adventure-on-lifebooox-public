FROM python:2.7-alpine

ENV TERM linux


# For example:
run apk update && apk add --no-cache netcat-openbsd bash
COPY requirements.txt /requirements.txt
run pip install -r requirements.txt



COPY exploit1.sh /

COPY check1.py /
COPY check2.sh /


