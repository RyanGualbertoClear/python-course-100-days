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
import random
options = [rock,paper,scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_choice = random.randint(0,2)

print(options[user_choice])
print("Computer chose:")
print(options[computer_choice])

if user_choice > computer_choice:
    print("You win")
elif user_choice == computer_choice:
    print("It's a draw")
else:
    print("You lose")