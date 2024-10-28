#include <iostream>
#include <vector>
#include <stdexcept>
#include <sstream>

using namespace std;

// Function to perform partition in Quick Sort
int partition(vector<int>& arr, int low, int high) {
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j < high; j++) {
        if (arr[j] <= pivot) {
            i++;
            swap(arr[i], arr[j]);
        }
    }
    swap(arr[i + 1], arr[high]);
    return i + 1;
}

// Quick Sort function
void quickSort(vector<int>& arr, int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

// Function to handle dynamic user input with an empty line to stop input
vector<int> getInput() {
    vector<int> arr;
    string line;
    cout << "Enter integers to sort (press Enter on an empty line to stop):" << endl;

    while (true) {
        getline(cin, line);
        if (line.empty()) break;  // Stop input on empty line

        stringstream ss(line);
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

int main() {
    try {
        vector<int> arr = getInput();

        quickSort(arr, 0, arr.size() - 1);

        cout << "Sorted array: ";
        for (int i : arr) {
            cout << i << " ";
        }
        cout << endl;

    } catch (const runtime_error& e) {
        cerr << "Error: " << e.what() << endl;
    }

    return 0;
}
