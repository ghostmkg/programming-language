#include <iostream>
using namespace std;

// Maintains the max-heap property for subtree rooted at index i
void heapify(int arr[], int n, int i)
{
    int largest = i;       // Assume current node is largest
    int left = 2 * i + 1;  // Left child index
    int right = 2 * i + 2; // Right child index

    // If left child is larger than root
    if (left < n && arr[left] > arr[largest])
        largest = left;

    // If right child is larger than current largest
    if (right < n && arr[right] > arr[largest])
        largest = right;

    // If largest is not root, swap and continue heapifying
    if (largest != i)
    {
        swap(arr[i], arr[largest]);
        heapify(arr, n, largest);
    }
}

// Main function to perform Heap Sort
void heapSort(int arr[], int n)
{
    // Build max-heap
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(arr, n, i);

    // Extract elements from heap one by one
    for (int i = n - 1; i >= 0; i--)
    {
        // Move current root (max element) to end
        swap(arr[0], arr[i]);
        // Call heapify on reduced heap
        heapify(arr, i, 0);
    }
}

int main()
{
    int arr[] = {12, 11, 13, 5, 6, 7};
    int n = sizeof(arr) / sizeof(arr[0]);

    heapSort(arr, n);

    // Print sorted array
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
}
