# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

maximum_number = 0
for max_number in student_scores:
  if max_number > maximum_number:
    maximum_number = max_number
print(maximum_number)



