#include<stdio.h>
struct vector{
    int x;
    int y;
}v1,v2;
struct vector add(struct vector a,struct vector b);
int main()
{
    v1.x=3;
    v1.y=4;
    v2.x=6;
    v2.y=2;
    printf("sum is {%d,%d}",add(v1,v2));

}
struct vector add(struct vector a,struct vector b)
{
    struct vector sum;
    sum.x=a.x+b.x;
    sum.y=a.y+b.y;
    return sum;
}