# Take a number as input and print its datatype before and after conversion.
number = input("Enter a Number: ")

print("Before conversion:", type(number))

number = int(number)

print("After conversion:", type(number))


# Create a calculator using user input and type casting.
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)

if num2 != 0:
    print("Division:", num1 / num2)
else:
    print("Cannot divide by zero")


# Take a comma-separated string ("10,20,30,40") and convert it into a list of integers.
number = input("Enter numbers separated by commas: ")
result = list(map(int, number.split(",")))

print(result)


# Take a space-separated string of numbers and calculate their sum.
numbers = input("Enter numbers sepatated by spaces: ")
numbers_list = list(map(int, numbers.split()))

print("Sum:", sum(numbers_list))


# Convert a list of numeric strings into a list of integers.
str_list = ["10", "20", "30", "40"]
int_list = list(map(int, str_list))

print(int_list)


# Convert a list of integers into a list of strings.
int_list = [10, 20, 30, 40]

str_list = list(map(str, int_list))
print(str_list)


# Count how many values become True after boolean conversion: [0, 1, "", "Python", [], [1], None]
values = [0, 1, "", "Python", [], [1], None]
count = 0
for value in values:
    if bool(value):
        count += 1

print("True values:", count)


# Take marks as strings and calculate total and percentage.
mark1 = input("Enter mark 1: ")
mark2 = input("Enter mark 2: ")
mark3 = input("Enter mark 3: ")

total = int(mark1) + int(mark2) + int(mark3)
percentage = (total / 300) / 100
print("Total:", total)
print("Percentage:", percentage)


# Convert a string representing a large number into an integer and find whether it is even or odd.
number = input("Enter a large number: ")

number = int(number)

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# Build a mini program that accepts age as input and determines eligibility for voting using type casting.
age = input("Enter your age: ")

age = int(age)

if age >= 18:
    print("Eligible for voting")
else:
    print("Not eligible for voting")