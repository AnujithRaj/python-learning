import math
# Take an age as input and convert it into an integer.
age = int(input("Enter Your Age: "))

print("Age:", age)


# Take two numbers as input and print their sum.
number1 = int(input("Enter First Number: "))
number2 = int(input("Enter Second Number: "))

print("Sum:", number1 + number2)


# Take a decimal number as input and convert it into a float.
dec_number = float(input("Enter Decimal Number: "))

print("Decimla Number:", dec_number)


# Take a number as input and print its square.
sqr_num = int(input("Enter Number for Square: "))

print("Square:", sqr_num ** 2)


# Take a number as input and print its cube.
cub_num = int(input("Enter Number for Cube: "))

print("Cube:", cub_num ** 3)


# Take the user's height in meters and convert it into a float.

# Take marks in 5 subjects and calculate the average.
maths = int(input("Enter Mathematics Marks: "))
science = int(input("Enter Science Marks: "))
social_science = int(input("Enter Social Science Marks: "))
hindi = int(input("Enter Hindi Marks: "))
sanskrit = int(input("Enter Sanskrit Marks: "))

avg = (maths + science + social_science + hindi + sanskrit) / 5

print("Average Marks:", avg)


# Take the radius of a circle and calculate its area.
radius = float(input("Enter Radius of Circle: "))

circle_area = math.pi * radius ** 2

print("Area of Circle:", circle_area)


# Take length and breadth and calculate area of a rectangle.
length = int(input("Enter Length: "))
breadth = int(input("Enter Breadth: "))

rec_area = length * breadth

print("Area of Rectangle:", rec_area)


# Take principal, rate, and time as input and calculate simple interest.
principal = float(input("Enter Principal: "))
rate = float(input("Enter Rate: "))
time = float(input("Enter Time: "))

si = principal * rate * time / 100

print("Simple Interest:", si)