//POTD of Oct 10
//You are given a string s consisting of digits. Perform the following operation repeatedly until the string has exactly two digits:
// For each pair of consecutive digits in s, starting from the first digit, calculate a new digit as the sum of the two digits modulo 10.
// Replace s with the sequence of newly calculated digits, maintaining the order in which they are computed.
// Return true if the final two digits in s are the same; otherwise, return false. 
import java.util.*;

class POTDLeetcode {
    public static boolean isSameAfterOperations(String s) {
        while (s.length() > 2) {
            StringBuilder newS = new StringBuilder();
            for (int i = 0; i < s.length() - 1; i++) {
                int sum = (s.charAt(i) - '0' + s.charAt(i + 1) - '0') % 10;
                newS.append(sum);
            }
            s = newS.toString();
        }
        return s.charAt(0) == s.charAt(1);
    }
    public static void main(String[] args) {
        Scanner sc=new Scanner(System.in);
        String s = sc.nextLine();
        boolean result = isSameAfterOperations(s);
        System.out.println("Final two digits are the same: " + result);
        sc.close();
    }
}

