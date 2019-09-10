FROM debian:stretch

WORKDIR /app

ADD . /app

RUN apt-get update
RUN apt-get -y install sudo
RUN apt-get -y install nano
RUN apt-get -y install python3
RUN apt-get -y install python3-pip
RUN apt-get -y install python-dev
RUN pip3 install -r /app/requirements.txt
RUN pip3 install whitenoise

EXPOSE 5001

CMD ["python3", "/app/main.py"]
