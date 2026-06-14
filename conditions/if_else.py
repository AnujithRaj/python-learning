# Find the larger of two numbers.
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number:"))

if a > b:
    print(a, "is Larger")
else:
    print(b, "is Larger")


# Check whether a number is even or odd.
number = int(input("Enter Number: "))

if number % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")


# Check whether a number is positive or negative.
if number >= 0:
    print("Positive")
else:
    print("Negative")


# Check whether a year is a leap year (basic version).
year = int(input("Enter Year: "))

if year % 4 == 0:
    print("Leap Year")
else:
    print("Not a Leap year")


# Check whether a character is a vowel or consonant.
ch = input("Enter a Character: ").lower()

if ch in "aeiou":
    print("Vowel")
else:
    print("Consonant")

    
# Check whether a number is divisible by both 3 and 5.
num = int(input("Enter Number: "))

if num % 3 == 0 and num % 5 == 0:
    print("Divisible by Both 3 and 5")
else:
    print("Not Divisible")

    
# Check whether a number is a multiple of 7.
num1 = int(input("Enter Number: "))

if num1 % 7 == 0:
    print("Multiple of 7")
else:
    print("Not Multiple of 7")


# Check whether a student passed or failed.
marks = int(input("Enter Marks: "))

if marks >= 40:
    print("Passed")
else:
    print("Failed")


# Check whether a person can get a driving license (18+).
age = int(input("Enter Age: "))

if age >= 18:
    print("Eligible for driving license")
else:
    print("Not Eligible")


# Check whether a number is within the range 1–100.
if 1 <= num1 <= 100:
    print("Number in range 1-100")
else:
    print("Out of range")