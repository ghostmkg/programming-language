// ------------------------------------------------------------
// Program: BucketSort.java
// Purpose: To implement the Bucket Sort algorithm for sorting
//          floating-point numbers in the range [0, 1).
// Author:  Jitin Saxena
// ------------------------------------------------------------

import java.util.ArrayList;
import java.util.Collections;

public class BucketSort {

    /*------------------------------------------------------------
        FUNCTION: bucketSort
        PURPOSE:
            Sorts an array of floating-point numbers using the
            Bucket Sort algorithm.
            
        ALGORITHM STEPS:
            1. Create 'n' empty buckets (lists).
            2. Distribute elements from the array into appropriate buckets
               based on their value.
            3. Sort each bucket individually using Collections.sort().
            4. Concatenate all buckets to get the final sorted array.

        TIME COMPLEXITY:
            - Average Case: O(n + k) ≈ O(n)
            - Worst Case: O(n²) (when all elements fall in one bucket)
        SPACE COMPLEXITY: O(n)
    -------------------------------------------------------------*/
    public static void bucketSort(float[] array) {
        int n = array.length;

        if (n <= 0) return; // Handle empty array case

        // Step 1: Create empty buckets
        @SuppressWarnings("unchecked")
        ArrayList<Float>[] buckets = new ArrayList[n];
        for (int i = 0; i < n; i++) {
            buckets[i] = new ArrayList<>();
        }

        // Step 2: Distribute elements into buckets
        for (float value : array) {
            // Assuming values are in range [0, 1)
            int bucketIndex = (int) (value * n);
            buckets[bucketIndex].add(value);
        }

        // Step 3: Sort individual buckets
        for (ArrayList<Float> bucket : buckets) {
            Collections.sort(bucket);
        }

        // Step 4: Concatenate all buckets into the original array
        int index = 0;
        for (ArrayList<Float> bucket : buckets) {
            for (float value : bucket) {
                array[index++] = value;
            }
        }
    }

    /*------------------------------------------------------------
        FUNCTION: main
        PURPOSE:
            Demonstrates the working of the Bucket Sort algorithm
            using sample floating-point data.
    -------------------------------------------------------------*/
    public static void main(String[] args) {
        // Example array of floating-point numbers in range [0, 1)
        float[] array = {0.42f, 0.32f, 0.53f, 0.12f, 0.66f, 0.90f};

        // Call the bucket sort function
        bucketSort(array);

        // Display the sorted array
        System.out.print("Sorted array: ");
        for (float num : array) {
            System.out.print(num + " ");
        }
    }
}
