#include <iostream>
using namespace std;

int main() {
    long long n; //using "long long" for bigger inputs, not with "int"
    cout << "Enter number of rows (n): ";
    cin >> n;

    // Input validation
    if (n <= 0) {
        cout << "Yrr, number of rows toh positive daal na!" << endl;
        return 1;
    }
    if (n > 1000) { // Limit to avoid console crash
        cout << "Itna bada n? Console hang ho jayega! 1000 tak try kar." << endl;
        return 1;
    }

    for (long long i = 1; i <= 2 * n; i++) {
        long long stars = (i <= n) ? i : (2 * n - i + 1);
        long long spaces = 2 * (n - stars);

        // Left stars
        for (long long j = 0; j < stars; j++) {
            cout << "*";
        }

        // Middle spaces
        for (long long j = 0; j < spaces; j++) {
            cout << " ";
        }

        // Right stars
        for (long long j = 0; j < stars; j++) {
            cout << "*";
        }

        cout << endl;
    }

    return 0;
}
