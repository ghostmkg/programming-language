import java.util.Stack;
import java.util.Scanner;

public class ParenthesisChecker {

    // Function to check if parentheses are balanced
    public static boolean isBalanced(String expr) {
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < expr.length(); i++) {
            char ch = expr.charAt(i);

            // Push opening brackets
            if (ch == '(' || ch == '{' || ch == '[') {
                stack.push(ch);
            }
            // Check closing brackets
            else if (ch == ')' || ch == '}' || ch == ']') {
                // If stack empty → no matching opening bracket
                if (stack.isEmpty())
                    return false;

                char top = stack.pop();

                // Check for matching pairs
                if ((ch == ')' && top != '(') ||
                    (ch == '}' && top != '{') ||
                    (ch == ']' && top != '[')) {
                    return false;
                }
            }
        }

        // If stack empty → all brackets matched
        return stack.isEmpty();
    }

    // Driver code
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter an expression: ");
        String expression = sc.nextLine();

        if (isBalanced(expression))
            System.out.println("Balanced Parentheses");
        else
            System.out.println("Not Balanced");

        sc.close();
    }
}