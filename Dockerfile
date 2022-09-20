FROM python:3.10-alpine
WORKDIR /rest/
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev
COPY requirements.txt /rest/
RUN pip install -r requirements.txt
COPY . /rest/
