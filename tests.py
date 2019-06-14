#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import time
import docker
import requests

client = docker.from_env()

# Testing build

time.sleep(10)  # we expect all containers are up and running in 20 secs

for c in client.containers.list():
    print("{}: {}" .format(c.name, c.status))
    if 'running' not in c.status:
        print(c.logs())

# php-fpm
app = client.containers.get('osticket')
assert "php-fpm entered RUNNING state" in app.logs()
assert "success: cron entered RUNNING state" in app.logs()


db = client.containers.get('db')
assert db.status == 'running'
cnf = db.exec_run("/usr/sbin/mysqld --verbose  --help")
db_log = db.logs()
assert "mysqld: ready for connections" in db_log.decode()
assert "Version: '5.7" in db_log.decode()

response = requests.get("http://localhost")
assert '<title>osTicket Installer</title>' in response.text
# assert 'osTicket, Customer support system, support ticket system' in response.text
