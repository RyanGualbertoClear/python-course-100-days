from art import logo
import random

print(logo)

guess = 0
selected_number = random.randint(0, 100)
difficult = input("Difficult type 'easy' or 'hard': ")
remaining_guesses = 5

if difficult == 'easy':
    remaining_guesses = 10

def verify_guess():
    if guess > selected_number:
        print(f"Too high, you are remainig {remaining_guesses} chances")
        return False
    elif guess < selected_number:
        print(f"Too low, you are remainig {remaining_guesses} chances")
        return False
    elif guess == selected_number:
        print(f"You win, the answer is {selected_number}")
        return True

while (guess != selected_number) and (remaining_guesses > 0):
    guess = int(input("Guess a number from 0 to 100: "))
    remaining_guesses -= 1
    verify_guess()

if verify_guess() == False:
    print("You Loose")
