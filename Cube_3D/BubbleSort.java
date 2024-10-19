package Cube_3D;

import java.util.Scanner;

public class BubbleSort {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.println("Please enter the total number of elements:");
        int n = sc.nextInt();
        int[] array = new int[n];

        System.out.println("Please enter the elements:");
        for (int i = 0; i < n; i++) {
            array[i] = sc.nextInt();
        }

        // Perform Bubble Sort
        bubbleSort(array);

        // Print the sorted array
        System.out.println("Sorted array:");
        for (int element : array) {
            System.out.print(element + "\t");
        }
        System.out.println();
    }

    static void bubbleSort(int[] arr) {
        int n = arr.length;
        for (int i = 0; i < n - 1; i++) {
            for (int j = 0; j < n - i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    // Swap arr[j] and arr[j + 1]
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }
}


