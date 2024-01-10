#Take both people's names and check for the number of times the letters in the word TRUE occurs. 
#Then check for the number of times the letters in the word LOVE occurs. Then combine these numbers to make a 2 digit number.
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
combined_name = name1 + name2
new_name = combined_name.lower()
t = new_name.count('t')
r = new_name.count('r')
u = new_name.count('u')
e = new_name.count('e')
total_count1 = t + r + u + e
l = new_name.count('l')
o = new_name.count('o')
v = new_name.count('v')
e = new_name.count('e')
total_count2 = l + o + v + e
score = int(str(total_count1) + str(total_count2))
if (score < 10) or (score > 90):
    print(f"Your score is {score}, you go together like coke and mentos.")
elif (score > 40) and (score < 50):
    print(f"You score is {score}, you are alright together.")
else:
    print(f"Your score is {score}")