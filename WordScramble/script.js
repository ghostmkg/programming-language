const wordText = document.getElementById('scrambled-word');
const hintText = document.getElementById('word-hint');
const timeText = document.getElementById('time-left');
const scoreText = document.getElementById('score');
const inputField = document.getElementById('user-input');
const refreshBtn = document.getElementById('refresh-btn');
const checkBtn = document.getElementById('check-btn');

let currentWord = {};
let score = 0;
let timeLeft = 30;
let timer;

// Function to shuffle the letters of a word (Fisher-Yates algorithm)
const shuffleWord = (word) => {
    let array = word.split('');
    for (let i = array.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        [array[i], array[j]] = [array[j], array[i]]; // Swap
    }
    return array.join('');
}

// Function to start a new word round
const initGame = () => {
    // Clear any previous response message
    clearMessage();
    
    // Select a random word object
    const randomObj = wordList[Math.floor(Math.random() * wordList.length)];
    currentWord.original = randomObj.word;
    currentWord.scrambled = shuffleWord(randomObj.word);

    // Update the DOM elements
    wordText.innerText = currentWord.scrambled;
    hintText.innerText = randomObj.hint;
    inputField.value = ""; // Clear input field
    inputField.focus();

    // Reset and start the timer
    clearInterval(timer); // Stop any existing timer
    timeLeft = 30; // Reset time
    timeText.innerText = `${timeLeft}s`;
    timer = setInterval(startTimer, 1000);
}

// Function to handle the timer countdown
const startTimer = () => {
    if (timeLeft > 0) {
        timeLeft--;
        timeText.innerText = `${timeLeft}s`;
    } else {
        clearInterval(timer);
        displayMessage("Time's up! You failed to unscramble the word.", 'wrong');
        // Give a moment for the user to read the message, then start a new word
        setTimeout(initGame, 2000);
    }
}

// Function to display an alert message below the input
const displayMessage = (msg, type) => {
    clearMessage();
    const messageEl = document.createElement('div');
    messageEl.className = `message ${type}`;
    messageEl.innerText = msg;
    inputField.after(messageEl);
}

// Function to remove any alert message
const clearMessage = () => {
    const existingMsg = document.querySelector('.message');
    if (existingMsg) {
        existingMsg.remove();
    }
}

// Function to check the user's guess
const checkWord = () => {
    let userGuess = inputField.value.trim().toUpperCase();

    if (!userGuess) {
        displayMessage("Please enter a word to check!", 'wrong');
        return;
    }
    
    if (userGuess === currentWord.original) {
        score++;
        scoreText.innerText = score;
        displayMessage("Awesome! That's the correct word!", 'correct');
        // Start a new word after a short delay
        setTimeout(initGame, 1500);
    } else {
        displayMessage("Incorrect. Try again!", 'wrong');
    }
}

// --- Event Listeners ---
refreshBtn.addEventListener('click', () => {
    // Penalty for skipping
    if (timeLeft > 5) {
        timeLeft -= 5;
        timeText.innerText = `${timeLeft}s`;
    }
    initGame();
});

checkBtn.addEventListener('click', checkWord);

// Allow pressing 'Enter' to check the word
inputField.addEventListener('keyup', (e) => {
    if (e.key === "Enter") {
        checkWord();
    }
});

// Initialize the first game round when the script loads
window.onload = initGame;