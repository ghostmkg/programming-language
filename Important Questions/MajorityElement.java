public class MajorityElement {

    // Function to find and return the majority element in an array
    public static int findMajorityElement(int[] nums) {
        int count = 0; // Counter for tracking occurrences
        int candidate = 0; // Variable to store the potential majority element

        // Find a candidate for the majority element
        for (int num : nums) {
            if (count == 0) {
                candidate = num; // Update candidate if count is zero
            }
            count += (num == candidate) ? 1 : -1; // Increment or decrement count
        }

        // Verify the candidate is majority element
        count = 0;
        for (int num : nums) {
            if (num == candidate) {
                count++; // Count occurrences of the candidate
            }
        }

        // If the candidate occurs more than n/2 times, it's the majority element
        if (count > nums.length / 2) {
            return candidate;
        } else {
            return -1; // Return -1 if no majority element exists
        }
    }

    public static void main(String[] args) {
        int[] nums = { 2, 2, 1, 1, 1, 2, 2 };
        int result = findMajorityElement(nums);

        if (result != -1) {
            System.out.println("Majority Element: " + result);
        } else {
            System.out.println("No Majority Element");
        }
    }
}
