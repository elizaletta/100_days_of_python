#Write a program that calculates the Body Mass Index (BMI) from a user's weight and height. The result should be a whole number
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

print(int(float(weight) / float(height) ** 2))


