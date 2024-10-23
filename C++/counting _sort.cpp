#include <iostream>
#include <vector>
using namespace std;

// Counting sort function
void countingSort(vector<int>& arr) {
    int n = arr.size();

    // Find the maximum element in the array
    int maxElement = *max_element(arr.begin(), arr.end());

    // Create a count array of size maxElement + 1, and initialize it to 0
    vector<int> count(maxElement + 1, 0);

    // Count the occurrences of each element in the input array
    for (int i = 0; i < n; i++) {
        count[arr[i]]++;
    }

    // Update the original array with sorted values
    int index = 0;
    for (int i = 0; i <= maxElement; i++) {
        while (count[i] > 0) {
            arr[index] = i;
            index++;
            count[i]--;
        }
    }
}

// Function to display the array
void display(const vector<int>& arr) {
    for (int i = 0; i < arr.size(); i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    int n;
    cout << "Enter the number of elements: ";
    cin >> n;

    vector<int> arr(n);

    cout << "Enter the elements of the array: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    countingSort(arr);

    cout << "Sorted array: ";
    display(arr);

    return 0;
}
