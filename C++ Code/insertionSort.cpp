#include<iostream>
using namespace std;

int main()
{
    int arr[50], i, n;

    // Take number of elements as input
    cout << "Enter the number of elements to enter: ";
    cin >> n;

    // Input array elements
    cout << "Enter " << n << " elements:\n";
    for(i = 0; i < n; i++)
        cin >> arr[i];

    // Display the entered elements
    cout << "Entered elements:\n";
    for(i = 0; i < n; i++)
        cout << arr[i] << " ";

    // Insertion Sort Algorithm
    // Picks one element at a time and inserts it into the correct place in the sorted part
    for(i = 1; i < n; i++)   // start from 2nd element
    {
        int key = arr[i];   // the element we want to insert into the sorted part
        int j = i - 1;

        // Shift elements of the sorted part to the right until we find the correct place for key
        while(j >= 0 && arr[j] > key)
        {
            arr[j + 1] = arr[j];
            j--;
        }

        // Place key at its correct position
        arr[j + 1] = key;
    }

    // Display the sorted array
    cout << "\nSorted array:\n";
    for(i = 0; i < n; i++)
        cout << arr[i] << " ";

    return 0;
}
