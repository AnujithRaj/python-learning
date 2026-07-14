# Check whether a number is a three-digit number.
number = int(input("Enter a Three-digit Number: "))

if 100 <= abs(number) <= 999:
    print("Three Digit Number")
else:
    print("Not Three Digit Number")


# Check whether a number is a two-digit number.
num = int(input("Enter a Two-digit Number: "))

if 10 <= abs(num) <= 99:
    print("Two Digit Number")
else:
    print("Not Two Digit Number")


# Find the middle value among three numbers.
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

if (num1 >= num2 and num1 <= num3) or (num1 <= num2 and num1 >= num3):
    print(num1, "Middle Value")
elif (num2 >= num1 and num2 <= num3) or (num2 <= num1 and num2 >= num3):
    print(num2, "Middle Value")
else:
    print(num3, "Middle Value")


# Determine the type of triangle: Equilateral, Isosceles, Scalene
side1 = int(input("Enter Tringle Side 1: "))
side2 = int(input("Enter Tringle Side 2: "))
side3 = int(input("Enter Tringle Side 3: "))

if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
    if side1 == side2 and side2 == side3:
        print("Equilateral Triangle")
    elif side1 == side2 or side2 == side3 or side3 == side1:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangle")
else:
    print("Invalid Triangle")


# Determine the quadrant of a point (x, y).
x = int(input("Enter Value of x: "))
y = int(input("Enter Value of y: "))

if x == 0 and y == 0:
    print("Origin")
elif x == 0:
    print("On Y-axis")
elif y == 0:
    print("On X-axis")
elif x > 0 and y > 0:
    print("Quadrant I")
elif x < 0 and y > 0:
    print("Quadrant II")
elif x < 0 and y < 0:
    print("Quadrant III")
else:
    print("Quadrant IV")


# Check whether a character is uppercase or lowercase.
char = input("Enter a Character: ")
if len(char) != 1:
    print("Invalid Character")
elif char.isupper():
    print("UpperCase:", char)
elif char.islower():
    print("LowerCase:", char)
else:
    print("Not Character")


# Check whether a character is alphabet, digit, or special character.
character = input("Enter a Character: ")

if len(character) != 1:
    print("Invalid Character")
elif character.isalpha():
    print("Alphabet")
elif character.isdigit():
    print("Digit")
else:
    print("Special Character")


# Determine the number of days in a month.
month_number = int(input("Enter Month number: "))

if month_number in (1, 3, 5, 7, 8, 10, 12):
    print("Days: 31")
elif month_number in (4, 6, 9, 11):
    print("Days: 30")
elif month_number == 2:
    print("Days: 28 or 29")
else:
    print("Invalid Month")


# Check whether a number is a palindrome.
number1 = int(input("Enter a Number: "))
str_number = str(number1)

if str_number == str_number[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# Check whether a number is an Armstrong number.
number2 = int(input("Enter a Number: "))

digits = len(str(number2))
sum = 0

for digit in str(number2):
    sum += int(digit) ** digits

if sum == number2:
    print("Armstrong Number")
else:
    print("Not Armstrong Number")




