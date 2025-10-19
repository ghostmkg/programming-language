/**
 * Simple Command-Line "Guess the Number" Game in JavaScript (Node.js)
 *
 * The computer picks a random number between 1 and 100. The player
 * tries to guess it, and the computer provides hints ("Too high!" or
 * "Too low!") until the player guesses correctly.
 */

// To read user input
const readline = require('readline').createInterface({
    input: process.stdin,
    output: process.stdout
});

// 1. Generate the random number (between 1 and 100)
const targetNumber = Math.floor(Math.random() * 100) + 1;

// 2. Initialize the attempts counter
let attempts = 0;

/**
 * The main game loop function.
 * It recursively asks the user for a guess until they get it right.
 */
function askGuess() {
    readline.question('Guess a number between 1 and 100: ', (input) => {
        const guess = parseInt(input);

        // 3. Input Validation
        if (isNaN(guess) || guess < 1 || guess > 100) {
            console.log('Invalid input. Please enter a number between 1 and 100.');
            askGuess(); // Ask again without counting it as an attempt
            return;
        }

        // Valid guess, increment attempt counter
        attempts++;

        // 4. Feedback Logic
        if (guess < targetNumber) {
            console.log('Too low! Try again.');
            askGuess(); // Recursive call for the next guess
        } else if (guess > targetNumber) {
            console.log('Too high! Try again.');
            askGuess(); // Recursive call for the next guess
        } else {
            // 5. Win Condition
            console.log(`\n🎉 Correct! The number was ${targetNumber}.`);
            console.log(`You guessed it in ${attempts} attempts!`);
            readline.close();
        }
    });
}

// Start the game
console.log('--- Welcome to Guess the Number! ---');
console.log("I'm thinking of a number between 1 and 100...");
askGuess();