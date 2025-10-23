#include <iostream>     // For input and output
#include <vector>       // For using dynamic arrays (vectors)
#include <stdexcept>    // For handling exceptions
#include <sstream>      // For reading input line by line

using namespace std;

/*------------------------------------------------------------
    FUNCTION: partition
    PURPOSE: To place the pivot element at its correct position
             in the sorted array and rearrange elements accordingly.
-------------------------------------------------------------*/
int partition(vector<int>& arr, int low, int high) {
    int pivot = arr[high];   // Choosing the last element as the pivot
    int i = low - 1;         // Index of smaller element

    // Traverse from low to high - 1
    for (int j = low; j < high; j++) {
        // If current element is smaller or equal to pivot
        if (arr[j] <= pivot) {
            i++;  // Move boundary of smaller elements
            swap(arr[i], arr[j]);
        }
    }

    // Place pivot at the correct sorted position
    swap(arr[i + 1], arr[high]);

    // Return the index of pivot after placement
    return i + 1;
}

/*------------------------------------------------------------
    FUNCTION: quickSort
    PURPOSE:  Recursively applies the Quick Sort algorithm.
-------------------------------------------------------------*/
void quickSort(vector<int>& arr, int low, int high) {
    if (low < high) {
        // Partition index: arr[pi] is now at right place
        int pi = partition(arr, low, high);

        // Recursively sort elements before and after partition
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

/*------------------------------------------------------------
    FUNCTION: getInput
    PURPOSE:  To take multiple lines of user input dynamically.
              Stops when user presses Enter on an empty line.
-------------------------------------------------------------*/
vector<int> getInput() {
    vector<int> arr;
    string line;

    cout << "Enter integers to sort (press Enter on an empty line to stop):" << endl;

    while (true) {
        getline(cin, line);     // Read a full line of input
        if (line.empty())       // Stop input when empty line is entered
            break;

        stringstream ss(line);  // Convert string to number stream
        int number;
        if (ss >> number) {
            arr.push_back(number);
        } else {
            throw runtime_error("Invalid input. Please enter integers only.");
        }
    }

    if (arr.empty()) {
        throw runtime_error("No numbers were entered.");
    }

    return arr;
}

/*------------------------------------------------------------
    FUNCTION: main
    PURPOSE:  Driver code to execute the program.
-------------------------------------------------------------*/
int main() {
    try {
        // Step 1: Get user input dynamically
        vector<int> arr = getInput();

        // Step 2: Apply Quick Sort on the input array
        quickSort(arr, 0, arr.size() - 1);

        // Step 3: Display the sorted array
        cout << "\nSorted array: ";
        for (int num : arr) {
            cout << num << " ";
        }
        cout << endl;

    } catch (const runtime_error& e) {
        // Handle any input or runtime errors gracefully
        cerr << "Error: " << e.what() << endl;
    }

    return 0;
}
