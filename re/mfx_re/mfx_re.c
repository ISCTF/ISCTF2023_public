#include <stdio.h>
#include <string.h>

int main(void){
    setbuf(stdin,0);
    setbuf(stdout,0);
    printf("Welcome To MFx_Reverse!\n");
    printf("I have two questions. You need guess the flag from the first question.\n");
    int a=1,b=2;
    printf("a=%d, b=%d\n",a,b);
    printf("The first question is a + b = ?\n");
    printf("a + b = ");
    int c=0;
    scanf("%d",&c);
    if(c==3){
        printf("Good!\n");
    }else{
        printf("Wrong!\n");
    }
    printf("The second question is flag = ?\n");
    printf("flag = ");
    char flag[50] = "";
    scanf("%s",flag);
    char real_flag[50] = "{{FLAG}}";
    for(int i=0;i<strlen(flag);i++){
        flag[i] = flag[i] - 1;
    }
    if(strcmp(flag,real_flag)){
        printf("Now you know your flag!\n");
    }else{
        printf("Now you know your flag!\n");
    }
    return 0;
}