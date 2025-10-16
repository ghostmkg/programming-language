#include<iostream>
using namespace std;

int main()
{
    int arr[50], i, n;

    // Ask the user for the number of elements
    cout << "Enter number of digits to enter: ";
    cin >> n;

    // Take array input from the user
    cout << "Enter " << n << " elements into the array:\n";
    for(i = 0; i < n; i++)
        cin >> arr[i];

    // Display the elements entered
    cout << "The entered elements are:\n";
    for(i = 0; i < n; i++)
        cout << arr[i] << " ";

    // Perform Bubble Sort
    // Bubble Sort repeatedly swaps adjacent elements if they are in the wrong order
    for(i = 0; i < n - 1; i++)
    {
        bool swap = false; // variable to check if any swapping happened in this pass

        // Compare each pair of adjacent elements
        for(int j = 0; j < n - i - 1; j++)
        {
            if(arr[j] > arr[j + 1])  // if elements are in wrong order
            {
                // Swap the elements
                int temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swap = true; // mark that a swap happened
            }
        }

        // If no swaps happened in this pass, the array is already sorted, so exit
        if(swap != true)
            break;
    }

    // Step 5: Print the sorted array
    cout << "\nSorted array:\n";
    for(i = 0; i < n; i++)
        cout << arr[i] << " ";

    return 0;
}
