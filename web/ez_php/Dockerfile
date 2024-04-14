#FROM php:7.4-apache

#COPY _files/html /var/www/html
#ENV FLAG="flag{thIS_ZZY_php}"
#COPY _files/start.sh /root/start.sh
#RUN chmod +x /root/start.sh
#RUN mkdir /tmp/users
#RUN chmod -R 777 /tmp/users
#RUN chmod -R 755 /var/www/html/
#COPY _files/built_in_user_for_check /tmp/users/built_in_user_for_check
#COPY _files/file_for_check.txt /file_for_check.txt
#RUN chmod 655 /file_for_check.txt


#EXPOSE 80
#ENTRYPOINT ["/root/start.sh"]
FROM php:7.4-apache

COPY _files/html /var/www/html
#ENV FLAG="flag{thIS_ZZY_php}"
COPY _files/start.sh /root/start.sh
RUN chmod +x /root/start.sh
RUN mkdir /tmp/users
RUN chmod -R 777 /tmp/users
RUN chmod -R 755 /var/www/html/
COPY _files/built_in_user_for_check /tmp/users/built_in_user_for_check
COPY _files/file_for_check.txt /file_for_check.txt
RUN chmod 655 /file_for_check.txt


EXPOSE 80
ENTRYPOINT ["/root/start.sh"]
