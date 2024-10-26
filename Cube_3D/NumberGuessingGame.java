package Cube_3D;

import java.util.Random;
import java.util.Scanner;

public class NumberGuessingGame {
    public void RandomNumGame(int randomNumber, int rounds) {
        Scanner sc = new Scanner(System.in);

        try {

            while (rounds > 0) {
                System.out.println("Guess the randomly generated number:");
                int guessNumber = sc.nextInt();
                System.out.println();

                if (guessNumber < 0 || guessNumber > 100) {
                    System.out.println("Invalid number guessed. Please guess a number between 0 and 100.");
                    System.out.println();
                } else if (guessNumber == randomNumber) {
                    System.out.println("Yupz Your Guess Is Correct");
                    System.out.println("Your final score is : " + rounds * 20);
                    return;
                } else if (guessNumber < randomNumber) {
                    System.out.println("Oops! You guessed the Low number as compared to randomly generated number");
                } else {
                    System.out.println("Oops! You guessed the High number as compared to randomly generated number");
                }

                rounds = rounds - 1;

                if (rounds > 0) {
                    System.out.println("You have " + rounds + " rounds left , try again in the next round");
                    System.out.println();
                } else {
                    System.out.println();
                    System.out.println("Sorry,Game over! The correct number was: " + randomNumber);
                    System.out.println("Your final score for the game is : " + rounds * 20);
                }
            }

        } catch(Exception e){
            System.out.println("You may entered the wrong number.");
        }
        sc.close();
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        Random randInt = new Random();
        int randomNumber = randInt.nextInt(101);

        System.out.println();
        System.out.println("Hello,What Is Your Name\n Please enter your name here :");
        String name = sc.nextLine();
        System.out.println("Hello "+ name+" Welcome! ");
        System.out.println();

        System.out.println("These are the rules and conditions for this game.");
        System.out.println();

        System.out.println("1. This is a game where you have to guess the randomly generated number.");
        System.out.println("2. The number guessed by you will be in range of 1 to 100 only.");
        System.out.println("3. The score will be shown to you according to rounds you will be taking in guessing the number.");
        System.out.println("4. If you failed to guess the correct number.Don't worry the correct number will be shown at the end of this game.");
        System.out.println("So, All The Best. Hope you will enjoy this game.");

        System.out.println();
        System.out.println("Let's Start The Game.");
        System.out.println("Random number generated is : " + randomNumber);
        System.out.println();

         NumberGuessingGame task = new NumberGuessingGame();
        task.RandomNumGame(randomNumber, 5);

    }
}   