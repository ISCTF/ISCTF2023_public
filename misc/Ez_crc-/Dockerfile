FROM python:3.12.0-alpine AS build
RUN apk add --no-cache zip && rm -rf /var/cache/apk/*
FROM python:3.12.0-alpine
COPY --from=build /usr/bin/zip /usr/bin/zip
COPY start.sh /start.sh
COPY task.py /task.py
RUN chmod +x /start.sh
CMD ["/start.sh"]