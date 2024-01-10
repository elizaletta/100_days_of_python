#Your first job is to build an automatic pizza order program.
print("Welcome to Python Pizza Deliveries!")
print("In our menu we have small pizza for $15, medium Pizza for $20 and large pizza for 25$.")
bill = 0
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? It will cost +2$ for small pizza and +3$ for medium and large. Y or N? ")
extra_cheese = input("Do you want extra cheese? It will cost additional 1$. Y or N? ")
if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1
if size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
if size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1
print(f"Thanks for the order, your final bill is ${bill}.")