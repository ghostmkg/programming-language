#include <stdio.h>

int findCandidate(int arr[], int n) {
    int count = 1, candidate = arr[0];

    // Phase 1: Finding a candidate
    for (int i = 1; i < n; i++) {
        if (arr[i] == candidate)
            count++;
        else
            count--;

        if (count == 0) {
            candidate = arr[i];
            count = 1;
        }
    }
    return candidate;
}

int isMajority(int arr[], int n, int candidate) {
    int count = 0;

    // Phase 2: Verify if the candidate is actually the majority
    for (int i = 0; i < n; i++) {
        if (arr[i] == candidate)
            count++;
    }

    return (count > n / 2);
}

void findMajorityElement(int arr[], int n) {
    int candidate = findCandidate(arr, n);

    if (isMajority(arr, n, candidate))
        printf("The majority element is %d\n", candidate);
    else
        printf("There is no majority element in the array.\n");
}

int main() {
    int arr[] = {2, 2, 1, 1, 2, 2, 3};
    int n = sizeof(arr) / sizeof(arr[0]);

    findMajorityElement(arr, n);

    return 0;
}
