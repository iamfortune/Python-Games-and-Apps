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

#Write your code below this line 👇

print(rock)

game_images = [rock, paper, scissors]

username = input("what is your name? ")
user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
# Here we will add an integer for the user in rock paper and scissor, next we will do the computer choice 

if user_input >= 3 or user_input < 0:
  print("You typed an invalid number, you lose!")
else:
  print(game_images[user_input])
  
  computer_choice = random.randint(0, 2)
  print(f"Computer chose:")
  print(game_images[computer_choice])
  
  if user_input == 0 and computer_choice == 2:
    print(f"{username} wins!")
  elif computer_choice == user_input:
    print("You lose")
  elif computer_choice > user_input:
    print("You lose!")
  elif user_input > computer_choice:
    print(f"{username} wins!")
  elif computer_choice == user_input:
    print("It's a draw") 
    