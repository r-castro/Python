# Double-subscripted list example.


def print_grades(grades):
    students = len(grades)
    exams = len(grades[0])

    print("The list is:")
    print("            ")

    for i in range(exams):
        print("[%d]" % i, end=" ")

    print()

    for i in range(students):
        print("grades[%d]  " % i, end=" ")

        for j in range(exams):
            print(grades[i][j], "", end=" ")

        print()

        
def minimum(grades):
    low_score = 100

    for studentExams in grades:
        for score in studentExams:
            if score < low_score:
                low_score = score
    return low_score


def maximum(grades):
    high_score = 0

    for student_exams in grades:
        for score in student_exams:
            if score > high_score:
                high_score = score
    return high_score


def average(setofgrades):
    total = 0.0

    for grade in setofgrades:
        total += grade

    return total / len(setofgrades)

grades = [[77, 68, 86, 73],
          [96, 87, 89, 81],
          [70, 90, 86, 81]]

print_grades(grades)
print("\n\nLowest grade:", minimum(grades))
print("Highest grade:", maximum(grades))
print("\n")

for i in range(len(grades)):
    print("Average for student", i, "is", average(grades[i]))
