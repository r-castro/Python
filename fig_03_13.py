# Class average pringram with sentinel-controlled repetition

total = 0
gradeCounter = 0

grade = input("Enter grade, -1 to end: ")
grade  = int(grade)

while grade != -1:
    total = total + grade
    gradeCounter = gradeCounter + 1
    grade = input("Enter grade, -1 to end: ")
    grade = int(grade)

if gradeCounter != 0:
    average = float(total) / gradeCounter
    print("Class average is", average)
else:
    print("Na grades were entered")
