#Write a program that adds the digits in a 2 digit number. e.g. if the input was 35, then the output should be 3 + 5 = 8
two_digit_number = input("Type a two digit number: ")

new_two_digit_number = str(two_digit_number)

print(int(new_two_digit_number[0]) + int(new_two_digit_number[1]))