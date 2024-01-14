#You are going to write a program that calculates the sum of all the even numbers from 1 to a particular number from input. 
#Thus, the first even number would be 2
target = int(input("Enter any number from 0 to 1000: "))

sum = 0
for number in range(2, target + 1, 2):
    sum += number
print(sum)