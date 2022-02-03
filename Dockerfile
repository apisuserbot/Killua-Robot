FROM unknownxx/lsf:botmanage
RUN apt-get update -y
RUN git clone https://github.com/apisuserbot/Killua-Robot.git /usr/src/KilluaRobot
WORKDIR /usr/src/KilluaRobot
RUN pip3 install --no-cache-dir -U -r requirements.txt
COPY . .
RUN chmod a+x gagalmoveon
CMD ["./gagalmoveon"]
