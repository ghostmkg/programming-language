public class ValidParenthesisString {
    public boolean checkValidString(String s) {
        int low = 0, high = 0;

        for (char c : s.toCharArray()) {
            if (c == '(') {
                low++;
                high++;
            } else if (c == ')') {
                low--;
                high--;
            } else { // c == '*'
                low--;      // treat '*' as ')'
                high++;     // treat '*' as '('
            }

            // high < 0 => too many ')'
            if (high < 0) return false;

            // low can't be negative
            if (low < 0) low = 0;
        }

        // if low == 0, we can balance all parentheses
        return low == 0;
    }

    public static void main(String[] args) {
        ValidParenthesisString obj = new ValidParenthesisString();

        System.out.println(obj.checkValidString("()"));     // true
        System.out.println(obj.checkValidString("(*)"));    // true
        System.out.println(obj.checkValidString("(*))"));   // true
        System.out.println(obj.checkValidString("(*)))"));  // false
    }
}
