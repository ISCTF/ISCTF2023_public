FROM alpine:3.15
RUN apk add apache2 php7 php7-apache2 && rm -rf /var/cache/apk/*
COPY index.php /var/www/localhost/htdocs/
COPY flag.php /var/www/localhost/htdocs/
COPY start.sh /start.sh
RUN rm -rf /var/www/localhost/htdocs/index.html && chmod +x /start.sh
CMD ["/start.sh"]