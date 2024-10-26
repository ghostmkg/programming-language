import java.util.Scanner;

class Solution {
    public int scoreOfString(String s) {
        int ans = 0;
        
        // Iterate through the string and calculate the score
        for (int i = 1; i < s.length(); i++) {
            int ascii1 = (int)s.charAt(i - 1);
            int ascii2 = (int)s.charAt(i);
            ans += Math.abs(ascii1 - ascii2);
        }
        
        return ans;
    }

    public static void main(String[] args) {
        // Create an instance of the Solution class
        Solution solution = new Solution();
        
        // Take input from the user
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String inputString = scanner.nextLine();
        
        // Call the scoreOfString method and print the result
        int result = solution.scoreOfString(inputString);
        System.out.println("Score of the string is: " + result);
    }
}
