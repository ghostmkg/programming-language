#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int n;
    cout << "Enter size: ";
    cin >> n;

    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (i == 1 || i == n || j == 1 || j == n ||
                abs(i - j) == n/2 || i + j == n/2 + n + 1)
                cout << "*";
            else
                cout << " ";
        }
        cout << endl;
    }
    return 0;
}
