# docker build -t ubuntu1604py36
FROM ubuntu:16.04

RUN apt-get update && \
        apt-get install -y software-properties-common nano tk-dev && \
        add-apt-repository ppa:jonathonf/python-3.6
RUN apt-get update -y

RUN apt-get install -y build-essential netcat python3.6 python3.6-dev python3-pip python3.6-venv python3.6-tk && \
        apt-get install -y git

# update pip
RUN python3.6 -m pip install pip --upgrade && \
        python3.6 -m pip install wheel

# update pip
RUN pip3.6 install sanic numpy matplotlib pytest mutmut requests

COPY . /app
WORKDIR "/app"
CMD python3.6 prolog.py
