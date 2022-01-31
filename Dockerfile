FROM debian:11
FROM python:3.9.7-slim-buster

RUN git clone https://github.com/apisuserbot/Killua-Robot.git /KilluaRobot
WORKDIR /KilluaRobot/

RUN apt-get -qq update && apt-get -qq upgrade -y
RUN apt-get -y install git
RUN python3.9 -m pip install -U pip
RUN apt-get -qq install -y \
    wget \
    python3-pip \
    curl \
    bash \
    neofetch \
    ffmpeg \
    software-properties-common

COPY requirements.txt .

RUN pip3 install wheel
RUN pip3 install -U -r requirements.txt

COPY . .
CMD ["python3.9", "-m", "KilluaRobot"]
