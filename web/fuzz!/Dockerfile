FROM ctftraining/base_image_nginx_php_73
# FROM tutum/lamp

# 制作者信息
LABEL Author="Jay17 <3539306573@qq.com>"
LABEL Blog="https://blog.csdn.net/Jayjay___"

RUN rm -r /var/www/html/index.php

COPY ./src/ /var/www/html

RUN chown -R www-data:www-data /var/www/html

COPY ./flag /flaggggggg.txt

#COPY ./service/docker-entrypoint.sh /docker-entrypoint.sh

#RUN chmod +x /docker-entrypoint.sh

#CMD /docker-entrypoint.sh
