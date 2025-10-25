#include <iostream>
using namespace std;

int main() {
    float height, weight, bmi;

    cout << "Enter your height in meters: ";
    cin >> height;
    cout << "Enter your weight in kg: ";
    cin >> weight;

    bmi = weight / (height * height);

    cout << "Your BMI is: " << bmi << endl;

    if (bmi < 18.5)
        cout << "Category: Underweight" << endl;
    else if (bmi < 24.9)
        cout << "Category: Normal weight" << endl;
    else if (bmi < 29.9)
        cout << "Category: Overweight" << endl;
    else
        cout << "Category: Obese" << endl;

    return 0;
}
