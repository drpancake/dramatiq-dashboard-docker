FROM python:3.8.2-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV APP_HOME=/home/app

# User and working dir
RUN mkdir -p $APP_HOME
RUN addgroup -S app && adduser -S -G app app
WORKDIR $APP_HOME

# Needed to build bjoern
RUN apk update && apk add musl-dev gcc libev-dev

# Dependencies
RUN pip install --upgrade pip
COPY requirements.txt $APP_HOME/requirements.txt
RUN pip install --no-cache-dir -r $APP_HOME/requirements.txt

COPY app.py $APP_HOME/
RUN chown -R app:app $APP_HOME
USER app

ENTRYPOINT ["./app.py"]