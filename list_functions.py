# Passing lists and individual list elements to functions


def modify_list(alist):
    for i in range(len(alist)):
        alist[i] *= 2


def modify_element(element):
    element *= 2

alist = [1, 2, 3, 4, 5]

print("Effects of passing entire list:")
print("The values of the original list are:")

for item in alist:
    print(item)

modify_list(alist)

print("\n\nThe values of the modified list are:")

for item in alist:
    print(item)

print("\n\nEffects of passing list element:")
print("alist[3] before modify_element:", alist[3])
modify_element(alist[3])
print("alist[3] after modify_element:", alist[3])

print("\n\nEffects of passing slices of list:")
print("alist[2:4] before modify_list:", alist[2:4])
modify_list(alist[2:4])
print("alist[2:4] after modify_list:", alist[2:4])
