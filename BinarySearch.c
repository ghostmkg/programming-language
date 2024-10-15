#include <stdio.h>
int BS(int arr[], int n, int elem) {
    int start = 0, end = n - 1;
    while (start <= end) { 
        int mid = (start + end) / 2;
        if (arr[mid] == elem) {
            return mid;
        } else if (arr[mid] > elem) {
            end = mid - 1; 
        } else {
            start = mid + 1; 
        }
    }
    return -1;
}

int main() {
    int n;
    printf("Enter size of array \n");
    scanf("%d", &n);

    int arr[n];
    printf("Enter array elements: ");
    for (int i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    int elem;
    printf("Enter element to be searched: ");
    scanf("%d", &elem);

    int ans = BS(arr, n, elem);
    printf("%d", ans);

    return 0;
}
