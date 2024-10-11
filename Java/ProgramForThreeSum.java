import java.util.*;
public class ProgramForThreeSum {
    public static void main(String[] args) {
        Scanner ttt = new Scanner(System.in);

        //TAKING INPUTS FROM THE USER

        int firstNumber = ttt.nextInt();
        int secondNumber = ttt.nextInt();
        int thirdNumber = ttt.nextInt();

        //CALCULATING SUM 
        int sum = firstNumber + secondNumber + thirdNumber;

        //PRINTING SUM
        System.out.println(sum);
        ttt.close();
    }
}
