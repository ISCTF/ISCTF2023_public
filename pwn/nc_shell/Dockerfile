FROM debian:testing-slim

RUN apt-get update && \
    apt-get install -y xinetd && \
    rm -rf /var/cache/apt/archives/* && \
    useradd -m ctf

COPY ctf.xinetd /etc/xinetd.d/ctf
COPY pwn /home/ctf/pwn
COPY start.sh /start.sh

RUN mkdir /home/ctf/dev && \
    mknod /home/ctf/dev/null c 1 3 && \
    mknod /home/ctf/dev/zero c 1 5 && \
    mknod /home/ctf/dev/random c 1 8 && \
    mknod /home/ctf/dev/urandom c 1 9 && \
    chmod 666 /home/ctf/dev/* && \
    mkdir /home/ctf/bin && \
    cp /bin/sh /home/ctf/bin && \
    cp /bin/ls /home/ctf/bin && \
    cp /bin/cat /home/ctf/bin && \
    cp -R /usr/lib* /home/ctf && \
    echo "Blocked by ctf_xinetd" > /etc/banner_fail && \
    echo flag > /home/ctf/flag && \
    chown -R root:ctf /home/ctf && \
    chmod -R 750 /home/ctf && \
    chmod 740 /home/ctf/flag && \
    chmod +x /start.sh

CMD ["/start.sh"]