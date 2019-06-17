#!/usr/bin/env bash

sudo rm -rf app/setup;
sudo chmod 0644 app/include/ost-config.php;
docker-compose restart osticket nginx;
# re-login