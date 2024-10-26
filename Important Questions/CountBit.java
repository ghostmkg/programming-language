import java.util.*;

public class CountBit {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int n = sc.nextInt(); // Input a number
        int count = 0;// set a counter

        // Loop to count the set bits in the binary representation of the number
        while (n > 0) {// Execute loop unlit no until num becomes 0
            count++;
            // This operation clears the rightmost set bit in n
            // Example: n = 1010 & 1001 clears the last '1' in binar
            n = n & (n - 1);
        }
        System.out.println("Total set bits: " + count);
        sc.close();
    }
}
