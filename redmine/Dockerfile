FROM redmine:latest

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    antiword unzip catdoc libwpd-tools libwps-tools gzip unrtf catdvi \
    djview djview3 uuid uuid-dev xz-utils darcs cvs cron

RUN PLUGINS_DIR=/usr/src/redmine/plugins \
    && cd $PLUGINS_DIR \
	&& git clone -b master --single-branch https://github.com/danmunn/redmine_dmsf.git $PLUGINS_DIR/redmine_dmsf 

COPY docker-entrypoint.sh /docker-entrypoint.sh