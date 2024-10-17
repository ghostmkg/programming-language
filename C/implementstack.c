#include<stdio.h>
#define Max 10
int stack[Max];
int top = -1;
void push(int data){
    if(top>Max)
        printf("Stack overflow");
    else{
        top++;
        stack[top] = data;
    }
}
void pop(){
    printf("%d popped from the stack \n", stack[top]);
    top--;
}
void peek(){
    if(top == -1){
        printf("Stack is empty");
    }else{

    printf("%d", stack[top]);
    }
}
int main(){
    push(19);
    push(10);
    pop();
    pop();
    peek();
}