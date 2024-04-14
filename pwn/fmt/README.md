在当前目录下，利用终端执行

```sh
sudo docker build -t "ctf/alloca" .
```

之后，启动镜像

```sh
sudo docker run  -p 10005:9999 -itd ctf/alloca
```

其中， 10005 是映射端口，可以更改

测试是否成功

```
nc 127.0.0.1 10005
```

