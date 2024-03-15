from auctionary_art import art

import os

print(art)

def who_wins_function(bidding_record):
    highest_bid = 0
    winner = ""
    for each_bidder in bidding_record:
        bid_amount = bidding_record[each_bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = each_bidder
    print(f"The winner is {winner} with a bid of ${highest_bid}.")

bids = {}

print("Welcome to the Secret Auctionary!")

many_players = True

while many_players:

    name = input("What is your name?\n")

    bid = int(input("What is your bid?\n$"))

    bids[name] = bid

    question = input("Are there any other players? Type yes or no.\n").lower()

    if question == "no":
        
        many_players = False

        who_wins_function(bids)
    
    elif question == "yes":
        
        os.system('clear')
