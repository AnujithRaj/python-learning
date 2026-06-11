# Create a tuple of 5 numbers.
tup1 = (20, 30, 50, 10, 11)
print("Tuple:", tup1)


# Access the second element.
second_element = tup1[1]
print("Second Element:", second_element)


# Find tuple length.
print("Length:", len(tup1))


# Count occurrence of a value.
print("Occurrrence of 10:", tup1.count(10))


# Find index of an element.
print("Index of 50:", tup1.index(50))

# Convert tuple to list and modify it.
tuple1 = (33, 59, 14, 67, 23, 93, 45)
list1 = list(tuple1)
list1.append(11)
print("Modified List:", list1)


# Find maximum element.
print("Maximum:", max(tuple1))


# Find minimum element.
print("Minimum:", min(tuple1))


# Find sum of tuple elements.
print("Sum:", sum(tuple1))


# Unpack tuple values into variables.
a, b, c, d, e, f, g = tuple1

print("Unpacked Values:", a, b, c, d, e, f, g)