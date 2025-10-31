package programming-language.Java;

public class Max_Avg_Subarray {
    public double findMaxAverage(int[] nums, int k) {
        double wsum=0,msum=Double.MIN_VALUE;
        for(int i=0;i<k;i++)
        {
            wsum+=nums[i];
        }
        msum=wsum;
        for(int i=k;i<nums.length;i++)
        {
            wsum=wsum+nums[i]-nums[i-k];
            msum=Math.max(msum,wsum);
        }
        return msum/k;
    }
}
