bidders = []
stopped_program = False

while stopped_program == False:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bidder = {}
    bidder["name"] = name
    bidder["bid"] = bid
    bidders.append(bidder)
    stopped_program = input(
        "Are There any others bidders? Type 'Yes' or 'No'.").lower() == 'no'

highest_bid = 0

for bidder in bidders:
    if bidder["bid"] > highest_bid:
        highest_bid = bidder["bid"]
        winner = bidder["name"]

print(f"The winner is {winner} with a bid of ${highest_bid}")
