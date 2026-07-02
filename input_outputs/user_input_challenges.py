# Take birth year and calculate age.
current_year = 2026
birth_year = int(input("Enter Birth Year: "))

age = current_year - birth_year
print("Age:", age)


# Take total seconds and convert into hours, minutes, and seconds.
seconds = int(input("Enter Seconds: "))

hours = seconds // 3600
remaining_seconds = seconds % 3600

minutes = remaining_seconds // 60
remain_seconds = remaining_seconds % 60

print(f"Hours: {hours}, Minutes: {minutes}, Seconds:{remain_seconds}")


# Take amount in rupees and convert to paise.
rupees = float(input("Enter Amount in Rupees: "))

paise = rupees * 100
print("Amount in Paise:", paise)


# Take two numbers and swap them using input/output.
number1, number2 = map(int, input("Enter First & Second Number: ").split())

number1, number2 = number2, number1

print("First Number:", number1)
print("Second Number:", number2)


# Take a 3-digit number and print each digit separately.
num1 = int(input("Enter a 3-digit Number: "))

hundreds = num1 // 100
tens = (num1 // 10) % 10
ones = num1 % 10

print("Hundreds:", hundreds)
print("Tens:", tens)
print("Ones:", ones)


# Take a 4-digit number and print the sum of its digits.
num_digit = int(input("Enter 4-digit Number: "))

d1 = num_digit // 1000
d2 = (num_digit // 100) % 10
d3 = (num_digit // 10) % 10
d4 = num_digit % 10

sum_digits = d1 + d2 + d3 + d4
print("Sum of digits:", sum_digits)


# Take a number and print whether it is positive, negative, or zero.
number = int(input("Enter a Number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero") 


# Take user details (name, age, city) and display them in a neat format.
name = input("Enter Your Name: ")
age = int(input("Enter Your age: "))
city = input("Enter Your City: ")

print(f"Name: {name}, Age: {age}, City: {city}")


# Create a mini student report card using inputs.
student_name = input("Enter Student Name: ")

math = int(input("Math Marks: "))
science = int(input("Science Marks: "))
english = int(input("English Marks: "))

total_marks = math + science + english
percentage = total_marks / 3

print("\n----- Report Card -----")
print("Name:", student_name)
print("Total:", total_marks)
print("Percentage:", percentage)


# Create a mini ATM balance display program using input.
holder_name = input("Enter Account Holder Name: ")
balance = float(input("Enter Account Balance: "))

print("\n------ ATM ------")
print("Account Holder:", holder_name)
print("Available Balance: ₹", balance)
print("Thank You!")