public class Fabo {
    public static int fibonacciRecursion(int n,int[]arr){

        /* if(n == 0){
             return 0;
         }
         if(n == 1 || n == 2){
             return 1;*/
     
             if(n<=1){
                 return n;
             }
             if(arr[n]!=0){
                 return arr[n];
             }
     
     
              int ans=fibonacciRecursion(n-2,arr) + fibonacciRecursion(n-1,arr);
             return arr[n]=ans;
     
         }
     
         public static void main(String args[]) {
             int maxNumber = 6;
             System.out.print("Fibonacci Series of " + maxNumber + " numbers: ");
             int []arr=new int[maxNumber+1];
             int ans=fibonacciRecursion(maxNumber,arr);
             System.out.println(ans);
     
         }
}
