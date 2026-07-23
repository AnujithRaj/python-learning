# Print a Square of *.
sq_size = 5
for i in range(sq_size):
    for j in range(sq_size):
        print("*", end=" ")
    print()


# Print Number Square
num_sq = 4

for i in range(1, num_sq+1):
    for j in range(1, num_sq+1):
        print(j, end=" ")
    print()


# Print multiplication table from 1 to n.
table_size = int(input("Enter a Number for multiplication table: "))

for i in range(1, table_size+1):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")
    print()


# Print all coordinate pairs.
n_pairs = int(input("Enter a Number for coordinat pairs: "))

for i in range(n_pairs):
    for j in range(n_pairs):
        print(f"{i}, {j}")

        
# Count total iterations in a nested loop.
n = int(input("Enter a Number for Iterations: "))

count = 0

for i in range(n):
    for j in range(n):
        count += 1

print("Total Iterations:", count)


# Print all pairs from two lists.
list1 = list(map(int, input("Enter First List Elements: ").split()))
list2 = list(map(int, input("Enter Second List Elements: ").split()))

for i in list1:
    for j in list2:
        print(i, j)


# For a matrix of size n x n, print the sum of numbers in each row.
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

for row in matrix:
    total = 0
    for num in row:
        total += num
    print(total)


# Without Using a counter outside the loops, determine how many times the inner loop executes.
n = 8

total = sum(1 for i in range(n) for j in range(n))

print(total)


# Print Right Triangel Pattern.
triangle_rows = 5

for i in range(1, triangle_rows+1):
    for j in range(i):
        print("*", end=" ")
    print()

# Print Inverted Triangle.
inverted_rows = 5

for i in range(inverted_rows, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()


# Print Consecutive Numbers.
consecutive_num = 5
num = 1

for i in range(consecutive_num):
    for j in range(consecutive_num):
        print(num, end=" ")
        num += 1
    print()


# Print Chessboard Pattern.
chessboard_size = 8 

for i in range(chessboard_size):
    for j in range(chessboard_size):
        if (i + j) % 2 == 0:
            print("X", end=" ")
        else:
            print("O", end=" ")
    print()

# Hollow square
hollow_size = 5

for i in range(hollow_size):
    for j in range(hollow_size):
        if i == 0 or i == hollow_size-1 or j == 0 or j == hollow_size-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# Floyd's triangle
floyd_size = 5
current_num = 1

for i in range(1, floyd_size+1):
    for j in range(i):
        print(current_num, end=" ")
        current_num += 1
    print()


# Pascal's triangle
pascal_rows = 5 

for i in range(pascal_rows):
    value = 1
    for j in range(i + 1):
        print(value, end=" ")
        value = value * (i -j) // (j + 1)
    print()


# Pyramid of *
pyramid_rows = 5
for i in range(pyramid_rows):
    for j in range(pyramid_rows - i-1):
        print(" ", end="")

    for j in range(2 * i+1):
        print("*", end="")
    print()


# Diamond pattern
pattern_size = 5

for i in range(pattern_size):  # Upper part
    for j in range(pattern_size - i-1):
        print(" ", end="")
    for j in range(2 * i+1):
        print("*", end="")
    print()

for i in range(pattern_size - 2, -1, -1):  # Lower part
    for j in range(pattern_size - i -1):
        print(" ", end="")
    for j in range(2 * i+1):
        print("*", end="")
    print()


# Multiplication table from 1 to 10
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i * j}")

print()


# Matrix addition
A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]

result = []

for i in range(len(A)):
    row = []
    for j in range(len(A[0])):
        row.append(A[i][j] + B[i][j])
    result.append(row)

for row in result:
    print(row)


# Matrix transpose
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
rows = len(matrix)
cols = len(matrix[0])

for j in range(cols):
    for i in range(rows):
        print(matrix[i][j], end=" ")
    print()


# Identity matrix
identity_rows = 5

for i in range(identity_rows):
    for j in range(identity_rows):
        if i == j:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print()
