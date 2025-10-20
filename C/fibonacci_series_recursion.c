/* 
This program generates the Fibonacci series using recursion.
It prompts the user to enter the number of terms in the series,
then computes and displays the Fibonacci numbers up to that term.
*/

/*Fibonacci series- 0  1  1  2  3  5  8  13
where 0 and 1 are fixed and the next number is the sum of the previous two numbers.
*/

#include<stdio.h>
int fib(int n);

void main()
{
    int n,res,i;

    printf("\n enter the value of n: ");
    scanf("%d",&n);

    for(i=0;i<n;i++)
    {
        res=fib(i);  
        printf("%d\t",res);
    }
}

//user-defined function to calculate Fibonacci series
int fib(int n)
{
    if(n==0)
        return 0;
    else if(n==1)
        return 1;
    else 
        return(fib(n-1)+fib(n-2));
}