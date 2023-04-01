def calc_current_score(cards):
    return sum(cards)


def verify_if_has_looser(user_cards, computer_cards):
    if calc_current_score(user_cards) > 20:
        print("User lose")
        return "User"
    elif calc_current_score(computer_cards) > 20:
        print("User wins")
        return "Computer"
    else:
        return


def verify_blackjack(user_cards):
    if calc_current_score(user_cards) == 21:
        return True


def print_current_score(user_cards):
    print(f"your cards: {user_cards}, current score: {calc_current_score(user_cards)}")

def verify_result(user_cards, computer_cards):
    if verify_if_has_looser(user_cards, computer_cards) == None:
        is_draw = calc_current_score(user_cards) == calc_current_score(computer_cards)
        if is_draw:
            return print("Is draw")
        user_wins = calc_current_score(user_cards) > calc_current_score(computer_cards)
        print(calc_current_score(user_cards), calc_current_score(computer_cards))
        if (user_wins): 
            return print("User wins")
        else:
            return print("Computer wins")