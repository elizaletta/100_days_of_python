from auctionary_art import art

import os

print(art)
winning_person = ""
winning_bid = int(0)
def who_wins_function(winning_person, winning_bid):
    
    for each_name in bids:
        if bids[name] > winning_bid:
            winning_bid = bids[name]
            winning_person = name

bids = {}

auction_bids = []



print("Welcome to the Secret Auctionary!")

many_players = True

while many_players:

    name = input("What is your name?\n")

    bid = int(input("What is your bid?\n$"))

    bids[name] = bid

    auction_bids.append(bids[name])

    question = input("Are there any other players? Type yes or no.\n").lower()

    if question == "no":
        
        who_wins_function()
        
        many_players = False
    
    os.system('clear')

print(f"The winner is{winning_person} with a bid of ${winning_bid}")
