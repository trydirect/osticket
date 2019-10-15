[![Build Status](https://travis-ci.com/trydirect/osticket.svg?branch=master)](https://travis-ci.com/trydirect/osticket)
![Docker Stars](https://img.shields.io/docker/stars/trydirect/osticket.svg)
![Docker Pulls](https://img.shields.io/docker/pulls/trydirect/osticket.svg)
![Docker Automated](https://img.shields.io/docker/cloud/automated/trydirect/osticket.svg)
![Docker Build](https://img.shields.io/docker/cloud/build/trydirect/osticket.svg)
[![Gitter chat](https://badges.gitter.im/trydirect/community.png)](https://gitter.im/try-direct/community)


# osTicket development template.
osTicket development template - project generator/development environment.
Can be used by PHP developers to start quickly on development osTicket modules.
This stack allows you to setup development environment in a single docker-compose command

## Stack includes

- Ubuntu 18.04 docker image
- PHP 7.2-FPM,
- osTicket 
- NGINX
- MySQL 5.7
- memcache (disabled by default)

## Note
Before installing this project, please, make sure you have installed docker and docker-compose

To install docker execute: 
```sh
$ curl -fsSL https://get.docker.com -o get-docker.sh
$ sh get-docker.sh
$ pip install docker-compose
```
## Installation
Clone this project into your work directory:
```sh
$ git clone https://github.com/trydirect/osticket.git
```

## Post installation
At the last step please run following command.

```
./post_install.sh    #this will remove setup directory and set permissions on config file.
```

Finally you have to re-login to get rid of osTicket secuirty alert message. 


## Quick deployment to cloud
##### Amazon AWS, Digital Ocean, Hetzner and others
[<img src="https://img.shields.io/badge/quick%20deploy-%40try.direct-brightgreen.svg">](https://try.direct/server/user/deploy/Im9zdGlja2V0fDZ8MzUi.EIJLoA.SohvaToLZXpcBHu_Ne--FTZvHD8/)



# Contributing

1. Fork it (https://github.com/trydirect/osticket/fork)
2. Create your feature branch (git checkout -b feature/fooBar)
3. Commit your changes (git commit -am 'Add some fooBar')
4. Push to the branch (git push origin feature/fooBar)
5. Create a new Pull Request



# Support Development

[![Donate](https://img.shields.io/badge/Donate-PayPal-green.svg)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=2BH8ED2AUU2RL)
