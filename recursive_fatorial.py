

def factorial(number):

    if number <= 1:
        return 1
    else:
        return number * factorial(number - 1)

for i in range(11):
    print("%2d! = %d" % (i, factorial(i)))
