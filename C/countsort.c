#include <stdio.h>
#include <stdlib.h>

// Function to perform Counting Sort
void countingSort(int arr[], int n) {
    // Find the maximum element in the array
    int max = arr[0];
    for (int i = 1; i < n; i++) {
        if (arr[i] > max) {
            max = arr[i];
        }
    }

    // Create a count array and initialize it to 0
    int *count = (int *)calloc(max + 1, sizeof(int));
    
    // Store the count of each element in the count array
    for (int i = 0; i < n; i++) {
        count[arr[i]]++;
    }

    // Reconstruct the sorted array from the count array
    int index = 0;
    for (int i = 0; i <= max; i++) {
        while (count[i] > 0) {
            arr[index++] = i;
            count[i]--;
        }
    }

    // Free the dynamically allocated memory
    free(count);
}

// Function to print the array
void printArray(int arr[], int n) {
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    printf("\n");
}

// Main function to test Counting Sort
int main() {
    int n;
    printf("Enter the number of elements: ");
    scanf("%d", &n);

    int arr[n];
    printf("Enter the elements: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    countingSort(arr, n);

    printf("Sorted array: ");
    printArray(arr, n);

    return 0;
}
