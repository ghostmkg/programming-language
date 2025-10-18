import java.util.Scanner;

public class PalindromeNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a number: ");
        int num = sc.nextInt();
        int original = num, rev = 0;
        while (num != 0) {
            rev = rev * 10 + num % 10;
            num /= 10;
        }
        if (rev == original)
            System.out.println(original + " is a palindrome number!");
        else
            System.out.println(original + " is NOT a palindrome number.");
        sc.close();
    }
}
