# Create a set of numbers.
set1 = {20, 11, 40, 68, 30, 86}

print("Set:", set1)


# Add a new element.
set1.add(72)

print("After New elements:", set1)

# Remove an element.
set1.remove(86)

print("After Remove:", set1)


# Find union of two sets.
set2 = {32, 40, 57, 72, 84, 18, 43}

print("Union:", set1.union(set2))


# Find intersection of two sets.
print("Intersection:", set1.intersection(set2))


# Find difference of two sets.
print("Difference:", set1.difference(set2))


# Check subset.
print("Is Subset:", {40, 72}.issubset(set1))


# Check superset.
print("Is Superset:", set1.issuperset({40, 72}))


# Remove duplicates from a list using set.
numbers = [1, 2, 2, 3, 4, 4, 5]

unique_numbers = list(set(numbers))

print("Unique Number:",unique_numbers)


# Find common elements between two lists using sets.
list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 60, 70]

common = set(list1).intersection(set(list2))

print("Common Elements:", common)