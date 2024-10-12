import java.util.*;
public class Selection_Sort {
    public static void main(String[] args) {
        int[]arr={1,22,3,42,5,2,94};
        int []arrs={8,0,7,1,3};
        selectionsort(arrs);
        System.out.println(Arrays.toString(arrs));

    }
    static void selectionsort(int[]arr){
        for (int i = 0; i < arr.length-1; i++) {
            int min=i;
            for (int j = i+1; j < arr.length ; j++) {
                if(arr[j]<arr[min]){
                    min=j;
                }
            }int temp=arr[min];
            arr[min]= arr[i];
            arr[i] =temp;
        }
    }
}
