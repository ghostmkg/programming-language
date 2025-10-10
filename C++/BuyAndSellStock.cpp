#include <iostream>
#include <climits>
using namespace std;

/*------------------------------------------------------------
    FUNCTION: maxProfit
    PURPOSE:
        To calculate the maximum profit that can be made by 
        buying and selling a stock once.

    LOGIC:
        - We maintain two variables:
            1. minPrice → Minimum stock price seen so far
            2. maxProfit → Maximum profit that can be made

        - As we iterate through the price list:
            - Update minPrice if the current price is lower.
            - Calculate profit for the current price:
                profit = currentPrice - minPrice
            - Update maxProfit if this profit is greater.

    TIME COMPLEXITY:  O(n)
    SPACE COMPLEXITY: O(1)
-------------------------------------------------------------*/
void maxProfit(int *prices, int n) {
    if (n <= 1) {
        cout << "Max Profit = 0 (Not enough data)" << endl;
        return;
    }

    int minPrice = prices[0];   // Track minimum price seen so far
    int maxProfit = 0;          // Track maximum profit possible

    // Traverse price list
    for (int i = 1; i < n; i++) {
        // Update minimum price if lower price found
        minPrice = min(minPrice, prices[i]);

        // Calculate profit for the current day
        int currProfit = prices[i] - minPrice;

        // Update maxProfit if current profit is higher
        maxProfit = max(maxProfit, currProfit);
    }

    cout << "Max Profit = " << maxProfit << endl;
}

/*------------------------------------------------------------
    FUNCTION: main
    PURPOSE:
        Entry point of the program. Demonstrates how the 
        maxProfit function works using sample data.
-------------------------------------------------------------*/
int main() {
    // Example stock prices on consecutive days
    int prices[] = {7, 1, 5, 3, 6, 4};
    int n = sizeof(prices) / sizeof(int);

    // Function call to compute max profit
    maxProfit(prices, n);

    return 0;
}
