FROM ubuntu:20.04
WORKDIR /

ENV TZ=Asia/Shanghai
COPY ./requirements.txt /requirements.txt

RUN apt-get update -y && \  
    apt-get install -y python3-pip python3-dev && \
    pip3 config set global.index-url https://mirrors.aliyun.com/pypi/simple/ && \
    python3 --version && \ 
    pip3 install --upgrade pip && \
    pip3 install -r requirements.txt  && \
    ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && \
    echo $TZ > /etc/timezone


COPY ./src /
## 使用gunicorn
CMD ["python3", "./app.py"]

## 若不使用gunicorn, 可将 CMD ["gunicorn"...] 替换成下面2行命令
# ENTRYPOINT [ "python3" ]
# CMD [ "app.py" ]  # 不使用gunicorn, 直接python运行app.py

