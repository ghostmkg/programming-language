public class Linear_search {

    // Function to perform linear search
    public static int linearSearch(int[] arr, int target) {
        // Traverse the array
        for (int i = 0; i < arr.length; i++) {
            // Check if the current element is the target element
            if (arr[i] == target) {
                return i;  // Return the index if found
            }
        }
        return -1;  // Return -1 if the target element is not found
    }

    public static void main(String[] args) {
        // Example array
        int[] arr = {5, 8, 1, 3, 10, 6, 2};

        // Target element to search for
        int target = 10;

        // Call linearSearch function and store the result
        int result = linearSearch(arr, target);

        // Print result
        if (result != -1) {
            System.out.println("Element found at index: " + result);
        } else {
            System.out.println("Element not found in the array.");
        }
    }
}

//👉🏻logic of code
// The for loop iterates over each element in the array (arr).
// The if statement compares each element with the target element.
// If a match is found, the index of that element is returned immediately.
// If no match is found after checking all elements, -1 is returned, indicating that the target element is not present in the array.

//👉🏻 time complexcity
// Worst Case: O(n) – You may have to check every element in the array.
// Best Case: O(1) – The target element is at the first position.

//👉🏻space complexcity
//O(1) – Only a few extra variables are used.

