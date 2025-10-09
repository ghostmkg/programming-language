public class BubbleSortExample {
    public static void main(String[] args) {
        int[] arr = {5, 1, 4, 2, 8};
        
        bubbleSort(arr);
        
        System.out.println("Sorted array:");
        for (int num : arr) {
            System.out.print(num + " ");
        }
    }

    // Bubble Sort function
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        boolean swapped;

        // Outer loop - number of passes
        for (int i = 0; i < n - 1; i++) {
            swapped = false; // flag to detect any swap in this pass
            
            // Inner loop - compare adjacent elements
            for (int j = 0; j < n - 1 - i; j++) {
                if (arr[j] > arr[j + 1]) {
                    // swap arr[j] and arr[j + 1]
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;

                    swapped = true;
                }
            }

            // If no swaps occurred, array is already sorted
            if (!swapped)
                break;
        }
    }
}
