import java.util.Scanner;

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

    // Function to take input from the user
    public static int[] getInputArray() {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Enter the size of the array: ");
        int size = scanner.nextInt();

        int[] arr = new int[size];

        System.out.println("Enter the elements of the array:");
        for (int i = 0; i < size; i++) {
            arr[i] = scanner.nextInt();
        }

        return arr;
    }

    public static void main(String[] args) {
        // Take array input from the user
        int[] arr = getInputArray();

        // Display the array to the user
        System.out.println("The array is:");
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();

        // Input target element to search for
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the target element to search for: ");
        int target = scanner.nextInt();

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

