# Fibonacci sequence
def fib_sec(n):
    if n <= 1:
        return n
    else:
        return fib_sec(n-1) + fib_sec(n-2)

# Main
n = int(input("Enter a number: "))
if n <= 0:
    print("Enter a positive number")
else:
    print("Fibonacci sequence:")
    for i in range(n):
        print(fib_sec(i))
# End of fibonacci sequence

# Factorial of a number
n = int(input("Enter a number: "))


def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n - 1)
# Main
print("Factorial of", n, "is", fact(n))

# End of factorial of a number

# Sum of first 'n' natural numbers and prints it. N is taken from user input.
n = int(input("Enter a number: "))
def sum(n):
    if n <= 1:
        return n
    else:
        return n + sum(n - 1)
# Main
print("Sum of first", n, "natural numbers is", sum(n))

# End of sum of first 'n' natural numbers

# Program that draws a diamond shaper pattern using user input to determine the number of rows.
rows = int(input("Enter a number of rows: "))
def diamond(rows):
    for i in range(rows):
        for j in range(rows - i):
            print(" ", end="")
        for k in range(i + 1):
            print("* ", end="")
        print()
    for i in range(rows - 1, 0, -1):
        for j in range(rows - i):
            print(" ", end="")
        for k in range(i):
            print("* ", end="")
        print()
# Main
diamond(rows)
# End of diamond pattern

# End of lab4.py
