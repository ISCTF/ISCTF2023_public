## easy_flower_tea

***

出题人：her01st

![image-20240413223713456](C:\Users\26272\AppData\Roaming\Typora\typora-user-images\image-20240413223713456.png)

正常步骤，先查壳，丢经die可以发现，该程序是无壳，32位程序

![屏幕截图 2023-11-17 102853](C:/Users/26272/Pictures/media/c84f47ab815e1ea5c761dec685714761.png)

丢进对应ida中，进入main函数，尝试tab，显示无法反编译，仔细阅读汇编，发现一个永恒跳的混淆指令，一个简单的花指令，那么我们要修复程序，进行手动去除花指令

![屏幕截图 2023-11-17 103518](C:/Users/26272/Pictures/media/5347b008eacccb06fcbb5d1e3028029d.png)

选中0041272D到00412739，ctrl+n 将其nop掉，如何光标指向0041272D，按快捷键u取消定义，在按p变为函数，在按tab发现以及可以正常进行反编译

![屏幕截图 2023-11-17 103800](C:/Users/26272/Pictures/media/72c4c2d5404f31b143f6602e59998acb.png)![屏幕截图 2023-11-17 103842](C:/Users/26272/Pictures/media/4484a084e638398ab1b093a38ecdfeaa.png)![屏幕截图 2023-11-17 103856](C:/Users/26272/Pictures/media/b8198d5176ffedc774f3411229510bd3.png)

进入函数后，可以发现一个未知函数，以及两个比较，进入未知函数

![屏幕截图 2023-11-17 103912](C:/Users/26272/Pictures/media/72fdcb71e8ea8a56285f3edaf5188c55.png)

可以发现未知函数是一个加密函数且前面有一长串赋值为12,34,56,78，有tea算法特征，通过比较tea算法，可以得知该tea未被魔改，那么通过整体代码逻辑可以得知，该程序通过用户输入的数字，通过tea加密后与1115126522以及2014982346进行比较，从而得出正确结论

![屏幕截图 2023-11-17 103518](C:/Users/26272/Pictures/media/f91ad9392e610537dca07b1388e66668.png)

![屏幕截图 2023-11-17 104107](C:/Users/26272/Pictures/media/eee10e7e36c212ff950c78334cf95280.png)

那么就可以得知1115126522以及2014982346就是我们要找的密文，有秘钥以及密文然后就开始脚本解密

![屏幕截图 2023-11-17 104122](C:/Users/26272/Pictures/media/84792c737aa8addfab43247571a7e4c0.png)

![屏幕截图 2023-11-17 111202](C:/Users/26272/Pictures/media/18dd24950aac7fc2716e35ebf12eda35.png)

便可以得到1472353 3847872，然后用ISCTF{}包裹上提交即可