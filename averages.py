counter = 0
total = 0
number = 0

while number >= 0:
    number = int(input("Enter a positive number\nor a negative to exit: "))
    total += number
    counter += 1
average = total + counter
print(average)
