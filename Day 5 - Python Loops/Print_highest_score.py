# Highest score
student_scores = input("Enter a list of student scores: \n").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
max_func = 0
count = 0
for i in range(0, len(student_scores)):
    if max_func < student_scores[i]:
        max_func = student_scores[i]
print(f"The highest scores in the class is: {max_func}")
