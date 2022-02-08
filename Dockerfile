FROM unknownxx/lsf:botmanage
RUN pip3 install --no-cache-dir -U -r requirements.txt
COPY . .
RUN chmod a+x gagalmoveon
CMD ["./gagalmoveon"]
