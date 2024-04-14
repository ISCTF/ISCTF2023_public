FROM php:7.3-fpm-alpine

COPY _files /tmp/
COPY src /var/www/html

RUN sed -i 's/dl-cdn.alpinelinux.org/mirror.tuna.tsinghua.edu.cn/g' /etc/apk/repositories \
    && apk add --update --no-cache netcat-openbsd socat bash sudo tar openrc nginx mysql mysql-client libpng libpng-dev freetype freetype-dev libjpeg-turbo libjpeg-turbo-dev libstdc++ \
    #&& mkdir /run/nginx \
    #&& adduser mysql -G root \
    && docker-php-source extract \
    && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-dir=/usr/include/\
    && docker-php-ext-install gd \
    && apk del libpng-dev freetype-dev libjpeg-turbo-dev \
    # mysql ext
    && docker-php-source extract \
    && docker-php-ext-install pdo_mysql mysqli \
    && docker-php-source delete \
    # init mysql
    && mysql_install_db --user=mysql --datadir=/var/lib/mysql \
    && sh -c "mysqld_safe & " \
    #&& mysqld_safe --secure-file-priv=''  \
    && sleep 5s \
    && ls -al \
    && mysqladmin -uroot password '4yWz8eu7HgNQVjD0' \
    && mysql -e "source /var/www/html/db.sql;" -uroot -p4yWz8eu7HgNQVjD0 \
    && mysql -e "source /var/www/html/db2.sql;" -uroot -p4yWz8eu7HgNQVjD0 \
    # configure file
    && mv /tmp/flag.sh /flag.sh \
    && mv -f /tmp/sudoers /etc/sudoers \
    && mv -f /tmp/menu /bin/menu \
    && chmod 755 /bin/menu \
    && mv -f /tmp/group /etc/group \
    && mv /tmp/docker-php-entrypoint /usr/local/bin/docker-php-entrypoint \
    && chmod +x /usr/local/bin/docker-php-entrypoint \
    && mv /tmp/nginx.conf /etc/nginx/nginx.conf \
    && chown -R www-data:www-data /var/www/html \    
    && mv /tmp/docker-php-ext-mysqli.ini /usr/local/etc/php/conf.d \
    && mv /tmp/docker-php-ext-pdo_mysql.ini /usr/local/etc/php/conf.d \
    && mv /tmp/glibc-2.30-r0.apk / \
    && mv /tmp/sgerrand.rsa.pub /etc/apk/keys/sgerrand.rsa.pub \
    && apk add --no-cache /glibc-2.30-r0.apk \
    # clear
    && rm -rf /glibc-2.30-r0.apk \
    && docker-php-source delete \
    && rm -rf /var/www/html/db.sql \
    && rm -rf /var/www/html/db2.sql \
    && rm -rf /tmp/* 

WORKDIR /var/www/html

EXPOSE 80

VOLUME ["/var/log/nginx"]

CMD ["/bin/bash", "-c", "docker-php-entrypoint"]
