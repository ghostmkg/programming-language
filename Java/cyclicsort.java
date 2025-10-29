import java.util.Arrays;

public class CycleSort {

    // Function to perform Cycle Sort
    public static void cycleSort(int[] arr) {
        int n = arr.length;

        // Traverse the array to place each element at its correct position
        for (int cycleStart = 0; cycleStart <= n - 2; cycleStart++) {
            int item = arr[cycleStart];

            // Find position where we put the item
            int pos = cycleStart;
            for (int i = cycleStart + 1; i < n; i++) {
                if (arr[i] < item) {
                    pos++;
                }
            }

            // If the item is already in correct position
            if (pos == cycleStart) {
                continue;
            }

            // Skip duplicates
            while (item == arr[pos]) {
                pos++;
            }

            // Swap item with correct position
            if (pos != cycleStart) {
                int temp = item;
                item = arr[pos];
                arr[pos] = temp;
            }

            // Rotate the rest of the cycle
            while (pos != cycleStart) {
                pos = cycleStart;
                for (int i = cycleStart + 1; i < n; i++) {
                    if (arr[i] < item) {
                        pos++;
                    }
                }

                while (item == arr[pos]) {
                    pos++;
                }

                if (item != arr[pos]) {
                    int temp = item;
                    item = arr[pos];
                    arr[pos] = temp;
                }
            }
        }
    }

    public static void main(String[] args) {
        int[] arr = {20, 40, 50, 10, 30};
        System.out.println("Original array: " + Arrays.toString(arr));

        cycleSort(arr);

        System.out.println("Sorted array:   " + Arrays.toString(arr));
    }
}
