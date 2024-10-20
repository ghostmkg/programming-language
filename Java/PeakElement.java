public class PeakElement {
    public int findPeakElement(int[] nums) {
        int l = 0, h = nums.length - 1;
        
        while (l < h) {
            int mid = (l + h) / 2;
            
            
            if (nums[mid] > nums[mid + 1]) {
                h = mid;  
            } else {
                l = mid + 1;  
            }
        }
        return l;  
    }

    public static void main(String[] args) {
        PeakElement sol = new PeakElement();  
        int[] nums = {1, 2, 3, 1};  
        int peakIndex = sol.findPeakElement(nums);
        System.out.println("Peak element is at index: " + peakIndex);
    }
}

