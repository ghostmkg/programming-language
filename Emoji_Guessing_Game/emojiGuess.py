import random
emojis = [
("😀", "smile"),
("😂", "smile"),
("😢", "sad"),
("🐶", "animal"),
("🐱", "animal"),
("🍎", "food"),
("🍔", "food"),
("⚽", "sports"),
("🚗", "vehicle")
]
emoji, category = random.choice(emojis)
print(" ")
print("🎊Welcome to my emoji guessing game!!!")
print("The category might be: smile, sad, animal, food, sports or vehicle")
print("Guess the category of the emoji: ")
print(emoji)
guess = input("Your guess:\n")
print(" ")
if guess.lower() == category:
    print("Congratulations💕!!!You Guessed it Right")
else:
    print("Sorry😞.The correct answer was: ", category)