# Print numbers from 1 to 10 using a for loop.
for i in range(1,11):
    print(i)


# Print numbers from 10 to 1.
for i in range(10, 0, -1):
    print(i)


# Print all even numbers fro 1 to 20.
for i in range(2, 21, 2):
    print(i)


# Print all odd numbers from 1 to 20.
for i in range(1, 21, 2):
    print(i)


# Print the multiplication table of 5.
for i in range(1, 11):
    print(f"5 x {i} = {5 * i}")


# Print squares of number from 1 to 10.
for i in range(1, 11):
    print(i ** 2)


# Print cubes of numbers from 1 to 10.
for i in range(1, 11):
    print(i ** 3)


# Find the sum of numbers from 1 to 100.
total = 0

for i in range(1, 101):
    total += i

print(total)


# Find the sum of all even numbers from 1 to 100.
total = 0

for i in range(2, 101, 2):
    total += i

print(total)


# Find the sum of all odd numbers from 1 to 100.
total = 0

for i in range(1, 101, 2):
    total += i

print(total)

