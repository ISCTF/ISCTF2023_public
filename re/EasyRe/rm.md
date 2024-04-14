## EasyRe
***

出题人：D0UBL3SEV3N

![image-20240413223809247](C:\Users\26272\AppData\Roaming\Typora\typora-user-images\image-20240413223809247.png)

考点:代码理解能力，逆向思维能力

下载附件之后载入 ida64，f5 反编译，查看 main 函数

````c
## EasyRe

***

出题人：D0UBL3SEV3N

考点:代码理解能力，逆向思维能力

下载附件之后载入 ida64，f5 反编译，查看 main 函数

```c
_main();
 strcpy(v4, "]P_ISRF^PCY[I_YWERYC");
 memset(v5, 0, sizeof(v5));
 v6 = 0;
 v7 = 0;
 puts("please input your strings:");
 gets(Str);
 v10 = strlen(Str);
 while ( Str[i] )
 {
 for ( i = 0; i < v10; ++i )
 v8[i] = Str[i] ^ 0x11;
 }
 for ( i = 0; i < v10; ++i )
 {
 if ( v8[i] == 66 || v8[i] == 88 )
 v8[i] = -101 - v8[i];
 }
 for ( i = v10 - 1; i >= 0; --i )
 v8[v10 - i - 1] = v8[i];
 i = 0;
 if ( v10 > 0 )
 {
 if ( v8[i] == v4[i] )
 printf("yes!!!");
 else
 printf("no!!!");
 }
 return 0;
_main();
 strcpy(v4, "]P_ISRF^PCY[I_YWERYC");
 memset(v5, 0, sizeof(v5));
 v6 = 0;
 v7 = 0;
 puts("please input your strings:");
 gets(Str);
 v10 = strlen(Str);
 while ( Str[i] )
 {
 for ( i = 0; i < v10; ++i )
 v8[i] = Str[i] ^ 0x11;
 }
 for ( i = 0; i < v10; ++i )
 {
 if ( v8[i] == 66 || v8[i] == 88 )
 v8[i] = -101 - v8[i];
 }
 for ( i = v10 - 1; i >= 0; --i )
 v8[v10 - i - 1] = v8[i];
 i = 0;
 if ( v10 > 0 )
 {
 if ( v8[i] == v4[i] )
 printf("yes!!!");
 else
 printf("no!!!");
 }
 return 0;
}
```

主函数逻辑是，由用户输入一个字符串，然后将字符串每一个字符与 0x11 异或。异或完了之 后检测字符串中是否有字母 B 和字母 X 因为（66 是 B，88 是 X）如果有就执行 155-66 或者 155-88

实际上这里的目的也就是字符替换

![descript](media/2ea9910ec2585fb41a2c3b41d4bc241d.png)

接着往下，就是倒序经过变换后的字符串。

![descript](media/503010e2cf4601a05d427ecaeec1a8f2.png)

接着到了比较这里：

![descript](media/2e72e08c8c438e6d785c88303e4945cc.png)

显然，是比较 v8 和 v4 两个数组的数据是否完全相同，如果相同那么输出判断 yes，反之判断 no。而 v4 的数据已经给了，v8 又是 flag 经过变化后得到的密文，那么显然密文就是 v4 的数 据，也就是：

![descript](media/0f6e0fd3634b328af3403c870f295118.png)

那么得到密文之后，解题过程就应该和算法反过来，先把这个字符串逆序，然后字符替换，然 后与 0x11 异或，最后输出得到 flag。

解题脚本如下：

```c++
#include <stdio.h>
#include <string.h>
#include <ctype.h>
int main(){
    char String[99];
    int i;
    char s1[99],s2[99];
    printf("please input your strings:\n");
    gets(String);
    int n=strlen(String);
    for(i=n-1;i>=0;i--) //逆序字符串
        s1[n-i-1]=String[i];
    for(i=0;i<strlen(s1);i++){
        if(s1[i] == 'Y' || s1[i]== 'C') //字符替换，因为题目替换的是 B和 X，155-66 是 89，155-88 是 67.所以这里换成 Y 和 C 把 B 和 X 换回来
            s1[i]=0x9b-s1[i];
    }
    for(i=0;i<strlen(s1);i++)
        s2[i]=s1[i]^0x11; //异或运算。
    for(i=0;i<strlen(s2);i++)
        printf("%c",s2[i]); //输出 flag
    return 0;
}

```

![descript](media/d5e2f9ff7de19e14b8d33844cf26b9c2.png)

得到 flag


````

主函数逻辑是，由用户输入一个字符串，然后将字符串每一个字符与 0x11 异或。异或完了之 后检测字符串中是否有字母 B 和字母 X 因为（66 是 B，88 是 X）如果有就执行 155-66 或者 155-88

实际上这里的目的也就是字符替换

![descript](media/2ea9910ec2585fb41a2c3b41d4bc241d.png)

接着往下，就是倒序经过变换后的字符串。

![descript](media/503010e2cf4601a05d427ecaeec1a8f2.png)

接着到了比较这里：

![descript](media/2e72e08c8c438e6d785c88303e4945cc.png)

显然，是比较 v8 和 v4 两个数组的数据是否完全相同，如果相同那么输出判断 yes，反之判断 no。而 v4 的数据已经给了，v8 又是 flag 经过变化后得到的密文，那么显然密文就是 v4 的数 据，也就是：

![descript](media/0f6e0fd3634b328af3403c870f295118.png)

那么得到密文之后，解题过程就应该和算法反过来，先把这个字符串逆序，然后字符替换，然 后与 0x11 异或，最后输出得到 flag。

解题脚本如下：

```c++
#include <stdio.h>
#include <string.h>
#include <ctype.h>
int main(){
    char String[99];
    int i;
    char s1[99],s2[99];
    printf("please input your strings:\n");
    gets(String);
    int n=strlen(String);
    for(i=n-1;i>=0;i--) //逆序字符串
        s1[n-i-1]=String[i];
    for(i=0;i<strlen(s1);i++){
        if(s1[i] == 'Y' || s1[i]== 'C') //字符替换，因为题目替换的是 B和 X，155-66 是 89，155-88 是 67.所以这里换成 Y 和 C 把 B 和 X 换回来
            s1[i]=0x9b-s1[i];
    }
    for(i=0;i<strlen(s1);i++)
        s2[i]=s1[i]^0x11; //异或运算。
    for(i=0;i<strlen(s2);i++)
        printf("%c",s2[i]); //输出 flag
    return 0;
}

```

![descript](media/d5e2f9ff7de19e14b8d33844cf26b9c2.png)

得到 flag