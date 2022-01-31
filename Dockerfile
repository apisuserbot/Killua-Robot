FROM debian:11
FROM python:3.9.7-slim-buster

RUN apt-get -qq update && apt-get -qq upgrade -y
RUN apt-get -qq install -y \
    git \
    wget \
    python3-pip \
    curl \
    bash \
    neofetch \
    ffmpeg \
    software-properties-common

RUN git clone https://github.com/apisuserbot/Killua-Robot.git /usr/src/KilluaRobot
WORKDIR /usr/src/KilluaRobot

RUN pip3 install --no-cache-dir -U -r requirements.txt

COPY . .
CMD ["python3.9", "-m", "KilluaRobot"]
