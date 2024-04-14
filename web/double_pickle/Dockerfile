FROM python:3.7-slim-bullseye

# 制作者信息
LABEL Author="Jay17 <3539306573@qq.com>"
LABEL Blog="https://blog.csdn.net/Jayjay___"

# 安装必要的python依赖库
# RUN sage --python -m pip install flask
# RUN sage --python -m pip install pybase64
RUN python3 -m pip install -i https://pypi.tuna.tsinghua.edu.cn/simple \flask

# 拷贝源码和启动脚本至根目录
COPY ./src/ /app
COPY ./service/docker-entrypoint.sh /

EXPOSE 8080
ENTRYPOINT ["/bin/bash","/docker-entrypoint.sh"]
