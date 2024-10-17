import java.util.*;

public class BitFlipCount {

    // Method to count the number of bits to flip to convert 'a' to 'b'
    public static int countBitsToFlip(int a, int b) {
        // XOR of a and b gives the positions where the bits differ
        int xor = a ^ b;
        int count = 0; // Initialize a counter to count differing bits

        // Loop until all differing bits are cleared
        while (xor != 0) {
            // This operation clears the rightmost set bit in xor
            xor = xor & (xor - 1);
            count++; // Increment the count for each set bit
        }

        return count; // Return the total number of bits to flip
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();

        // Output the number of bits to flip to convert 'a' to 'b'
        System.out.println("Bits to flip: " + countBitsToFlip(a, b));

        sc.close();
    }
}
