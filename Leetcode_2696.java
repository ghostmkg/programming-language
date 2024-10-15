import java.util.Stack;

public class Leetcode_2696 {
    public int minLength(String s) {
        Stack<Character> st = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) == 'B') {
                if ((!st.isEmpty()) && (st.peek() == 'A')) {
                    st.pop();
                    continue;
                }
            }
            if (s.charAt(i) == 'D') {
                if ((!st.isEmpty()) && (st.peek() == 'C')) {
                    st.pop();
                    continue;
                }
            }
            st.push(s.charAt(i));
        }
        return st.size();
    }
    public static void main(String[] args) {
        Leetcode_2696 obj = new Leetcode_2696();
        System.out.println(obj.minLength("ABFCACDB"));
    }
}
