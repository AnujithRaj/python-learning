# Create a variable storing your age.
age = int(input("Enter Your age: "))

print("Age:", age)


# Add 10 to the age and print the result.
age += 10

print("New Age:", age)


# Find the type of an integer variable.
int1 = int(input("Enter Number: "))

print(type(int1))

# Calculate the square of a number.
number = int(input("Enter Number: "))

sqr = number ** 2

print("Squre of Number:", sqr)

# Find whether a number is even or odd.
num = int(input("Enter Number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
