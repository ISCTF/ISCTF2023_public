#include <stdio.h>
#include <string.h>
#include <ctype.h>
int main()
{
	int i;
	char String[99];
	char s1[99];
	char s2[99]="]P_ISR\F^PCY[I_YWERYC"; 
	printf("please input your strings:\n");
	gets(String);
	int n=strlen(String);
	while(String[i] != '\0'){
		for(i=0;i<n;i++)
			s1[i]=String[i]^0x11;
	}
	for(i=0;i<n;i++){
		if(s1[i] == 'B' || s1[i] == 'X')
			s1[i]=0x9b-s1[i];
	}
	for(i=n-1;i>=0;i--)
		s1[n-i-1]=s1[i];
	for(i=0;i<n;i++){
		if(s1[i]==s2[i]){
			printf("yes!!!");
			break;
		}
		else{
			printf("no!!!"); 
			break;
		}
	}
	return 0;
}
