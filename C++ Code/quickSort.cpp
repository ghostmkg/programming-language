#include<iostream>
using namespace std;

// Function to partition the array
// Places the pivot element at correct position
// and moves smaller elements to left, larger to right
int partition(int arr[], int low, int high)
{
    int pivot = arr[high];   // choosing last element as pivot
    int i = low - 1;         // index of smaller element

    for(int j = low; j < high; j++)
    {
        // If current element is smaller than pivot
        if(arr[j] < pivot)
        {
            i++;
            // Swap arr[i] and arr[j]
            int temp = arr[i];
            arr[i] = arr[j];
            arr[j] = temp;
        }
    }

    // Place pivot at the correct position
    int temp = arr[i + 1];
    arr[i + 1] = arr[high];
    arr[high] = temp;

    return i + 1;  // return pivot index
}

// Function to implement Quick Sort recursively
void quickSort(int arr[], int low, int high)
{
    if(low < high)
    {
        // Partitioning index
        int pi = partition(arr, low, high);

        // Recursively sort elements before and after partition
        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

int main()
{
    int arr[50], i, n;

    // Input number of elements
    cout << "Enter the number of elements: ";
    cin >> n;

    // Input array elements
    cout << "Enter " << n << " elements:\n";
    for(i = 0; i < n; i++)
        cin >> arr[i];

    // Display entered elements
    cout << "Entered elements:\n";
    for(i = 0; i < n; i++)
        cout << arr[i] << " ";

    // Apply Quick Sort
    quickSort(arr, 0, n - 1);

    // Display sorted elements
    cout << "\nSorted elements:\n";
    for(i = 0; i < n; i++)
        cout << arr[i] << " ";

    return 0;
}
