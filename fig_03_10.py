# Class average program with counter-controlled repetition

total = 0
gradecounter = 1

while gradecounter <= 10:
    grade = input("Enter grade: ")
    grade = int(grade)
    total = total + grade
    gradecounter = gradecounter + 1

average = total / 10
print("Class average is", average)
