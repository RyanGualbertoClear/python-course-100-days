from users import users;
from vs import vs;
import random


def checkWinner(user_a, user_b):
    if user_a['followers'] > user_b['followers']:
        return 'a'
    else:
        return 'b'
    

score = 0
error_count = 3

def initGame():
    global score
    global error_count
    if len(users) == 0:
        print("You win!")
        return
    selected_user_a_index = random.randint(0, len(users) - 1)
    user_a = users.pop(selected_user_a_index)
    selected_user_b_index = random.randint(0, len(users) - 1)
    user_b = users.pop(selected_user_b_index)
    print(f"Compare A: {user_a['name']}, a {user_a['description']}, from {user_a['country']}")
    print(vs)
    print(f"Against B: {user_b['name']}, a {user_b['description']}, from {user_b['country']}")
    user_choice = input("Who has more followers? Type 'A' or 'B': ").lower()
    if user_choice == checkWinner(user_a, user_b):
        print("You're right! Next round:")
        score += 1
        print(f"Your score is {score}")
        initGame()
    else:
        print("Sorry, that's wrong.")
        error_count -= 1
        print(f"You have {error_count} attempts left.")
        if error_count > 0:
            initGame()
        else:
            print("You lose!")
        
initGame()
