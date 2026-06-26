# Create a dictionary containing student details.
student = {
    'name': 'Siddharth',
    'age': 22,
    'city': 'Rajgir'
}
print(student['name'])
print(student['city'])


# Access a value using key.
print(student.values())


# Add a new key-value pair.
student['college'] = 'Manipal University'


# Update a value.
student['age'] = 21


# Delete a key.
del student['age']


# Print all keys.
print(student.keys())


# Print all values.
print(student.values())


# Print all key-value pairs.
print(student.items())


# Check if a key exists.
if 'city' in student:
    print("Key Exists")
else:
    print("Key does not exist")


# Count total keys.
print(len(student))


# Merge two dictionaries.
dict1 = {'a': 10, 'b': 20}
dict2 = {'c': 30, 'd': 40}

merged = dict1 | dict2
print("Merged Dictionary:", merged)


# Find key having maximum value.
marks = {'Math': 90, 'Science': 85, 'English': 95, 'Hindi': 86}

max_key = max(marks, key = marks.get)
print("Key with Maximum Value:", max_key)


# Find key having minimum value.
min_key = min(marks, key = marks.get)
print("Key with Minimum value:", min_key)


# Create a dictionary from two lists.
keys = ['name', 'age', 'city']
values = ['Rahul', 21, 'Patna']

new_dict = dict(zip(keys, values))
print("Dictionary from Lists:", new_dict)


# Sort dictionary by values.
sorted_dict = dict(sorted(marks.items(), key = lambda item: item[1]))
print("Sorted Dictionary by Values:", sorted_dict)
