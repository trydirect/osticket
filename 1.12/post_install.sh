#!/usr/bin/env bash


sudo rm -rf ./src/osTicket-1.12/setup;
sudo chmod 0644 ./src/osTicket-1.12/include/ost-config.php;
docker-compose restart osticket nginx;
# re-login
