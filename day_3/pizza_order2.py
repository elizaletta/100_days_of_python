print("Welcome to Python Pizza Deliveries!")
print("In our menu we have small pizza for $15, medium Pizza for $20 and large pizza for 25$.")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? It will cost +2$ for small pizza and +3$ for medium and large. Y or N? ")
extra_cheese = input("Do you want extra cheese? It will cost additional 1$. Y or N? ")
bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if extra_cheese == "Y":
    bill += 1

print(f"Thanks for the order, your final bill is ${bill}.")
