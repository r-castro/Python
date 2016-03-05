# Unpacking sequences.

astring = "abc"
alist = [1, 2, 3]
atuple = "a", "A", 1

print("Unpacking string...")
first, second, third = astring
print("String values:", first, second, third)

print("\nUnpacking list...")
first, second, third = alist
print("List values:", first, second, third)

print("\nUnpacking tuple...")
first, second, third = atuple
print("Tuple values:", first, second, third)

x = 3
y = 4

print("\nBefore swapping: x = %d, y = %d" % (x, y))
x, y = y, x
print("After swapping: x = %d, y = %d" % (x, y))
