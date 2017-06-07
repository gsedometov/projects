#!/usr/bin/env python
from os import getenv
from subprocess import PIPE, Popen, check_call

with open('/root/.pgpass', 'w') as f:
    f.write(':'.join([
        'db', 
        '5432', 
        getenv('REDMINE_DB_DATABASE'), 
        getenv('REDMINE_DB_USERNAME'), 
        getenv('REDMINE_DB_PASSWORD')
        ]))
check_call('chmod 600 /root/.pgpass', shell=True)

def backup_db():
    exitcode = check_call('pg_dump -h {0} {1} > dump.sql'.format('db', getenv('REDMINE_DB_DATABASE')), shell=True)

backup_db()