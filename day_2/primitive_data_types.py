#counting starts from zero - use [] to single out the necessary string from the row

#subscripting - pulling out a particular element from the string

print("Elizabeth"[3])

#Integer - whole nembers

#Large number that in real life are separated with a comma like in the UK can be separated with an underscore

print(123 + 345)

print(123_456_678)

#float -floating point number like 3.456

#boolean - True or False

#type() - shows the data type

num_char = len(input("What is your name?"))
print(type(num_char))

#type conversion or type casting a = str(b), where b is int

num_char = len(input("What is your name?"))
new_num_char = str(num_char)
print('Your name has ' + new_num_char + ' characters.')

# we can also convert int to float, or string to float

print(123 + 456)
print(str(123) + str(456))
print(45 + float("100.6"))
print(int("4") + int("5"))
print(int(10.6))
a = 10.6
print(type(a))
a = int(10.6)
print(type(a))
print(a)

