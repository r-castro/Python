# Recursive fibonacci function.


def fibonacci(n):
    if n < 0:
        print("Cannot find the fibonacci of a negative number.")

    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

number = int(input("Enter an integer: "))
result = fibonacci(number)
print("Fibonacci(%d) = %d" % (number, result))
