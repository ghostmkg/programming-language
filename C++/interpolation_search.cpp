int interpolationSearch(int arr[], int n, int x) {
    int low = 0, high = n - 1;

    while (low <= high && x >= arr[low] && x <= arr[high]) {
        if (low == high) {
            if (arr[low] == x) return low;
            return -1;
        }

        // Estimate the position of the element
        int pos = low + ((double)(high - low) / (arr[high] - arr[low])) * (x - arr[low]);

        // Check if the element is at the estimated position
        if (arr[pos] == x)
            return pos;

        // If the target element is larger, move to the right sub-array
        if (arr[pos] < x)
            low = pos + 1;

        // If the target element is smaller, move to the left sub-array
        else
            high = pos - 1;
    }
    return -1;  // Element not found
}
