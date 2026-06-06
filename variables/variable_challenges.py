# Swap two variables without using a third variable.
a = 20
b = 10

a, b = b, a

print("First Variable:", a, "Second Variable:", b)


# Swap three variables cyclically.
val1 = 12
val2 = 28
val3 = 64

val1, val2, val3 = val3, val1, val2

print("First Value:", val1)
print("Second Value:", val2)
print("Third Value:", val3)


# Convert total seconds into hours, minutes, and seconds.
total_seconds = int(input("Enter total second: "))

hours = total_seconds // 3600
remain_seconds = total_seconds % 3600

minutes = remain_seconds // 60
seconds = remain_seconds % 60

print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)


# Find the last digit of a number.
number = int(input("Enter a number: "))

last_digit = number % 10

print("Last digit:", last_digit)


# Find the number of digits in a number using variables.
number = int(input("Enter a number: "))

count = 0
temp = abs(number)  # handles negative numbers

if temp == 0:
    count = 1
else:
    while temp > 0:
        temp = temp // 10
        count += 1

print("Number of difits:", count)


# Reverse a 3-digit number.
number = int(input("Enter a 3-digit number: "))

hundreds = number // 100
tens = (number // 10) % 10
ones = number % 10

reverse = ones * 100 + tens * 10 + hundreds

print("Reversed number:", reverse)


# Find the sum of digits of a 5-digit number.
number = int(input("Enter a 5-digit number: "))

digit1 = number // 10000
digit2 = (number // 1000) % 10
digit3 = (number // 100) % 10
digit4 = (number // 10) % 10
digit5 = number % 10

sum_of_digits = digit1 + digit2 + digit3 + digit4 + digit5

print("Sum of digits:", sum_of_digits)

# Convert days into years, months, and days.
total_days = int(input("Enter total day: "))

years = total_days // 365
remain_days = total_days % 365

months = remain_days // 30
days = remain_days % 30

print("Years:", years)
print("Months:", months)
print("Days:", days)


# Calculate electricity bill using unit consumption.
units = int(input("Enter units consumed: "))

if units <= 100:
    bill = units * 1.5

elif units <= 200:
    bill = (100 * 1.5) + ((units - 100) * 2.5)

else:
    bill = (100 * 1.5) + (100 * 2.5) + ((units -200) * 4)

print("Electricity bill:", bill)


# Calculate compound interest.
principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (%): "))
time = float(input("Enter time (years): "))

amount = principal * (1 + rate /100) ** time
compound_interest = amount - principal

print("Amount:", round(amount, 2))
print("Compount Interest: ", round(compound_interest, 2))