#include <iostream>
#include <string>
using namespace std;

int myAtoi(const string &str)
{
    int i = 0;
    int sign = 1;
    int result = 0;

    // Skip leading whitespaces
    while (i < str.length() && isspace(str[i]))
    {
        i++;
    }

    // Check for optional sign
    if (i < str.length() && (str[i] == '+' || str[i] == '-'))
    {
        sign = (str[i] == '-') ? -1 : 1;
        i++;
    }

    // Convert digits to integer
    while (i < str.length() && isdigit(str[i]))
    {
        result = result * 10 + (str[i] - '0');
        i++;
    }

    return sign * result;
}

int main()
{
    string input = "  -1234";
    cout << "Converted integer: " << myAtoi(input) << endl;
    return 0;
}
