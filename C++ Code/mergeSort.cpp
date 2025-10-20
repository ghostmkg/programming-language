#include<iostream>
using namespace std;

// Function to merge two sorted halves into a single sorted array
void merge(int arr[], int start, int mid, int end)
{
    // Find sizes of two subarrays
    int n1 = mid - start + 1;   // size of left half
    int n2 = end - mid;         // size of right half

    // Create temporary arrays
    int L[n1], R[n2];

    // Copy data into temporary arrays
    for(int i = 0; i < n1; i++)
        L[i] = arr[start + i];
    for(int j = 0; j < n2; j++)
        R[j] = arr[mid + 1 + j];

    // Merge the temporary arrays back into arr[]
    int i = 0, j = 0, k = start;

    // Compare elements of both subarrays and place them in sorted order
    while(i < n1 && j < n2)
    {
        if(L[i] <= R[j])
            arr[k++] = L[i++];
        else
            arr[k++] = R[j++];
    }

    // Copy any remaining elements of L[]
    while(i < n1)
        arr[k++] = L[i++];

    // Copy any remaining elements of R[]
    while(j < n2)
        arr[k++] = R[j++];
}

// Function to apply merge sort (recursive)
void mergeSort(int arr[], int start, int end)
{
    if(start < end)
    {
        // Find the middle index
        int mid = (start + end) / 2;

        // Recursively sort the first half
        mergeSort(arr, start, mid);

        // Recursively sort the second half
        mergeSort(arr, mid + 1, end);

        // Merge the two halves
        merge(arr, start, mid, end);
    }
}

int main()
{
    int arr[50], n, i;

    // Input number of elements
    cout << "Enter the number of elements: ";
    cin >> n;

    // Input array elements
    cout << "Enter the elements:\n";
    for(i = 0; i < n; i++)
        cin >> arr[i];

    // Display entered elements
    cout << "Entered elements:\n";
    for(i = 0; i < n; i++)
        cout << arr[i] << " ";

    // Sort the array using merge sort
    mergeSort(arr, 0, n - 1);

    // Display sorted array
    cout << "\nSorted array:\n";
    for(i = 0; i < n; i++)
        cout << arr[i] << " ";

    return 0;
}
