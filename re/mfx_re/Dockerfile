FROM python:3.11-alpine3.18
RUN apk update && apk add --no-cache gcc musl-dev && rm -rf /var/cache/apk/*
COPY start.sh /
COPY upx /
COPY mfx_re.c /
RUN chmod +x /start.sh && chmod +x /upx
CMD ["/bin/sh","/start.sh"]
