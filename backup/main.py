#!/usr/bin/env python3
import asyncio
import logging
import os
import shutil
import subprocess
import sys
import time

import requests

log = logging.getLogger(__name__)
stream_handler = logging.StreamHandler(sys.stderr)
log.addHandler(stream_handler)

def wait_redmine():
    while True:
        try:
            resp = requests.get('http://projects:3000', timeout=10)
            if resp.status_code == 200:
                return
        except Exception as e:  #pylint: disable=broad-except
            log.warning(e)
            time.sleep(10)

BACKUP_PATH = '/backups/dump.db'

async def backup_db():
    if os.path.isfile(BACKUP_PATH):
        os.rename(BACKUP_PATH, BACKUP_PATH+'.old')
    subprocess.check_call('pg_dump > /backups/dump.db', shell=True)

async def backup_files():
    shutil.make_archive('/backups/files', 'gztar', base_dir='/files')

def main():
    loop = asyncio.get_event_loop()
    wait_redmine()
    while True:
        loop.run_until_complete(
            asyncio.gather(
                backup_db(),
                backup_files(),
            ))
        time.sleep(20)

if __name__ == '__main__':
    main()

