// Finding Factorial using memoization (Top-Down approach)
#include <iostream>
#include <vector>
using namespace std;
vector<long long> fact;

long long factorial(int n)
{
    if (n == 0 || n == 1)
        return 1;
    if (fact[n] != -1)
        return fact[n];
    fact[n] = n * factorial(n - 1);
    return fact[n];
}

int main()
{
    int n;
    cout << "Enter a number: ";
    cin >> n;
    fact.assign(n + 1, -1);
    cout << "Factorial of " << n << " is: " << factorial(n) << endl;
}

/*
Complexity analysis
If we compute factorial recursively without DP then for finding factorial of N, T.C = O(N)
and each recursive call adds a frame to the call stack, so S.C = O(N).
However, with memoization, repeated subproblems (if called multiple times across test cases or functions)
are avoided, making subsequent lookups O(1).
As we go from N down to 1 storing intermediate results, this is the top-down or memoization approach.
*/
