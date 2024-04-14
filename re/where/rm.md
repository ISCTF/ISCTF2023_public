## where

***

出题人:pl1rry

![image-20240413224313149](C:\Users\26272\AppData\Roaming\Typora\typora-user-images\image-20240413224313149.png)

![descript](C:/Users/26272/Pictures/media/66359db92b6b847981f04a0b2e308ad6.png)

where解题脚本

```C
//where解题脚本

#include "stdio.h"
#include<string.h>
#include "dataFlag.h"
#include <stdlib.h>


void Tea(unsigned char* str){
	printf("Tea解密中\n");
	unsigned int* box = (unsigned int*) str;
	for(int i = 6; i >= 0; i  = i - 2){
		unsigned int sum=0;
		unsigned int k0 = str[(i + 2) * 4 % 32], k1 = str[(i + 2) * 4 % 32 + 1], k2 = str[(i + 2) * 4 % 32 + 2], k3 = str[(i + 2) * 4 % 32 + 3];
		unsigned int delta=0xDEADBEEF;
		unsigned int l = box[i], r=box[i + 1];
		for(int ii = 0; ii < 32; ii++){
			sum+=delta;
		}
		for(int j = 0; j < 32; j++){
			r-=((l<<4)+k2)^(l+sum)^((l>>5)+k3);
			l-=((r<<4)+k0)^(r+sum)^((r>>5)+k1);
			sum-=delta;
		}
		box[i] = l;
		box[i + 1] = r;
	}
	printf("Tea解密完毕\n");
}

int initST(unsigned char *S, unsigned char *T, unsigned char *K, int len)
{
        int i = 0;

        for(i=0; i<256; i++)
        {
                S[i] = i;
                T[i] = K[i%len];
        }

        return 0;
}

int initS(unsigned char *S, unsigned char *T)
{
        unsigned char tmp = 0x00;
        int i = 0;
        int j = 0;

        for(i=0; i<256; i++)
        {
                j = (j + S[i] + T[i]) % 256;
                tmp = S[j];
                S[j] = S[i];
                S[i] = tmp;
        }

        return 0;
}

int initK(unsigned char *S, unsigned char *K, int len)
{
        unsigned char tmp = 0x00;
        int i = 0;
        int j = 0;
        int r = 0;
        int t = 0;

        for(r=0; r<len; r++)
        {
                i = (i + 1) % 256;
                j = (j + S[i]) % 256;
                tmp = S[j];
                S[j] = S[i];
                S[i] = tmp;
                t = (S[i] + S[j]) % 256;
                K[r] = S[t];
        }
        return 0;
}

int RC4(unsigned char *K, unsigned char *M, unsigned char *E, int len){
        int i = 0;
		unsigned char ans[33] = {0};
		memcpy(ans, M,32);
        for(i=0; i<len; i++){
			if(i == 0){
				E[i] = (M[i] ^ K[i]);
			}else{
				E[i] = (M[i] ^ K[i] ^ ans[K[i] % i]);
			}

        }
        return 0;
}

void RC4_ENC(unsigned char* enc){
		printf("RC4解密中\n");
		unsigned char S[256];
        unsigned char T[256];
        unsigned char K[256];
        unsigned char M[256];
        unsigned char* E = enc;
        unsigned char C[256];
		memset(S, 0x00, sizeof(S));
		memset(T, 0x00, sizeof(T));
        memset(K, 0x00, sizeof(K));
        memset(C, 0x00, sizeof(C));

		strcpy((char*)M, (char*)E);
		itoa(20220222, (char*)K, 8);
        initST(S, T, K, strlen((char*)K));
        initS(S, T);
        initK(S, K, 256);
        RC4(K, M, E, 32);
		printf("RC4解密完毕\n");
}

unsigned char keyMap[] ={241,239,97,187,201,69,87,67,54,235,195,245,97,31,224,237,95,25,195,131,11,103,91,68,122,157,178,126,245,181,34,101};

int main(){
	int index = 0, i = 0, j = 0;
	unsigned char enc[33] = {0};
	for(i = 0; i < 300; i++){
		for(j = 0; j < 300; j++){
			if(TrueMap[i][j] == 1){
				enc[index++] = i;
				enc[index++] = j;
				break;
			}
		}
	}

	for (i = 0; i<32; i++){
		enc[i] ^= keyMap[i];
	}
	Tea(enc);
	RC4_ENC(enc);
	printf("%s",enc);
	getchar();

	return 0;
}

```

```
//dataFlag.h
```

