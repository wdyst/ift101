# Start Lab 6
# Write a program that prompts the user to enter a number 'n' and print out the sum of the first n natural numbers, and the sum of the cubes of the first n natural numbers
n = int(input("Enter a number: "))
def sumN(n):
    if n <= 1:
        return n
    else:
        return n + sumN(n - 1)
def sumNCubes(n):
    if n <= 1:
        return n
    else:
        return n**3 + sumNCubes(n - 1)
print("Sum of first", n, "natural numbers is", sumN(n))
print("Sum of first", n, "cubes is", sumNCubes(n))
# End of sum of first 'n' natural numbers

# Write a function to compute the nth Fibonacci number.
n = int(input("Enter a number: "))
def fib_sec(n):
    if n <= 1:
        return n
    else:
        return fib_sec(n-1) + fib_sec(n-2)
print("Fibonacci sequence:")
for i in range(n):
    print(fib_sec(i))
# End of fibonacci sequence

# Write a function to compute the factorial of a number.
n = int(input("Enter a number: "))
def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n - 1)
# Main
print("Factorial of", n, "is", fact(n))
# End of factorial of a number
# End Lab 6