FROM python:3.12-alpine3.18
RUN pip install pillow qrcode -i https://mirrors.ustc.edu.cn/pypi/web/simple
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh
COPY ./task.py /task.py
ENTRYPOINT ["/entrypoint.sh"]