from art import logo
from game import *

print(logo)
retry_game = True

while retry_game:
    run_game()
    retry_game = input("Do you want to start a new game? Type 'Y' to yes or 'N' to no: ").lower() == "y"