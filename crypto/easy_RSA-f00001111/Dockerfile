FROM python:3.12-alpine3.18
RUN pip install pycryptodome -i https://pypi.tuna.tsinghua.edu.cn/simple
COPY serve.py /serve.py
CMD ["python3","/serve.py"]
