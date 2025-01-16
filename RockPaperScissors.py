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
possible_choices = [rock, paper, scissors]
players_choice = int(input("What do you choose? "
                           "Type 0 for Rock, "
                           "1 for Paper "
                           "or 2 for Scissors.\n"))

if players_choice >=0 and players_choice <=2:
    print(possible_choices[players_choice])

computer_choice = random.randint(0,2)
print("Computer chose: ")
print((possible_choices[computer_choice]))

if players_choice>=3 or players_choice < 0:
    print("You typed an invalid number. You lose")
elif players_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and players_choice == 2:
    print("You lose!")
elif computer_choice > players_choice:
    print("You lose!")
elif computer_choice == players_choice:
    print("It's a draw!")
elif players_choice > computer_choice:
    print("You win!")




