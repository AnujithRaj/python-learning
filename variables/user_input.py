# Take user's name as input and print a greeting.
name = input("Enter Your Name: ")

print(f"Welcome: {name}")


# Take age as input and print it.
age = input("Enter Age: ")

print(f"You are {age} year old.")


# Take two numbers and print their sum.
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print(f"Sum of Numbers is: {num1 + num2}")


# Take two numbers and print their multiplication.
number1 = int(input("Enter First Number: "))
number2 = int(input("Enter Second Number: "))

print(f"Multiplication of Numbers is: {number1 * number2}")


# Take length and width and find area.
length = int(input("Enter Length: "))
width = int(input("Enter Width: "))

area = length * width

print(f"Area: {area}")


# Take temperature in Celsius and convert to Fahrenheit.
celsius = float(input("Enter Temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print(f"Temperature in Fahrenheit: {fahrenheit}")


# Take marks in 5 subjects and calculate total.
science = int(input("Enter Science Marks: "))
math = int(input("Enter Math Marks: "))
english = int(input("Enter English Marks: "))
hindi = int(input("Enter Hindi Marks: "))
sanskrit = int(input("Enter Sanskrit Marks: "))

total_marks = science + math + english + hindi + sanskrit

print(f"Total Marks: {total_marks}")


# Calculate average marks.
avg = total_marks / 5

print(f"Average Marks: {avg}")


# Calculate percentage marks.
percent = (total_marks / 500) * 100

print(f"Percentage Marks: {percent}")


# Convert kilometers into meters.
kmetr = int(input("Enter Distance in Kilometers: "))

metr = kmetr * 1000

print(f"Distance in meter: {metr}")

