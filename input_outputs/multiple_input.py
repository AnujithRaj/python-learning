# Take two numbers in one line and print them separately.
num1, num2 = map(int, input("Enter two numbers: ").split())

print("First Number:", num1)
print("Second Number:", num2)


# Take three numbers and print their sum.
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

print("Sum:", num1 + num2 + num3)


# Take three numbers and print their average.
avg = (num1 + num2 + num3) / 3

print("Average:", avg)


# Take four numbers and print the largest.
num4 = int(input("Enter Fourth Number: "))

largest = max(num1, num2, num3, num4)

print("Largest Number:", largest)

# Take five numbers and print the smallest.
num5 = int(input("Enter Fifth Number: "))

smallest = min(num1, num2, num3, num4, num5)

print("Smallest Number:", smallest)