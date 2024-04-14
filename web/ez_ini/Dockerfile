FROM alpine:3.15
RUN apk add apache2 php7 php7-apache2 && rm -rf /var/cache/apk/*
COPY index.html /var/www/localhost/htdocs/
COPY upload.php /var/www/localhost/htdocs/
COPY start.sh /start.sh
RUN chmod +x /start.sh
CMD ["/start.sh"]
