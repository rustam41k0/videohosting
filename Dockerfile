FROM python:3.10

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/videohosting

COPY ./requirements.txt /usr/src/requirements.txt
RUN pip install --upgrade pip && pip install -r /usr/src/requirements.txt

COPY . /usr/src/videohosting