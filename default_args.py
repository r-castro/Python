# Using default arguments.


def box_volume(length=1, width=1, height=1):
    return length * width * height

print("The default box volume is:", box_volume())
print("\nThe volume of a box with length 10,")
print("width 1 and height 1 is:", box_volume(10))
print("\nThe volume of a box with length 10,")
print("width 5 and height 1 is:", box_volume(10, 5))
print("\nThe volume of a box with length 10,")
print("width 5 and height 2 is:", box_volume(10, 5, 2))
