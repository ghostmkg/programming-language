#include <stdio.h>
#include <limits.h>
#include <stdbool.h>
#define capacity 5
typedef struct queue
{
    int data[capacity];
    int front;
    int rear;
    int current_size;
} queue;
void initialise(queue *q)
{
    q->front = -1;
    q->rear = -1;
    q->current_size=0;
}
bool empty(queue *q)
{
    return (q->front == -1 && q->rear == -1);
    //can also use currentsize==0
}
bool full(queue *q)
{
    return (q->front == (q->rear + 1) % capacity);
    //can also use currentsize==capacity
}
int enqueue(queue *q, int a)
{
    if (full(q))
        {
            printf("QUEUE IS FULL\n");
            return INT_MAX;
        }
    if (empty(q))
        q->front = 0;
    q->rear = (q->rear + 1) % capacity;
    q->data[q->rear] = a;
    q->current_size++;
    return a;
}
int dequeue(queue *q)
{
    if (empty(q))
    {
        printf("QUEUE IS EMPTY\n");
        return INT_MIN;
    }
    int a = q->data[q->front];
    q->front = (q->front + 1) % capacity;
    q->current_size--;
    if (q->current_size==0)
        initialise(q);
    return a;
}
int main()
{
    queue q1;
    initialise(&q1);
    printf("enqueued:%d\n",enqueue(&q1,5));
    printf("enqueued:%d\n",enqueue(&q1,15));
    printf("enqueued:%d\n",enqueue(&q1,25));
    printf("enqueued:%d\n",enqueue(&q1,35));
    printf("current size = %d\n",q1.current_size);
    printf("enqueued:%d\n",enqueue(&q1,45));
    printf("%d\n",enqueue(&q1,55));
    printf("dequeued:%d\n",dequeue(&q1));
    printf("dequeued:%d\n",dequeue(&q1));
    printf("dequeued:%d\n",dequeue(&q1));
    printf("current size = %d\n",q1.current_size);
    printf("dequeued:%d\n",dequeue(&q1));
    printf("dequeued:%d\n",dequeue(&q1));
    printf("%d\n",dequeue(&q1));
    printf("enqueued:%d\n",enqueue(&q1,65));
    printf("enqueued:%d\n\n",enqueue(&q1,75));
    for (int i = 0; i < q1.current_size; i++)
    {
        printf("element %d in queue is %d\n",i+1,q1.data[i]);
    }
    
    return 0;
}

//output is
/*
enqueued:5
enqueued:15
enqueued:25
enqueued:35
current size = 4
enqueued:45
QUEUE IS FULL
2147483647
dequeued:5
dequeued:15
dequeued:25
current size = 2
dequeued:35
dequeued:45
QUEUE IS EMPTY
-2147483648
enqueued:65
enqueued:75

element 1 in queue is 65
element 2 in queue is 75
*/