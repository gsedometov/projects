FROM alpine

RUN apk update \
    && apk add postgresql python3

ENV PGHOST=db
ENV PGPASSWORD=redmine
ENV PGUSER=redmine

COPY backupdb.sh /bin/backupdb.sh
RUN chmod +x /bin/backupdb.sh
ENTRYPOINT ["/bin/backupdb.sh"]

