# Don't change the code below
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

# Write code below this line
highScore = 0
for n in range(0, len(student_scores)):
    if student_scores[n] > highScore:
        highScore = student_scores[n]
    else:
        highScore = highScore

print(f"The highest score in the class is: {highScore}")
