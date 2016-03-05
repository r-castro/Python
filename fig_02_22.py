# Compare integers using if structures, relational operators

print("Enter two integers, and I will tell you")
print("the relationschips they satisfy.")

number1 = input("Please enter first integer: ")
number1 = int(number1)

number2 = input("Please enter second integer: ")
number2 = int(number2)

if number1 == number2:
    print("%d is equal to %d" % (number1, number2))

if number1 != number2:
    print("%d is not equal to %d" % (number1, number2))

if number1 < number2:
    print("%d is less than %d" % (number1, number2))

if number1 > number2:
    print("%d is greater then %d" % (number1, number2))

if number1 <= number2:
    print("%d is less then or equal to %d" % (number1, number2))

if number1 >= number2:
    print("%d is greater then or equal to %d" % (number1, number2))
