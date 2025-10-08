#include<iostream>
#include<climits>
#include<vector>
using namespace std;

void maxProfit (int *prices , int n) {
    if (n <= 1) {
        cout << "max Profit = 0" << endl;
        return;
    }
    
    // Optimized single-pass solution - O(1) space instead of O(n)
    int minPrice = prices[0];
    int maxProfit = 0;
    
    for(int i = 1; i < n; i++) {
        minPrice = min(minPrice, prices[i]);
        int currProfit = prices[i] - minPrice;
        maxProfit = max(maxProfit, currProfit);
    }

    // O(n) Time complexity, O(1) Space complexity
    cout << "max Profit = " << maxProfit << endl;
}

int main (){
    int prices[] = {7, 1, 5, 3, 6, 4};
    int n = sizeof(prices) / sizeof(int);

    maxProfit (prices , n);

    return 0;
}