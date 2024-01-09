#Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.
#It should tell them the interpretation of their BMI based on the BMI value.
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = weight / height ** 2
if bmi < 18.5:
    print("Your BMI is " + str(round(bmi, 1)) + ", you are underweight.")
elif bmi < 25:
    print("Your BMI is " + str(round(bmi, 1)) + ", you have a normal weight.")
elif bmi < 30:
    print("Your BMI is " + str(round(bmi, 1)) + ", you are slightly overweight.")
elif bmi < 35:
    print("Your BMI is " + str(round(bmi, 1)) + ", you are obese.")
else:
    print("Your BMI is " + str(round(bmi, 1)) + ", you are clinically overweight.")