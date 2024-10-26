import java.util.Scanner;

public class LinearSearchAlgorithm {

    /**
     * This method performs a linear search on an array to find the target element.
     * 
     * @param arr   The array to search through.
     * @param target The element to search for.
     * @return The index of the target element if found, otherwise -1.
     */
    public static int linearSearch(int[] arr, int target) {
        // Loop through each element in the array
        for (int i = 0; i < arr.length; i++) {
            // Check if the current element matches the target
            if (arr[i] == target) {
                return i;  // Return the index if target is found
            }
        }
        return -1;  // Return -1 if the target is not found
    }

    public static void main(String[] args) {
        // Create a Scanner object to take input from the user
        Scanner scanner = new Scanner(System.in);

        // Take the size of the array as input from the user
        System.out.print("Enter the size of the array: ");
        int size = scanner.nextInt();

        // Create an array of the given size
        int[] numbers = new int[size];

        // Take the array elements as input from the user
        System.out.println("Enter " + size + " elements for the array:");
        for (int i = 0; i < size; i++) {
            numbers[i] = scanner.nextInt();
        }

        // Take the target element to search for as input from the user
        System.out.print("Enter the target element to search for: ");
        int target = scanner.nextInt();

        // Perform linear search
        int result = linearSearch(numbers, target);

        // Output the result
        if (result != -1) {
            System.out.println("Element " + target + " found at index " + result);
        } else {
            System.out.println("Element " + target + " not found in the array.");
        }

        // Close the scanner
        scanner.close();
    }
}



// Time Complexity:

// Best Case: O(1)
// If the target is the first element.
// Worst Case: O(n)
// If the target is the last element or not in the array.


// Space Complexity:

// O(1)
// Since we are using a fixed amount of extra space regardless of the input size. 
// The input array does not count as extra space.
