FROM python:2.7

RUN apt-get update && apt-get install -y python-pip
RUN pip install pipenv

COPY ./ /

WORKDIR /vdb

RUN pipenv install

RUN cd app && python app.py