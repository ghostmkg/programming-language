// Solution of Nth Sum Problem in C
/*
Problem Statement:
There is a series, S , where the next term is the sum of pervious three terms. Given the first three terms of the series, a, b, and c respectively, you have to output the nth term of the series using recursion.
*/

#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>

int sum=0,i=0;


int find_nth_term(int n, int a, int b, int c) {

  if (n == 3) return c;
  if (n == 2) return b;
  if (n == 1) return a;
  int s = a + b + c;
  return find_nth_term(n-1, b, c, s);
}
int main() {
    int n, a, b, c;
  
    scanf("%d %d %d %d", &n, &a, &b, &c);
    int ans = find_nth_term(n, a, b, c);
 
    printf("%d", ans); 
    return 0;
}
