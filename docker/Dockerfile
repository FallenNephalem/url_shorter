FROM python:3.10-slim as runtime

WORKDIR /usr/src/app

ENV APP_PORT 8080
ENV APP_NUM_WORKERS 2
ENV PYTHONPATH /usr/src/app
ENV PYTHONUNBUFFERED TRUE

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt
#RUN apt-get update -y && apt-get install -y gcc libmariadb-dev-compat
#RUN pip install mysqlclient

#FROM runtime as test
#ADD requirements-dev.txt requirements-dev.txt
#RUN pip install -r requirements-dev.txt
#ADD ludaciti ludaciti
#ADD tests tests

FROM runtime
ADD . .
CMD exec uvicorn --workers $APP_NUM_WORKERS --host 0.0.0.0 --port $APP_PORT main:app --reload


#
#FROM python:3.10
#
#WORKDIR /app
#COPY ../requirements.txt requirements.txt
#RUN pip3 install -r requirements.txt
#COPY .. .
#
#CMD exec uvicorn --host 0.0.0.0 --port 8080 main:app --reload
