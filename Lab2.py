# Lab 2
# python library to help do math
import math
## problem 1 variables

### sum variables
x = 6
y = 9

### Area variables
length = 17
width = 38
## problem 2 variables
a = 6
b = 12
c = 24
radius = 7
celsius = 12
farenheit2 = 21
Principal = 5000
APR = 3
time = 10
# problem 1

# Adding numbers
sum = x + y
print("The sum of", x, "and",  y,  "is",  sum)

# Switching variables
print(" ")
print("Switching values now...")
## placeholder variable is used as a temporary variable to enable switching of variable values
placeholder = y
y = x
x = placeholder
print(" ")
print("New value of x =", x)
print("New value of y =", y)

# Calculating the perimeter and area of a rectangle
print(" ")
print("Rectangle related calculations incoming...")
print(" ")
## Area calculation
area = length * width

## Perimeter calculation
perimeter = (length + width) * 2

## printing solutions
print("The area of the rectangle is", area)
print("The perimeter of the rectangle is", perimeter)

# problem 2

#finding the area of a circle
circlearea = math.pi * radius * radius
print(" ")
print("The area of the circle is ", circlearea)
# finding the circumference of a circle
circumference = 2 * math.pi * radius
print(" ")
print("The circumference of the circle is ", circumference)

# temperature conversion
farenheit = (celsius * 1.8) + 32
print(" ")
print(celsius, " celsius in farenheit is", farenheit)
# switch variables to change conversion
changetemp = farenheit
farenheit = farenheit2
farenheit2 = changetemp
celsis = (farenheit - 32) / 1.8
print(" ")
print(farenheit, " farenheit in celsis is", celsis)

# solving the quadratic equation
print(" ")
print("Solving the quadratic equation for", "a =", a, "b =", b, "and c=", c)
print(" ")
## defining the equation
def roots( a, b, c):

    # discriminant calculation
    dis = b * b - 4 * a * c
    sqrtvalue = math.sqrt(abs(dis))

    # checking discriminant solutions
    if dis > 0:
        print(" Real and Different roots ")
        print((-b + sqrtvalue)/(2 * a))
        print((-b - sqrtvalue)/(2 * a))

    elif dis == 0:
        print(" Real and Same roots")
        print(-b / (2 * a))


    else:
        print("Complex roots")
        print(- b / (2 * a), " + i", sqrtvalue)
        print(- b / (2 * a), " - i", sqrtvalue)

# If a is 0, then incorrect equation
## Doesn't matter since a, b, c are static variables in THIS setup
if a == 0:
        print("Not a valid quadratic equation")

else:
    roots(a, b, c)

# Determining compound interest
print(" ")
print("Calculating compound interest for", "$", Principal, "with a", APR, "% interest rate", "for the duration of", time, "years")
print(" ")
Amount = Principal * (1 + APR/100) * time
print(Amount)
