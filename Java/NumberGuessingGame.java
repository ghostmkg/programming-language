//NumberGuessingGame
import java.util.Random;
import javax.swing.JOptionPane;

public class NumberGuessingGame {
    public static void main(String[] args) {
        int lowerBound = 1;
        int upperBound = 100;
        int maxAttempts = 5;
        int score = 0;

        JOptionPane.showMessageDialog(null, "Welcome to Guess the Number Game!");

        boolean playAgain = true;
        while (playAgain) {
            int randomNumber = generateRandomNumber(lowerBound, upperBound);
            int attempts = 0;
            boolean guessedCorrectly = false;

            while (attempts < maxAttempts && !guessedCorrectly) {
                int userGuess = getUserGuess(lowerBound, upperBound);
                attempts++;

                if (userGuess == randomNumber) {
                    JOptionPane.showMessageDialog(null, "Congratulations! You guessed the correct number.");
                    score += maxAttempts - attempts + 1;
                    guessedCorrectly = true;
                } else if (userGuess < randomNumber) {
                    JOptionPane.showMessageDialog(null, "Too low! Try a higher number.");
                } else {
                    JOptionPane.showMessageDialog(null, "Too high! Try a lower number.");
                }
            }

            if (!guessedCorrectly) {
                JOptionPane.showMessageDialog(null, "Sorry, you did not guess the correct number. The number was: " + randomNumber);
            }

            int option = JOptionPane.showConfirmDialog(null, "Do you want to play again?", "Play Again", JOptionPane.YES_NO_OPTION);
            playAgain = (option == JOptionPane.YES_OPTION);
        }

        JOptionPane.showMessageDialog(null, "Game Over! Your total score is: " + score);
        JOptionPane.showMessageDialog(null, "Thank you for playing Guess the Number Game!");
    }

    private static int generateRandomNumber(int lowerBound, int upperBound) {
        Random random = new Random();
        return random.nextInt(upperBound - lowerBound + 1) + lowerBound;
    }

    private static int getUserGuess(int lowerBound, int upperBound) {
        String userInput = JOptionPane.showInputDialog(null, "Enter your guess (" + lowerBound + " - " + upperBound + "):");
        try {
            return Integer.parseInt(userInput);
        } catch (NumberFormatException e) {
            JOptionPane.showMessageDialog(null, "Invalid input! Please enter a valid number.");
            return getUserGuess(lowerBound, upperBound);
        }
    }
}