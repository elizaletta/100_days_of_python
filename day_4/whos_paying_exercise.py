#You are going to write a program which will select a random name from a list of names.
#The person selected will have to pay for everybody's food bill.
names_string = input("Give me everybody's names, separated by a comma. ")
names_separated = names_string.split(", ")
number_of_names = len(names_separated)
import random
random_number = random.randint(0, number_of_names - 1)
whos_paying = names_separated[random_number]
print(whos_paying + " is going to pay the bill today!")

