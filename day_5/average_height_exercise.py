#You are going to write a program that calculates the average student height from a List of heights.
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
total_height = 0
for height in student_heights:
  total_height += height

print(f'Total height is {total_height}')

number_of_students = 0

for student in student_heights:
  number_of_students += 1

print(f'Total number of students is {number_of_students}')

average_height = round(total_height / number_of_students)

print(f'The average student height in class in {average_height}.')

#Write your code below this row 👇