# Finding the maximum of three integers.

def maximum_value(x, y, z):
    maximum = x

    if y > maximum:
        maximum = y

    if z > maximum:
        maximum = z

    return maximum

a = int(input("Enter first integer: "))
b = int(input("Enter second integer: "))
c = int(input("Enter third integer: "))

print("Maximum integer is:", maximum_value(a, b, c))
print()

d = float(input("Enter first integer: "))
e = float(input("Enter second integer: "))
f = float(input("Enter third integer: "))

print("Maximum float is:", maximum_value(d, e, f))
print()

g = input("Enter first integer: ")
h = input("Enter second integer: ")
i = input("Enter third integer: ")

print("Maximum string is:", maximum_value(g, h, i))
print()
