# Print numbers from 1 to 5 in a same column. 
for i in range(1, 6):
    print(i)


# Print numbers from 1 to 5 in a same rows
for i in range(1, 6):
    print(i, end=",")

print() # prints a blank line


# Print reverse number from 5 to 1 in same rows.
for i in range(5, 0, -1):
    print(i, end=",")

print() 

# Print numbers divisible by 3 between 1 and 50.
for num in range(1,51):
    if num % 3 == 0:
        print(num, end=",")

print() 


# Print numbers divisible by both 3 and 5 between 1 and 100.
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(num, end=",")

print() 

# Count How many numbers between 1 and 100 are divisible by 7.
count = 0
for i in range(1, 101):
    if i % 7 == 0:
        count += 1

print(count)


# Find factorial of given number.
num = int(input("Enter a Factorial Number: "))

factorial = 1

for i in range(1, num + 1):
    factorial *= i

print("Factorial:", factorial)


# Calculate power without using **.
base = int(input("Enter a Number: "))
power = int(input("Enter Number's Power: "))
result = 1

for i in range(power):
    result *= base

print("Power:", result)


# Reverse counting from 100 to 1.
for i in range(100, 0, -1):
    print(i, end=",")

print() 
