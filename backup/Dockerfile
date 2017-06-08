FROM alpine

RUN apk update \
    && apk add postgresql supervisor python3 \
    && pip3 install requests

COPY supervisord.conf /etc/supervisord.conf
COPY backupdb /bin/backupdb
RUN chmod +x /bin/backupdb

ENTRYPOINT ["supervisord", "--nodaemon", "-c", "/etc/supervisord.conf"]

