# docker build -t ubuntu1604py36
FROM ubuntu:16.04

RUN apt-get update && \
        apt-get install -y software-properties-common && \
        add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update -y

RUN apt-get install -y build-essential && \
    apt-get install -y git && \
    apt-get install -y nano && \
    apt-get install -y tk-dev && \
    apt-get install -y netcat && \
    apt-get install -y python3.6 && \
    apt-get install -y python3.6-dev && \
    apt-get install -y python3-pip && \ 
    apt-get install -y python3.6-venv  && \
    apt-get install -y python3.6-tk


# update pip
RUN python3.6 -m pip install pip --upgrade && \
    python3.6 -m pip install wheel

# install pip packages
RUN pip install sanic numpy matplotlib pytest mutmut requests

# set locales
ENV LC_ALL C.UTF-8
ENV LANG C.UTF-8

COPY . /app
WORKDIR "/app"
CMD python3.6 prolog.py
