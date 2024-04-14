FROM python:3.12-alpine3.18
RUN apk add gcc musl-dev && rm -rf /var/cache/apk/*
COPY z3_revenge.py /z3_revenge.py
COPY start.sh /start.sh
RUN chmod +x /start.sh
CMD ["/bin/sh","/start.sh"]