FROM ubuntu:18.04

MAINTAINER Optimum <info@optimum-web.com>

ENV OST_VERSION 1.10.4

RUN apt-get update -y -qq ; apt-get install --no-install-recommends -y -qq software-properties-common; \
    LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php -y; apt-get update -y -qq; \
    apt-get install -y -qq sudo supervisor cron unzip curl net-tools \
    php7.2 php7.2-fpm php7.2-mysql php7.2-cli php7.2-cgi php7.2-gd php7.2-zip php7.2-xml php7.2-curl \
    && apt-get clean; apt-get autoclean; apt-get autoremove -y -qq && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN groupadd -r -g 2000 osticket; useradd -r -u 2000 -g 2000 -m -c "app account" -d /home/osticket -s /bin/bash osticket;

COPY ./src/osTicket-v${OST_VERSION}.zip /usr/src
RUN unzip -qq /usr/src/osTicket-v${OST_VERSION}.zip -d /usr/src
ADD ./configs/php/fpm/php.ini /etc/php/7.2/fpm/php.ini
ADD ./configs/php/fpm/www.conf /etc/php/7.2/fpm/pool.d/www.conf
ADD ./configs/supervisord/ost.conf /etc/supervisor/conf.d/ost.conf
RUN mkdir /run/php
RUN chown www-data:www-data /run/php
