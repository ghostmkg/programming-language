import java.util.*;

class Solution {
    public String longestCommonPrefix(String[] strs) {

        // Use a StringBuilder to efficiently build the result string
        StringBuilder result = new StringBuilder();

        // Sort the array of strings lexicographically
        // After sorting, the common prefix of the whole array must be
        // a prefix of both the first and last strings
        Arrays.sort(strs);

        // Convert the first and last strings into character arrays
        char[] first = strs[0].toCharArray();
        char[] last = strs[strs.length - 1].toCharArray();

        // Find the minimum length between the first and last strings
        int len = Math.min(first.length, last.length);

        // Compare characters one by one
        for (int i = 0; i < len; i++) {
            // If characters don't match, stop comparing
            if (first[i] != last[i]) {
                break;
            }
            // Otherwise, append the character to the result
            result.append(first[i]);
        }

        // Return the longest common prefix
        return result.toString();
    }
}
