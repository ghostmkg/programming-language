//The 0/1 knapsack problem means that the items are either completely or no items are filled in a knapsack//
#include<stdio.h>
int max(int a,int b){
    if(a>b) return a;
    else return b;
}
int knapsack(int capacity, int weights[],int values[],int n){
    int dp[n+1][capacity+1];
    for(int i=0;i<=n;i++){
        for(int w=0;w<=capacity;w++){
            if(i==0||w==0)
            dp[i][w]=0;
        else if (weights[i-1]<=w)
            dp[i][w]=max(values[i-1]+dp[i-1][w-weights[i-1]],dp[i-1][w]);
        else
            dp[i][w]=dp[i-1][w];
            printf("%d",dp[i][w]);


        }
        printf("\n");
        printf("the max profit value of %d row is %d", i,dp[i][capacity]);
        printf("\n");

    }
    return dp[n][capacity];
}
int main(){
    int values[]={6,10,12};
    int weights[]={1,2,3};
    int capacity=5;
    int n=sizeof(values)/sizeof(values[0]);
    int maxValue=knapsack(capacity,weights,values,n);
    printf("\n");
    printf("Maximum value in knapsack = %d\n",maxValue);
    return 0;
}
