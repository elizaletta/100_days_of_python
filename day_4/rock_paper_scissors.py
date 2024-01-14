#Make a rock, paper, scissors game.
import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

if user_input == 0:
    print(rock)
elif user_input == 1:
    print(paper)
elif user_input == 2:
    print(scissors)
else:
    print("Oops, there is a mistake. You should enter only 0, 1 or 2.")
    exit()

chioce_list = [rock, paper, scissors]

computer_choice = random.choice(chioce_list)

print(f"Computer choice is {computer_choice}")

if (user_input == 0 and computer_choice == rock) or (user_input == 1 and computer_choice == paper) or (user_input == 2 and computer_choice == scissors):
    print("It's a draw.")
elif (user_input == 0 and computer_choice == scissors) or (user_input == 1 and computer_choice == rock) or (user_input == 2 and computer_choice == paper):
    print("You win!")
else:
    print("You've lost the game.")