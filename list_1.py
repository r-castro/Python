# Creating, accessing and changing a list.

alist = []

for number in range(1, 11):
    alist += [number]

print("The value of alist is:", alist)

print("\nAceessing values by iteration:")

for item in alist:
    print(item)

print()

print("\nAccessing values by index:")
print("Subscript  Value")

for i in range(len(alist)):
    print("%9d %7d" % (i, alist[i]))

print("\nModifying a list value...")
print("Value of alist before modification:", alist)
alist[0] = -100
alist[-3] = 19
print("Value of alist after modification:", alist)
