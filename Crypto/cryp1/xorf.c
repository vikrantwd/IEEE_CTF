#include<stdio.h>
#include<string.h>
main()
{
	char s1[20],s2[20],s3[20];
	printf("String 1:");
	scanf("%s",s1);
	printf("String 2:");
	scanf("%s",s2);
	int i=0;
	for(i=0;i<strlen(s1);++i)
	{
		s3[i]=s1[i]^s2[i];
	}
	printf("%s",s3);
}
