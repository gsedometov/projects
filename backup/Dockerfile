FROM alpine

RUN apk update \
    && apk add postgresql supervisor python3

COPY supervisord.conf /etc/supervisord.conf
COPY backupdb.sh /bin/backupdb.sh
RUN chmod +x /bin/backupdb.sh

ENTRYPOINT ["supervisord", "--nodaemon", "-c", "/etc/supervisord.conf"]

