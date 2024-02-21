# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.
"""def greet():
    print('Hi')
    print('Nice to see you!')
    print('Welcome to Python')

greet()

#functions_with_input
def greet_with_name(name):
    print(f'Hi {name}')
    print(f'Nice to see you {name}!')
    print(f'Welcome to Python, {name}')

greet_with_name("Liza")"""
#Liza is a new variable, like name = "Liza", name is the parameter, Liza is the argument
#functions with more than 1 input
def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with("Liza", "Warsaw")
greet_with(location="Minsk", name="Liza")