/**
 * ✅ Valid Parenthesis String — LeetCode 678
 *
 * Problem
 * -------
 * Given a string s containing only the characters '(', ')' and '*', where '*'
 * can be treated as '(' or ')' or an empty string, determine if s is a valid
 * parenthesis string.
 *
 * A string is valid if:
 * - Every '(' has a corresponding ')' that comes after it.
 * - Every ')' has a corresponding '(' that comes before it.
 * - Parentheses are properly nested.
 *
 * Key Idea (Greedy Lower/Upper Bound)
 * -----------------------------------
 * Track a RANGE of how many '(' can be "open" at each position:
 * - lo = the minimum possible number of open '(' so far if we use '*' as ')' when helpful
 * - hi = the maximum possible number of open '(' so far if we use '*' as '(' when helpful
 *
 * For each character:
 * - '('  => lo++, hi++
 * - ')'  => lo = max(0, lo - 1), hi--
 * - '*'  => lo = max(0, lo - 1)   // treat '*' as ')'
 *           hi++                  // OR treat '*' as '('
 *
 * If at any time hi < 0, we have more ')' than we can match => invalid.
 * At the end, we must be able to close all opens in the "best" way: lo == 0.
 *
 * Time/Space:
 * - Time: O(n)
 * - Space: O(1)
 *
 * Alternative Approaches (for reference)
 * --------------------------------------
 * 1) Two-pass counting:
 *    - Left-to-right: treat '*' as '(' and ensure no premature neg balance.
 *    - Right-to-left: treat '*' as ')' and ensure no premature neg balance.
 *    If both passes succeed, the string is valid. O(n) time, O(1) space.
 *
 * 2) Stack-based:
 *    - One stack for '(' indices, one for '*' indices. Match ')' greedily,
 *      then match remaining '(' with '*' coming after them. O(n) time, O(n) space.
 *
 * References
 * ----------
 * - Problem: https://leetcode.com/problems/valid-parenthesis-string/
 * - Editorial: https://leetcode.com/problems/valid-parenthesis-string/solutions/
 *
 * This file includes:
 * - Greedy O(n)/O(1) solution: checkValidString
 * - Two-pass O(n)/O(1) solution: checkValidStringTwoPass
 * - Sample main() with tests
 */
public class ValidParenthesisString {

    /**
     * Greedy lower/upper bound solution.
     *
     * @param s input string consisting of '(', ')', '*'
     * @return true if s can be a valid parenthesis string, false otherwise
     */
    public static boolean checkValidString(String s) {
        int lo = 0; // min possible open '('
        int hi = 0; // max possible open '('

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (c == '(') {
                lo++;
                hi++;
            } else if (c == ')') {
                if (lo > 0) lo--;
                hi--;
            } else { // '*'
                if (lo > 0) lo--;
                hi++;
            }
            if (hi < 0) return false; // too many ')'
        }

        return lo == 0; // all opens can be closed
    }

    /**
     * Two-pass linear-time solution.
     * Pass 1 (L->R): treat '*' as '(' to ensure we never run out of opens.
     * Pass 2 (R->L): treat '*' as ')' to ensure we never run out of closes.
     */
    public static boolean checkValidStringTwoPass(String s) {
        int balance = 0;

        // Left-to-right: treat '*' as '('
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            balance += (c == ')') ? -1 : 1;
            if (balance < 0) return false;
        }

        // Right-to-left: treat '*' as ')'
        balance = 0;
        for (int i = s.length() - 1; i >= 0; i--) {
            char c = s.charAt(i);
            balance += (c == '(') ? -1 : 1;
            if (balance < 0) return false;
        }

        return true;
    }

    // Helper to print results neatly
    private static void runAndPrint(String s) {
        boolean greedy = checkValidString(s);
        boolean twoPass = checkValidStringTwoPass(s);
        System.out.printf("s=\"%s\" -> greedy=%s, twoPass=%s%n", s, greedy, twoPass);
    }

    public static void main(String[] args) {
        // Basic sanity tests (including LeetCode examples)
        runAndPrint("");
        runAndPrint("()");
        runAndPrint("(*)");
        runAndPrint("(*))");
        runAndPrint("(*()");
        runAndPrint(")*(");
        runAndPrint("(()");
        runAndPrint("())");
        runAndPrint("()*");
        runAndPrint("((*)");
        runAndPrint("(*)))");
        runAndPrint("((()))");
        runAndPrint("((*)*)");
        runAndPrint("(((******))");
        runAndPrint("((**))");
        runAndPrint("((((");
        runAndPrint("))))");
        runAndPrint("*");
        runAndPrint("(*");
        runAndPrint(")*");
        runAndPrint("((*)*)*");
    }
}
