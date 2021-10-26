FROM python:3.10

COPY requirements/ /tmp/requirements/

RUN apt update
RUN apt install vim -y

RUN python -m pip install --upgrade pip
RUN python -m pip install -r /tmp/requirements/base.txt
