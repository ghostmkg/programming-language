#include<iostream>
using namespace std;

class Factorial {
private:
    int num;
public:
    void setNum(int n) {
        num = n;
    }

    long long calculateFactorial() {
        long long result = 1;
        for(int i = 2; i <= num; i++) {
            result *= i;
        }
        return result;
    }

    void displayFactorial() {
        if(num < 0) {
            cout << "Error! Factorial of a negative number doesn't exist.";
        } else {
            cout << "The factorial of " << num << " is " << calculateFactorial();
        }
    }
};

int main() {
    Factorial factorialObj;
    int num;
    cout << "Enter a positive integer: ";
    cin >> num;
    factorialObj.setNum(num);
    factorialObj.displayFactorial();
    return 0;
}