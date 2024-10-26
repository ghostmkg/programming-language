function quickSort(arr) {
    // Base case: arrays with less than 2 elements are already sorted
    if (arr.length < 2) {
        return arr;
    }

    // Choose a pivot element (usually the first or last element)
    let pivot = arr[arr.length - 1];

    // Arrays to hold elements smaller and larger than the pivot
    let left = [];
    let right = [];

    // Partitioning: putting elements in left or right arrays based on comparison with the pivot
    for (let i = 0; i < arr.length - 1; i++) {
        if (arr[i] < pivot) {
            left.push(arr[i]);
        } else {
            right.push(arr[i]);
        }
    }

    // Recursively sort the left and right arrays, then combine them with the pivot
    return [...quickSort(left), pivot, ...quickSort(right)];
}
