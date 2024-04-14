FROM ubuntu:22.04

RUN sed -i "s/http:\/\/archive.ubuntu.com/http:\/\/mirrors.tuna.tsinghua.edu.cn/g" /etc/apt/sources.list && \
    apt-get update && apt-get -y dist-upgrade && \
    apt-get install -y lib32z1 xinetd vim net-tools gcc && \
    useradd -m ctf

WORKDIR /home/ctf

COPY ./ctf.xinetd /tmp/xinetd.d/ctf
COPY ./start.sh /tmp/start.sh
COPY ./bin/ /tmp/ctf/test/
#COPY ./bin/ /home/ctf/
#COPY ./ctf.xinetd /etc/xinetd.d/ctf
#COPY ./start.sh /start.sh

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
    cp /tmp/xinetd.d/ctf /etc/xinetd.d/ctf && \
    cp -R /usr/lib* /home/ctf && \
    ls /tmp/ctf/test/ -al && \
    cp /tmp/ctf/test/f* /home/ctf/ && \
    ls /home/ctf/ -al&& \
    cp /tmp/start.sh /start.sh && \
    echo "Blocked by ctf_xinetd" > /etc/banner_fail && \
    chmod +x /start.sh && \
    chown -R root:ctf /home/ctf && \
    chmod -R 750 /home/ctf && \
    ls /home/ctf/ -al&& \
    cat flag && \
    chmod 740 /home/ctf/flag && \
    rm -rf /tmp/



CMD ["/start.sh"]

EXPOSE 8080
