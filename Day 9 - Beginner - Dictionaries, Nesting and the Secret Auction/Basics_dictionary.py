# Programming_dictionary = {"Bug": "Type of an error", "Name": "The name is Sami, Saleh Sami"}
# Programming_dictionary["Loop"] = "Runs again and again till reach the end"
# for key in Programming_dictionary:
#     print(key)
#     print(Programming_dictionary[key])
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62
}
student_grades = {}
for names in student_scores:
    if 91 <= student_scores[names] <= 100:
        student_grades[names] = "outstanding"
    if 81 <= student_scores[names] <= 90:
        student_grades[names] = "Exceeds Expectation"
    if 71 <= student_scores[names] <= 80:
        student_grades[names] = "Acceptable"
    if student_scores[names] <= 70:
        student_grades[names] = "Fail"
print(student_grades)
