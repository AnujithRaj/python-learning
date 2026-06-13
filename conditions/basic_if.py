# Check whether a number is positive.
number = int(input("Enter Number: "))

if number >= 0:
    print("Positive Number")


# Check whether a number is negative.
if number < 0:
    print("Negative Number")


# Check whether a number is zero.
num = int(input("Enter Number: "))
if num == 0:
    print("Number is Zero")


# Check whether a number is even.
if num % 2 == 0:
    print("Even Number")


# Check whether a number is odd.
if num % 2 != 0:
    print("Odd Number")


# Check whether a person is eligible to vote (18+).
age = int(input("Enter Your Age: "))

if age >= 18:
    print("Eligible for voting")


# Check whether a number is divisible by 5.
num1 = int(input("Enter Number: "))

if num1 % 5 == 0:
    print("Divisible by 5")



# Check whether a number is divisible by 10.
if num1 % 10 == 0:
    print("Divisible by 10")


# Check whether a student has passed (marks ≥ 40).
marks = int(input("Enter Marks: "))

if marks >= 40:
    print("Passed")


# Check whether a person is a senior citizen (age ≥ 60).
person_age = int(input("Enter Age: "))

if person_age >= 60:
    print("Senior Citizen")