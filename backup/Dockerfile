FROM alpine

RUN apk update \
    && apk add postgresql supervisor python3 \
    && pip3 install requests

COPY supervisord.conf /etc/supervisord.conf
COPY main.py /bin/main.py
RUN chmod +x /bin/main.py

ENTRYPOINT ["supervisord", "--nodaemon", "-c", "/etc/supervisord.conf"]

