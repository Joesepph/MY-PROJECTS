import random
import os

print("Welcome to rock, paper, scissors game!")
clear = lambda: os.system('cls')

while True:
    choices = ['rock','paper','scissors']

    AI = random.choice(choices)
    Player = None

    while Player not in choices:
        Player = input("Rock, paper or scissors?: ").lower()
    
    if Player == AI:
        print("Computer chose ", AI)
        print("It's a tie!")

    elif Player == "rock":
        if AI == "paper":
            print("Computer chose ", AI)
            print("You lose!")
        if AI == "scissors":
            print("Computer chose ", AI)
            print("You win!")

    elif Player == "paper":
        if AI == "rock":
            print("Computer chose ", AI)
            print("You win!")
        if AI == "scissors":
            print("Computer chose ", AI)
            print("You lose!")
            
    elif Player == "scissors":
        if AI == "paper":
            print("Computer chose ", AI)
            print("You win!")
        if AI == "rock":
            print("Computer chose ", AI)
            print("You lose!")

    p_again = input("Wanna play again? (yes/no): ").lower()

    if p_again != "yes":
        break
    else:
        clear()

print("Bye!")
