#include<iostream>
using namespace std;

int main() {

    int num;
    cout << "Enter a non-negative number: ";
    cin >> num;

    // Ensure the number is non-negative
    if (num < 0) {
        cout << "Factorial is not defined for negative numbers." << endl;
    } else {
        int fact = 1;

        // Factorial of 0 is 1
        for (int i = num; i >= 1; i--) {
            fact = fact * i;
        }

        cout << "The factorial of " << num << " is " << fact << endl;
    }

    return 0;
}
