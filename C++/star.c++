#include <iostream>   // Header file for input/output operations
using namespace std;  // Allows direct use of standard library names (like cout, cin)

int main() {
    int rows;  // Variable to store the number of rows for the star pattern

    // Step 1: Ask user to input the number of rows
    cout << "Enter the number of rows: ";
    cin >> rows;  // User enters number (e.g., 5)

    // Step 2: Validate user input
    if (rows <= 0) {
        cout << "Number of rows should be greater than 0!" << endl;
        return 0;  // Exit program if invalid input
    }

    cout << "\n--- Right Angled Triangle Star Pattern ---\n" << endl;

    // Step 3: Outer loop - Controls the number of rows
    // 'i' represents the current row number
    for (int i = 1; i <= rows; i++) {

        // Step 4: Inner loop - Prints stars in each row
        // For each row, print as many stars as the row number
        for (int j = 1; j <= i; j++) {
            cout << "* ";  // Print a star followed by a space
        }

        // Step 5: Move to the next line after each row
        cout << endl;
    }

    // Step 6: End message
    cout << "\nPattern printing complete!" << endl;

    return 0;  // Successful program termination
}
