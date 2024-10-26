#include <stdio.h>
#include <stdlib.h>
#define size 100

struct stack {
    int a[size];
    int top;
};

void init_Stack(struct stack *s){
    s->top = -1;
}

void pop(struct stack *s){
    if(s->top == -1){
        printf("Stack is Already Empty\n");
    } else {
        s->a[s->top] = 0;
        (s->top)--;
    }
}

void push(struct stack *s, int data){
    if (s->top == size - 1){
        printf("Stack is Full\n");
    } else {
        (s->top)++;
        s->a[s->top] = data;
        printf("Data Added\n");
    }
}

int main(){
    struct stack sv;

    init_Stack(&sv);
    
    int pos, choice, data;

    while(1){
        printf("1. Push\n");
        printf("2. Pop\n");
        printf("3. Display Stack\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        switch(choice){
            case 1:
                printf("Enter the data to be added: ");
                scanf("%d", &data);
                push(&sv, data);
                break;
            case 2:
                pop(&sv);
                printf("Popped value\n");
                break;
            case 3:
                printf("Display\n");
                break;
            case 4:
                exit(0);
        }
    }

    return 0;
}