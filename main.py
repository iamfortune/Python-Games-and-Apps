# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
print(student_heights)

#Write your code below this row 👇

# Getting the total height of students 
total_height = 0
for height in student_heights:
  total_height = total_height + height

# Getting the number of students 
number_of_students = 0
for student in student_heights:
  number_of_students = number_of_students + 1

#Getting the average number of students using the int method to keep it as a whole number

average_num_of_students = total_height/number_of_students
print(int(average_num_of_students))


