# Create a list of 5 fruits.
fruits = ['Apple', 'Banana', 'Mango', 'Grapes', 'Orange']

print("Fruits:", fruits)


# Access the third element.
third_element = fruits[2]

print("Third Element:", third_element)


# Add a new fruit.
fruits.append('Watermelon')

print("Fruits:", fruits)


# Sort the list.
fruits.sort()

print("Sorted List:", fruits)


# Reverse the list.
fruits.reverse()

print("Reversed List:", fruits)


# Find the length of the list.
print("Length:", len(fruits))


# Count occurrence of an element.
print("Apple count:", fruits.count("Apple"))


# Find maximum value in a list.
num1 = [18, 12, 23, 14, 45, 26]

print("Maximum:", max(num1))


# Find minimum value in a list.
print("Minmum:", min(num1))


# Find sum of all numbers.
print("Sum:", sum(num1))


# Find average of list elements.
print("Average:", sum(num1) / len(num1))


# Remove duplicates from a list.
numbers = [10, 20, 20, 30, 30, 40]

unique_numbers = list(set(numbers))

print("Without Duplicates:", unique_numbers)


# Merge two lists.
merge_list = num1 + numbers

print("Merge Lists:", merge_list)


# Find second largest element.
unique_numbers = list(set(merge_list))
unique_numbers.sort()

print("Second Largest:", unique_numbers[-2])