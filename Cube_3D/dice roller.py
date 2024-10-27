import random

#range of a dice
minimum = 1
maximum = 6

#to loop the rolling through user input
Diceroll_again = "yes"

while Diceroll_again == "yes" or Diceroll_again == "y":
    print("Rolling your Dice...")
    print("The Values are :")
    
    #generating and printing 1st random value
    print(random.randint(minimum,maximum))
    
    #generating and printing 2nd random value
    print(random.randint(minimum,maximum))
    
    Diceroll_again = input("Do you want to roll the Dice Again? ")