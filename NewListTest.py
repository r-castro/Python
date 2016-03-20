from NewList import SingleList


def get_integer():
    size = int(input("List size: "))

    return_list = []

    for i in range(size):
        return_list.append(int(input("Integer %d: " % (i + 1))))

    return return_list

print("Creating integers1...")
integers1 = SingleList(get_integer())

print("Creating integers2...")
integers2 = SingleList(get_integer())

print("Size of list integers1 is", len(integers1))
print("List:\n", integers1)

print("Size of list integers2 is", len(integers2))
print("List:\n", end="", integers2)

print("Evaluating integers1 == integers2")

if integers1 == integers2:
    print("They are equal")

print("integers1[0] is", integers1[0])
print("Assignig 0 to integers1[0]")
integers1[0] = 0
print("integers1:", integers1)
