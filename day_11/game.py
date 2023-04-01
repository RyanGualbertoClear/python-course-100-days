from helpers import *
import random

def run_game():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_cards = []
    computer_cards = []


    def get_user_new_card():
        user_cards.append(random.choice(cards))
        return print_current_score(user_cards)


    def get_computer_cards():
        computer_cards.append(random.choice(cards))
        return print_current_score(computer_cards)

    def setup_init_game():
        user_cards.append(random.choice(cards))
        user_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
        computer_cards.append(random.choice(cards))
        print_current_score(user_cards)
        print(f"Computers first card: {computer_cards[0]}")

    game_over = False
    setup_init_game()
    if verify_blackjack(user_cards):
        return print("User wins, BLACKJACK!!!")
    if verify_blackjack(computer_cards):
        return print("Computer wins, BLACKJACK!!!")
    else:
        if verify_if_has_looser(user_cards, computer_cards):
            game_over = True
        while game_over == False:
            user_decision = input(
                "Type 'Y' to get other card or type 'n' to show cards: ")
            if (user_decision.lower() == "y"):
                get_user_new_card()
                if verify_if_has_looser(user_cards, computer_cards):
                    game_over = True
            else:
                get_computer_cards()
                verify_result(user_cards, computer_cards)
                game_over = True
