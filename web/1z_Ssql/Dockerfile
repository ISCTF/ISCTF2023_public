FROM alpine:3.15
RUN apk add apache2 php7 php7-apache2 mariadb php7-mysqli && rm -rf /var/cache/apk/*
COPY init.sql /tmp/init.sql
COPY html /var/www/localhost/htdocs
COPY start.sh /start.sh
COPY my.cnf /etc/mysql/my.cnf
RUN rm -rf /var/www/localhost/htdocs/index.html && chmod +x /start.sh && rm -rf /etc/my.cnf.d/*
CMD ["/start.sh"]