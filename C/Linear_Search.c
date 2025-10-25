#include <stdio.h>

int main() {
    int arr[100], n, target, i, found = 0;

    printf("Enter number of elements: ");
    scanf("%d", &n);

    printf("Enter %d integers:\n", n);
    for (i = 0; i < n; i++) {
        scanf("%d", &arr[i]);
    }

    printf("Enter the number to search: ");
    scanf("%d", &target);

    for (i = 0; i < n; i++) {
        if (arr[i] == target) {
            found = 1;
            printf("✅ %d found at index %d.\n", target, i);
            break;
        }
    }

    if (!found) {
        printf("❌ %d not found in the array.\n", target);
    }

    return 0;
}