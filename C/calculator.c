//Write a program to make a simple calculator of two inputs only using switch case.
#include<stdio.h>
#include<stdlib.h>
void addition(int a,int b){
    int sum = a+b;
    printf("Sum of the two num is %d \n",sum);
}
void subtraction(int a,int b){
    int diff = a-b;
    printf("Difference of the two num is %d \n",diff);
}
void multiplication(int a, int b){
    int product = a*b;
    printf("Product of the two num is %d \n",product);
}
void division(int a, int b){
    int quotient = a/b;
    printf("Quoteint of the two num is %d \n",quotient);
}
int main(){
    int a,b;
    int choice;
    while(1){
        printf("Press 1 for addition\n");
        printf("Press 2 for subtraction\n");
        printf("Press 3 for multiplication\n");
        printf("Press 4 for division\n");
        printf("Press 5 for exit\n");
        printf("Enter your choice :- ");
        scanf("%d",&choice);

        switch(choice){
            case 1:
                printf("Enter first number :- ");
                scanf("%d",&a);
                printf("Enter second number :- ");
                scanf("%d",&b);
                addition(a,b);
                break;
            case 2:
                printf("Enter first number :- ");
                scanf("%d",&a);
                printf("Enter second number :- ");
                scanf("%d",&b);
                subtraction(a,b);   
                break;
            case 3:
                printf("Enter first number :- ");
                scanf("%d",&a);
                printf("Enter second number :- ");
                scanf("%d",&b);
                multiplication(a,b);
                break; 
            case 4:
                printf("Enter first number :- ");
                scanf("%d",&a);
                printf("Enter second number :- ");
                scanf("%d",&b);
                division(a,b);
                break;   
            case 5:
                printf("Exiting program...\n");
                exit(0);
            default:
                printf("nashe me ho kya...sahi option choose karo!!!\n");     
        }
    }
    return 0;
}