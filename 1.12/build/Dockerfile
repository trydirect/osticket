FROM ubuntu:18.04
LABEL maintainer="info@optimum-web.com"

# Let the container know that there is no tty
ENV DEBIAN_FRONTEND noninteractive

ENV APP_VERSION 1.12

RUN apt-get update -y -qq ; apt-get install --no-install-recommends -y -qq supervisor curl software-properties-common; \
    LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php -y; apt-get update -y -qq; \
    apt-get install --no-install-recommends -y -qq cron net-tools sudo lsof \
    php7.2 php7.2-fpm php7.2-mysql php7.2-cli php7.2-cgi \
    php7.2-gd php7.2-zip php7.2-xml php7.2-curl php7.2-imap \
    php7.2-mbstring php7.2-intl php7.2-apcu \
    && apt-get clean; apt-get autoclean; apt-get autoremove -y -qq && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN groupadd -r -g 2000 osticket; useradd -r -u 2000 -g 2000 -m -c "app account" -d /home/osticket -s /bin/bash osticket
RUN curl -L -o /usr/src/app.tar.gz https://github.com/osTicket/osTicket/archive/v${APP_VERSION}.tar.gz
WORKDIR /home/osticket
RUN mkdir -p /var/run/php && chown -R osticket:osticket /var/run/php
RUN tar -xf /usr/src/app.tar.gz && mv osTicket-${APP_VERSION} app
RUN chown -R osticket:osticket app
ADD ./configs/php/fpm/php-fpm.conf /etc/php/7.2/fpm/php-fpm.conf
ADD ./configs/php/fpm/php.ini /etc/php/7.2/fpm/php.ini
ADD ./configs/php/fpm/www.conf /etc/php/7.2/fpm/pool.d/www.conf
ADD ./configs/supervisord/osticket.conf /etc/supervisor/conf.d/osticket.conf

WORKDIR /home/osticket/app
EXPOSE 9000
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/osticket.conf"]
