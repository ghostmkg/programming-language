#include<iostream>
#include<string>
#include<climits>
using namespace std;

class BinaryConverter {
private:
    string binaryNum;
public:
    void setBinaryNum(string num) {
        binaryNum = num;
    }

    long long binaryToDecimal() {
        long long decimalNum = 0;
        long long base = 1;

        for(int i = binaryNum.length() - 1; i >= 0; i--) {
            if(binaryNum[i] == '1') {
                // Check for overflow
                if (decimalNum > LLONG_MAX - base) {
                    throw overflow_error("Binary number too large to convert");
                }
                decimalNum += base;
            }
            base *= 2;
        }

        return decimalNum;
    }

    void displayConversion() {
        try {
            long long decimalNum = binaryToDecimal();
            cout << "The decimal equivalent of " << binaryNum << " is " << decimalNum << endl;
        } catch (const overflow_error& e) {
            cout << "Error: " << e.what() << endl;
        }
    }

    bool isValidBinary() {
        for(size_t i = 0; i < binaryNum.length(); i++) {
            if(binaryNum[i] != '0' && binaryNum[i] != '1') {
                return false;
            }
        }
        return true;
    }

    bool isEmpty() {
        return binaryNum.empty();
    }

    bool isTooLong() {
        return binaryNum.length() > 63; // 63 bits for long long
    }
};

int main() {
    BinaryConverter converter;
    string binaryNum;
    cout << "Enter a binary number: ";
    cin >> binaryNum;

    converter.setBinaryNum(binaryNum);

    if(converter.isEmpty()) {
        cout << "Error: Binary number cannot be empty." << endl;
    } else if(converter.isTooLong()) {
        cout << "Error: Binary number is too long. Maximum length is 63 bits." << endl;
    } else if(!converter.isValidBinary()) {
        cout << "Error: Invalid binary number. Please enter a number consisting only of 0s and 1s." << endl;
    } else {
        converter.displayConversion();
    }

    return 0;
}
