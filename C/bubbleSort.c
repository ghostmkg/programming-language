#include <stdio.h>

void bubbleSort(int arr[], int n) {
    int temp, swapped;
    
    for (int i = 0; i < n - 1; i++) {
        swapped = 0;
        
        for (int j = 0; j < n - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                // Swap arr[j] and arr[j + 1]
                temp = arr[j];
                  arr[j] = arr[j + 1];
                arr[j + 1] = temp;
                swapped = 1; // Set swapped to true
            }
        }

        // If no two elements were swapped in the inner loop, the array is already sorted
        if (swapped == 0) {
            break;
        }
    }
}

int main() {
    int n;
    
    printf("Enter the number of elements: ");
    scanf("%d", &n);
    
    int arr[n];
    
    printf("Enter %d elements:\n", n);
    
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }
    
    // Call the Bubble Sort function
    bubbleSort(arr, n);
    
    printf("Sorted array in ascending order:\n");
    
    for (int i = 0; i < n; i++) {
        printf("%d ", arr[i]);
    }
    
    printf("\n");
    
    return 0;
}