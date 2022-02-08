FROM unknownxx/lsf:botmanage
RUN apt-get update -y
WORKDIR /KilluaRobot/
RUN pip3 install --no-cache-dir -U -r requirements.txt
COPY . .
RUN chmod a+x gagalmoveon
CMD ["./gagalmoveon"]
