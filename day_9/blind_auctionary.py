from auctionary_art import art

import os

bids = {}

auction_bids = []

print(art)

print("Welcome to the Secret Auctionary!")

many_players = True

while many_players:

    name = input("What is your name?\n")

    bid = int(input("What is your bid?\n$"))

    bids[name] = bid

    auction_bids.append(bids[name])

    question = input("Are there any other players? Type yes or no.\n").lower()

    if question == "no":
        
        who_wins = max(auction_bids)
        
        many_players = False
    
    os.system('clear')

print(who_wins)
