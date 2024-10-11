import java.util.Arrays;

public class Insertion_Sort {
    
    public static void main(String[] args) {
        int[] arr={4,10,6,8,2,9};
        insertsort(arr);
        System.out.println(Arrays.toString(arr));

    }
   static void insertsort(int[] arr){
        for (int i = 1; i < arr.length; i++) {
            int j=i;
            while (j>0&&arr[j-1]>arr[j]){
                int temp=arr[j];
                arr[j]=arr[j-1];
                arr[j-1]=temp;
                j--;
            }
        }
    }
}


