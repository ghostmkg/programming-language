public class Kaden_Algo {
    
    public static void main(String[] args) {
        int[] arr= { -2, 1, -3, 4, -1, 2, 1, -5, 4 };
        System.out.println(Kadane(arr));
    }
    public static int Kadane(int[] arr) {
        int ans = Integer.MIN_VALUE;
        int prevsum = 0;
        for (int i = 0; i < arr.length; i++) {
            prevsum += arr[i];
            ans = Math.max(ans, prevsum);

            if (prevsum < 0) {
                prevsum = 0;
            }
        }
        return ans;

    }
}
