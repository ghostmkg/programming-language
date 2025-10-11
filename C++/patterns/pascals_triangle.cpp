#include <iostream>
using namespace std;

int fact(int n) {
    int f = 1;
    for (int i = 1; i <= n; i++) f *= i;
    return f;
}

int nCr(int n, int r) {
    return fact(n) / (fact(r) * fact(n - r));
}

int main() {
    int n;
    cout << "Enter number of rows: ";
    cin >> n;

    for (int i = 0; i < n; i++) {
        for (int space = 0; space < n - i; space++)
            cout << " ";
        for (int j = 0; j <= i; j++)
            cout << nCr(i, j) << " ";
        cout << endl;
    }

    return 0;
}
