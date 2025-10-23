import random
choices = ["rock", "paper", "scissors"]
user = input("Choose rock/paper/scissors: ")
comp = random.choice(choices)
print("Computer chose:", comp)
if user == comp:
    print("Draw")
elif (user == "rock" and comp == "scissors") or (user == "paper" and comp == "rock") or (user == "scissors" and comp == "paper"):
    print("You win!")
else:
    print("You lose!")
