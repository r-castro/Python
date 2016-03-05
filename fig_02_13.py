# Displaying an object's location, type and value


integer1 = input("Enter first integer:\n")
print("integer1: ", id(integer1), type(integer1), integer1)
integer1 = int(integer1)
print("integer1: ", id(integer1), type(integer1), integer1)

integer2 = input("Enter second integer:\n")
print("integer2: ", id(integer2), type(integer2), integer2)
integer2 = int(integer2)
print("integer2: ", id(integer2), type(integer2), integer2)

sum = integer1 + integer2
print("Sum is: ", id(sum), type(sum), sum)
