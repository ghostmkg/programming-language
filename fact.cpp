#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    cout << "Enter a number to calculate its factorial: ";
    cin >> n;

    // Vector to store factorial results for each step
    vector<int> factorial(n + 1);

    // Initial factorial of 0 and 1 is 1
    factorial[0] = 1;

    // Calculate factorial using previous results stored in the vector
    for (int i = 1; i <= n; ++i) {
        factorial[i] = factorial[i - 1] * i;
    }

    cout << "Factorial of " << n << " is: " << factorial[n] << endl;

    return 0;
}