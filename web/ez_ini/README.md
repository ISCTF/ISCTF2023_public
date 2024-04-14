## 题目名称

ez_ini

## 题目类型

web

## 出题人

Jay17

## 学校

杭州师范大学

## 题目环境

docker

## 题目难度

中

## 题目考点

user.ini配置文件、PHP配置项、伪协议、日志包含、破除定式思维。

## 题目描述

固定思维不可取呀~

## 题目提示

Hint1：注意题目描述哦

Hint2：注意PHP配置项用法，以及.user.ini配置文件正常使用的原理

Hint3：.user.ini文件->文件上传变成文件包含

## 解题思路

.user.ini的奇技淫巧。目的是破除定式思维，使新生加强对php配置文件的理解，对一两年的老生可能是一种挑战。通常选手对此配置文件的认识是：仅可以用来包含文件。其实如果开放了这一配置文件的上传，可以实现很多玩法。

**伪协议：**（这里题目镜像无法修改配置，故不可行）

`php://input `：php://input可以读取没有处理过的POST数据。

```
auto_append_file=php://input
```

然后POST恶意代码就行。

**日志包含：**

nginx下的日志文件路径：`/var/log/nginx/access.log`

```
auto_append_file=/var/log/nginx/access.log
```

--------------------------------

