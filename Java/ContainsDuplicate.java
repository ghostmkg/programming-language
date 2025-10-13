import java.util.HashSet;

class ContainsDuplicate {
    public boolean containsDuplicate(int[] nums) {
        HashSet<Integer> seen = new HashSet<>();

        for (int num : nums) {
            if (seen.contains(num)) {
                return true;  // Found a duplicate
            }
            seen.add(num);
        }

        return false;  // No duplicates found
    }
}
