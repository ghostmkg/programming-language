#include<iostream>
using namespace std;

int main()
{
    int arr[50], i, n;

    // Input number of elements
    cout << "Enter the number of elements to enter: ";
    cin >> n;

    // Input array elements
    cout << "Enter " << n << " elements:\n";
    for(i = 0; i < n; i++)
        cin >> arr[i];

    // Display entered elements
    cout << "Entered elements:\n";
    for(i = 0; i < n; i++)
        cout << arr[i] << " ";

    // Selection Sort Algorithm
    // Find the minimum element in the unsorted part and put it at the beginning
    for(i = 0; i < n - 1; i++)
    {
        int minIndex = i; // assume the current position has the minimum element

        // Find the index of the minimum element in the remaining unsorted array
        for(int j = i + 1; j < n; j++)
        {
            if(arr[j] < arr[minIndex])
            {
                minIndex = j;
            }
        }

        // Swap the found minimum element with the first element of unsorted part
        if(minIndex != i)
        {
            int temp = arr[i];
            arr[i] = arr[minIndex];
            arr[minIndex] = temp;
        }
    }

    // Display sorted array
    cout << "\nSorted array:\n";
    for(i = 0; i < n; i++)
        cout << arr[i] << " ";

    return 0;
}
