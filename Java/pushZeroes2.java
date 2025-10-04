public class pushZeroes2 {
    public static void main(String[] args) {
        
        int [] arr = {4,6,0,0,3,5,0};
    int n=7;
        int indx= 0;
        for(int i=0; i<n; i++){

            while(arr[i]!=0){
                arr[indx] = arr[i];
                indx++;

            }

        }
    for (int i=0; i<n; i++){
        System.out.print(arr[i]);
    }
    
    }
}
