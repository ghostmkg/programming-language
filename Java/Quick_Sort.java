import java.util.Arrays;
 public class Quick_Sort {
    public static void main(String[] args) {
        int []arr={1,22,34,4,55,42,8,-79};
        quicksort(arr,0, arr.length-1);
        System.out.println(Arrays.toString(arr));

    }
    public static void swap(int[]arr,int x,int y){
        int temp=arr[x];
        arr[x]=arr[y];
        arr[y]=temp;
    }
    //partition returns the correct index of the element and elements before that index are small and after that index are large
    static int partition(int[]arr,int st,int end){
        int pivot=arr[st];
        int count=0;
        for (int i = st+1; i <=end ; i++) {
            if(arr[i]<=pivot) count++;
        }
        int pivotInd=st+count;
        swap(arr,st,pivotInd);//yaha tak me pivot apni sahi place pr aagya h
        //aage ka code left side pr pivot se chote right side pr pivot se badhe elements daalega
        int i=st,j=end;//2 pointer
        while (i<pivotInd&&j>pivotInd){
            while (arr[i]<=pivot) i++;
            while (arr[j]>pivot) j--;
            if(i<pivotInd&&j>pivotInd){
                swap(arr,i,j);
                i++;
                j--;
            }
        }
        return pivotInd;
    }
    static void quicksort(int[]arr,int st,int end){
        if(st>=end){
            return;
        }
        int pi=partition(arr,st,end);
        quicksort(arr,st,pi-1);
        quicksort(arr,pi+1,end);
    } {
    
}
 }