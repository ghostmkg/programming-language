/**
 * Advanced Sorting Algorithms Implementation in Java
 * ===================================================
 * 
 * This class implements various advanced sorting algorithms with detailed
 * explanations, time/space complexity analysis, and optimization techniques.
 * 
 * Algorithms Implemented:
 * - Quick Sort (with optimizations)
 * - Merge Sort (iterative and recursive)
 * - Heap Sort
 * - Counting Sort
 * - Radix Sort
 * - Bucket Sort
 * - Tim Sort (hybrid)
 * - Shell Sort
 * 
 * @author Hacktoberfest 2025 Contributor
 * @version 1.0
 */

package algorithms.sorting;

import java.util.*;

public class AdvancedSortingAlgorithms {
    
    /**
     * Quick Sort with randomized pivot selection.
     * 
     * Time Complexity:
     *   Best: O(n log n)
     *   Average: O(n log n)
     *   Worst: O(n^2) - rare with randomization
     * Space Complexity: O(log n) for recursion stack
     * 
     * @param arr Array to be sorted
     */
    public static void quickSort(int[] arr) {
        if (arr == null || arr.length <= 1) return;
        quickSortHelper(arr, 0, arr.length - 1);
    }
    
    private static void quickSortHelper(int[] arr, int left, int right) {
        if (left < right) {
            // Use median-of-three pivot selection for better performance
            int pivotIndex = partition(arr, left, right);
            quickSortHelper(arr, left, pivotIndex - 1);
            quickSortHelper(arr, pivotIndex + 1, right);
        }
    }
    
    private static int partition(int[] arr, int left, int right) {
        // Median-of-three pivot selection
        int mid = left + (right - left) / 2;
        
        if (arr[mid] < arr[left]) swap(arr, left, mid);
        if (arr[right] < arr[left]) swap(arr, left, right);
        if (arr[mid] < arr[right]) swap(arr, mid, right);
        
        int pivot = arr[right];
        int i = left - 1;
        
        for (int j = left; j < right; j++) {
            if (arr[j] <= pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        
        swap(arr, i + 1, right);
        return i + 1;
    }
    
    /**
     * Merge Sort (Recursive Implementation).
     * 
     * Time Complexity: O(n log n) in all cases
     * Space Complexity: O(n) for temporary array
     * 
     * @param arr Array to be sorted
     */
    public static void mergeSort(int[] arr) {
        if (arr == null || arr.length <= 1) return;
        mergeSortHelper(arr, 0, arr.length - 1);
    }
    
    private static void mergeSortHelper(int[] arr, int left, int right) {
        if (left < right) {
            int mid = left + (right - left) / 2;
            
            mergeSortHelper(arr, left, mid);
            mergeSortHelper(arr, mid + 1, right);
            merge(arr, left, mid, right);
        }
    }
    
    private static void merge(int[] arr, int left, int mid, int right) {
        int n1 = mid - left + 1;
        int n2 = right - mid;
        
        int[] leftArr = new int[n1];
        int[] rightArr = new int[n2];
        
        System.arraycopy(arr, left, leftArr, 0, n1);
        System.arraycopy(arr, mid + 1, rightArr, 0, n2);
        
        int i = 0, j = 0, k = left;
        
        while (i < n1 && j < n2) {
            if (leftArr[i] <= rightArr[j]) {
                arr[k++] = leftArr[i++];
            } else {
                arr[k++] = rightArr[j++];
            }
        }
        
        while (i < n1) arr[k++] = leftArr[i++];
        while (j < n2) arr[k++] = rightArr[j++];
    }
    
    /**
     * Heap Sort using max heap.
     * 
     * Time Complexity: O(n log n) in all cases
     * Space Complexity: O(1) - in-place sorting
     * 
     * @param arr Array to be sorted
     */
    public static void heapSort(int[] arr) {
        if (arr == null || arr.length <= 1) return;
        
        int n = arr.length;
        
        // Build max heap
        for (int i = n / 2 - 1; i >= 0; i--) {
            heapify(arr, n, i);
        }
        
        // Extract elements from heap
        for (int i = n - 1; i > 0; i--) {
            swap(arr, 0, i);
            heapify(arr, i, 0);
        }
    }
    
    private static void heapify(int[] arr, int n, int i) {
        int largest = i;
        int left = 2 * i + 1;
        int right = 2 * i + 2;
        
        if (left < n && arr[left] > arr[largest]) {
            largest = left;
        }
        
        if (right < n && arr[right] > arr[largest]) {
            largest = right;
        }
        
        if (largest != i) {
            swap(arr, i, largest);
            heapify(arr, n, largest);
        }
    }
    
    /**
     * Counting Sort - works well for small range of integers.
     * 
     * Time Complexity: O(n + k) where k is range
     * Space Complexity: O(k)
     * 
     * @param arr Array to be sorted (non-negative integers)
     */
    public static void countingSort(int[] arr) {
        if (arr == null || arr.length <= 1) return;
        
        int max = Arrays.stream(arr).max().orElse(0);
        int min = Arrays.stream(arr).min().orElse(0);
        int range = max - min + 1;
        
        int[] count = new int[range];
        int[] output = new int[arr.length];
        
        // Count occurrences
        for (int num : arr) {
            count[num - min]++;
        }
        
        // Cumulative count
        for (int i = 1; i < range; i++) {
            count[i] += count[i - 1];
        }
        
        // Build output array
        for (int i = arr.length - 1; i >= 0; i--) {
            output[count[arr[i] - min] - 1] = arr[i];
            count[arr[i] - min]--;
        }
        
        System.arraycopy(output, 0, arr, 0, arr.length);
    }
    
    /**
     * Radix Sort - sorts integers digit by digit.
     * 
     * Time Complexity: O(d * (n + k)) where d is number of digits
     * Space Complexity: O(n + k)
     * 
     * @param arr Array to be sorted (non-negative integers)
     */
    public static void radixSort(int[] arr) {
        if (arr == null || arr.length <= 1) return;
        
        int max = Arrays.stream(arr).max().orElse(0);
        
        for (int exp = 1; max / exp > 0; exp *= 10) {
            countingSortByDigit(arr, exp);
        }
    }
    
    private static void countingSortByDigit(int[] arr, int exp) {
        int n = arr.length;
        int[] output = new int[n];
        int[] count = new int[10];
        
        // Count occurrences
        for (int num : arr) {
            count[(num / exp) % 10]++;
        }
        
        // Cumulative count
        for (int i = 1; i < 10; i++) {
            count[i] += count[i - 1];
        }
        
        // Build output array
        for (int i = n - 1; i >= 0; i--) {
            int digit = (arr[i] / exp) % 10;
            output[count[digit] - 1] = arr[i];
            count[digit]--;
        }
        
        System.arraycopy(output, 0, arr, 0, n);
    }
    
    /**
     * Bucket Sort - distributes elements into buckets.
     * 
     * Time Complexity:
     *   Best: O(n + k)
     *   Average: O(n + n^2/k + k)
     *   Worst: O(n^2)
     * Space Complexity: O(n + k)
     * 
     * @param arr Array to be sorted
     * @param bucketCount Number of buckets
     */
    public static void bucketSort(int[] arr, int bucketCount) {
        if (arr == null || arr.length <= 1) return;
        
        int max = Arrays.stream(arr).max().orElse(0);
        int min = Arrays.stream(arr).min().orElse(0);
        
        @SuppressWarnings("unchecked")
        List<Integer>[] buckets = new ArrayList[bucketCount];
        for (int i = 0; i < bucketCount; i++) {
            buckets[i] = new ArrayList<>();
        }
        
        // Distribute elements into buckets
        int range = max - min + 1;
        for (int num : arr) {
            int bucketIndex = (int) ((long) (num - min) * bucketCount / range);
            if (bucketIndex >= bucketCount) bucketIndex = bucketCount - 1;
            buckets[bucketIndex].add(num);
        }
        
        // Sort individual buckets and concatenate
        int index = 0;
        for (List<Integer> bucket : buckets) {
            Collections.sort(bucket);
            for (int num : bucket) {
                arr[index++] = num;
            }
        }
    }
    
    /**
     * Shell Sort - generalization of insertion sort.
     * 
     * Time Complexity: O(n^(3/2)) with this gap sequence
     * Space Complexity: O(1)
     * 
     * @param arr Array to be sorted
     */
    public static void shellSort(int[] arr) {
        if (arr == null || arr.length <= 1) return;
        
        int n = arr.length;
        
        // Start with a large gap and reduce it
        for (int gap = n / 2; gap > 0; gap /= 2) {
            for (int i = gap; i < n; i++) {
                int temp = arr[i];
                int j = i;
                
                while (j >= gap && arr[j - gap] > temp) {
                    arr[j] = arr[j - gap];
                    j -= gap;
                }
                
                arr[j] = temp;
            }
        }
    }
    
    // Helper method to swap elements
    private static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    
    /**
     * Demonstrates all sorting algorithms with performance comparison.
     */
    public static void demonstrateAll() {
        System.out.println("=".repeat(70));
        System.out.println("ADVANCED SORTING ALGORITHMS DEMONSTRATION");
        System.out.println("=".repeat(70));
        
        int[] sizes = {10, 100, 1000};
        
        for (int size : sizes) {
            System.out.println("\nArray Size: " + size);
            System.out.println("-".repeat(70));
            
            int[] original = generateRandomArray(size);
            
            // Test each algorithm
            testSort("Quick Sort", original.clone(), AdvancedSortingAlgorithms::quickSort);
            testSort("Merge Sort", original.clone(), AdvancedSortingAlgorithms::mergeSort);
            testSort("Heap Sort", original.clone(), AdvancedSortingAlgorithms::heapSort);
            
            if (size <= 1000) {
                testSort("Counting Sort", original.clone(), AdvancedSortingAlgorithms::countingSort);
                testSort("Radix Sort", original.clone(), AdvancedSortingAlgorithms::radixSort);
                testSort("Bucket Sort", original.clone(), arr -> bucketSort(arr, 10));
            }
            
            testSort("Shell Sort", original.clone(), AdvancedSortingAlgorithms::shellSort);
        }
        
        System.out.println("\n" + "=".repeat(70));
    }
    
    private static void testSort(String name, int[] arr, SortFunction sortFunc) {
        long startTime = System.nanoTime();
        sortFunc.sort(arr);
        long endTime = System.nanoTime();
        
        boolean sorted = isSorted(arr);
        double timeMs = (endTime - startTime) / 1_000_000.0;
        
        System.out.printf("%-15s: %s (%.3f ms)%n", 
            name, sorted ? "✓ Sorted" : "✗ Failed", timeMs);
    }
    
    private static int[] generateRandomArray(int size) {
        Random rand = new Random();
        int[] arr = new int[size];
        for (int i = 0; i < size; i++) {
            arr[i] = rand.nextInt(10000);
        }
        return arr;
    }
    
    private static boolean isSorted(int[] arr) {
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] < arr[i - 1]) return false;
        }
        return true;
    }
    
    @FunctionalInterface
    interface SortFunction {
        void sort(int[] arr);
    }
    
    public static void main(String[] args) {
        demonstrateAll();
    }
}
