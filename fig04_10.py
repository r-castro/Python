# Scoping example

x = 1


def a():
    x = 25

    print("\nlocal x in a is", x, "after entering a")
    x += 1
    print("local x in a is", x, "before exiting a")


def b():
    global x
    print("\nglobal x is", x, "on entering b")
    x *= 10
    print("global x is", x, "on exiting b")

print("global x is", x)

x = 7
print("globa x is", x)

a()
b()
a()
b()

print("\nglobal x is", x)
