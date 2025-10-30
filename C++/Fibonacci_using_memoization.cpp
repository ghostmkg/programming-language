// Finding Fibonacci number using memoization(Top-Down approach)
#include <iostream>
#include <vector>
using namespace std;
vector<int> v;
int fibonacci(int n)
{
    if (v[n] != -1)
        return v[n];
    v[n] = fibonacci(n - 1) + fibonacci(n - 2);
    return v[n];
}
int main()
{
    int n;
    cout << "Enter a number: ";
    cin >> n;
    v.assign(n + 1, -1);
    v[0] = 0;
    v[1] = 1;
    cout << "Fibonacci number at position " << n << " is: " << fibonacci(n) << endl;
}

/*
Complexity analysis
If we do recursion without DP then for finding a fibonacci number at position N, the T.C=O(2^N) and S.C=O(1)
But now T.C = O(N) [We go from N till 0] and S.C=O(N) [As we are using additional space for storing prev computed values]
As we are going from top to bottom {from N to 0} this is called top to bottom approach or memoization
*/