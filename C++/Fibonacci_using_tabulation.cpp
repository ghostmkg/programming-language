//Finding Fibonacci number using tabulation (Bottom to top approach)
#include <iostream>
#include <vector>
using namespace std;
int Fibonacci(int n)
{
    vector<int>dp(n+1);
    dp[0]=0;
    dp[1]=1;
    for(int i=2;i<n+1;i++)
    {
        dp[i]=dp[i-1]+dp[i-2];
    }
    return dp[n];
}
int main()
{
    int n;
    cout << "Enter a number: ";
    cin >> n;
    cout << "Fibonacci number at position " << n << " is: " << Fibonacci(n) << endl;
}

/*
Complexity analysis
T.C=O(N) as there is one loop running from i=2 to n
S.C=O(N) as we are storing the previously computed result
As we are going from bottom to top [From 0 to N] this is bottom to top approach [Tabulation]
*/