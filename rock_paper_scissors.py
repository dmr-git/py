import random as rand

choices = ['rock', 'paper', 'scissors']
computer_choice = rand.choice(choices)

user_choice = input("Do you want rock, paper, or scissors?\n")

print(f"Computer selected {computer_choice}.", end = " ")

if computer_choice == user_choice:
    print('TIE!')
elif user_choice == 'rock' and computer_choice == 'scissors':
    print("You win.")
elif user_choice == 'scissors' and computer_choice == 'paper':     
    print("You win.")
elif user_choice == 'paper' and computer_choice == 'rock':
    print("You win.")
else:
    print("You lose.")     