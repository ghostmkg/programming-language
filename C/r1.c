#include<stdio.h>
void main()
{
int a,b,temp;
printf("enter the two variables of a and b \n");
scanf( "%d,%d",a,b);
temp=a;
a=b;
b=temp;
printf( "interchanging of two variables is\n");
scanf("%d",temp);
}
