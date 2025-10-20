#author: seema kumari patel
# implementation of binary search in java

import java.util.Scanner;

class search{
     public static void main(String[] args) {
        
            Scanner sc = new Scanner(System.in);
            System.out.println("Enter the number of elements:");
            int n = sc.nextInt();
            int[] arr = new int[n];
            System.out.println("Enter the elements in sorted order:");
            for (int i = 0; i < n; i++) {
                arr[i] = sc.nextInt();
            }
            System.out.println("Enter the element to be searched:");
            int key = sc.nextInt();
            
            int result = binarySearch(arr, key);
            if (result == -1) {
                System.out.println("Element not found in the array.");
            } else {
                System.out.println("Element found at index: " + result);
            }
            sc.close();
     }
}