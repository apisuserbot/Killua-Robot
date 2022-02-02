FROM ubuntu:xenial-20210804
FROM debian:bookworm-20220125-slim
FROM python:3.10.2-slim-buster

# Install Dependencies
RUN apt-get update -y
RUN apt-get install g++ gcc libxml2 libxslt-dev -y

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

RUN chmod a+x gagalmoveon
CMD ["./gagalmoveon"]
