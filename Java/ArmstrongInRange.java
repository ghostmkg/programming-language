import java.util.Scanner;

public class ArmstrongInRange {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter start: ");
        int start = sc.nextInt();
        System.out.print("Enter end: ");
        int end = sc.nextInt();
        System.out.println("Armstrong numbers between " + start + " and " + end + ":");
        for (int num = start; num <= end; num++) {
            int sum = 0, temp = num, digits = String.valueOf(num).length();
            while (temp > 0) {
                sum += Math.pow(temp % 10, digits);
                temp /= 10;
            }
            if (sum == num) System.out.print(num + " ");
        }
        sc.close();
    }
}
