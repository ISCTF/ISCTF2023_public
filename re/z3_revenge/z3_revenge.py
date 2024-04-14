import os
import random
flag=os.getenv('FLAG')
os.putenv('FLAG','flag')
code_prev='''#include<stdio.h>
int main(void){
    char flag[200]="";
    printf("Printf input the flag:");
    scanf("%s",flag);
    if(flag[43]=='\\0'){
'''
code = "        if("
def calc(n1,n2,c):
    if c=="+":
        return n1+n2
    elif c=="-":
        return n1-n2
    else:
        return n1*n2

def generate_code(i,n1,c1,n2,c2,c3,num):
    return f"((flag[{i}] {c1} {n1}) {c3} ({n2} {c2} flag[{(i+1)%len(flag)}]) == {num}) && "

def generate_num(i,s1,s2):
    n1=random.randint(100,999)
    n2=random.randint(100,999)
    c1=random.choice("+-*")
    c2=random.choice("+-*")
    c3=random.choice("+-")
    num1=calc(ord(s1),n1,c1)
    num2=calc(n2,ord(s2),c2)
    num3=calc(num1,num2,c3)
    return generate_code(i,n1,c1,n2,c2,c3,num3)

for i in range(len(flag)):
    code+=generate_num(i,flag[i],flag[(i+1)%len(flag)])

code=code[:-4]+")"
code_next='''{
            printf("true\\n");
        }else{
            printf("false\\n");
        }
    }else{
        printf("false\\n");
    }
    return 0;
}
'''
f=open('/z3_revenge.c','w')
f.write(code_prev+code+code_next)
f.close()