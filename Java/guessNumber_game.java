
import java.util.Scanner;

public class guessNumber_game {
    public static void main(String[] args) {
        
        Scanner sc = new Scanner(System.in);
        int myNumber = (int)(Math.random()*100);

        int userNumber = 0;

        System.out.println("Guess number (1-100)");

        while(userNumber!=-1){

           userNumber = sc.nextInt();
            
            if(userNumber==-1){ System.out.println("Exit");
            break;
            }
            
            if(userNumber == myNumber) {
                System.out.println("Whohooo , You Found Correct Number");
                break;
            }
            

            else if(userNumber < myNumber) System.out.println("Your Number Is too small");

            else if(userNumber > myNumber) System.out.println("Your number is too large");
             System.out.println("Try Again !!");
            

        }



    }
}
