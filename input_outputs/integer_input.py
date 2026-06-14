# Take an integer and print its square.
integer1 = int(input("Enter an Integer Number: "))

sqr = integer1 ** 2
print("Square of Integer:", sqr)


# Take an integer and print its cube.
cube = integer1 ** 3
print("Cube of Integer:", cube)


# Take a number and print its double.
double = integer1 * 2
print("Double of Integer:", double)


# Take a number and print its half.
half = integer1 / 2
print("Half of Integer:", half)
# Take two integers and print their sum.
integer2 = int(input("Enter Second Integer Number: "))

sum_result = integer1 + integer2
print("Sum of Integers:", sum_result)


# Take two integers and print their difference.
diff = integer1 - integer2
print("Difference of Integers:", diff)


# Take two integers and print their product.
product = integer1 * integer2
print("Product of Integers:", product)


# Take two integers and print their quotient.
if integer2 != 0:
    quotient = integer1 / integer2
    print("Quotient of Integers:", quotient)
else:
    print("Division by zero is not allowed.")