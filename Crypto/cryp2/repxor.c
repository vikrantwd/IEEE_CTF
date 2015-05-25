#include<stdio.h>
#include<string.h>
main()
{
	char p[20],k[20],c[20];
	int i;
	printf("enter hex string:");
	scanf("%s",p);
	printf("key:");
	scanf("%s",k);
	for(i=0;i<strlen(p);++i)
	{
		c[i]=p[i] ^ k[i%strlen(k)];
	}
	printf("ciphertext:%s",c);
}
