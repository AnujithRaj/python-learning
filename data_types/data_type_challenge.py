# Create a phonebook using dictionary.
phonebooks = {
    "Aman": 9848755843,
    "Rohit": 7483973929,
    "mahi": 9383938491
}

print(phonebooks)


# Build a simple student record system.
students ={
    "Rahul": {"Age": 20, "Marks": 85},
    "Lokesh": {"Age": 21, "Marks": 92},
    "Ankush": {"Age": 19, "Marks": 86}
}

for name, details in students.items():
    print(f"Name: {name}")
    print(f"Age: {details['Age']}")
    print(f"Marks: {details['Marks']}")
    print("-" * 20)


# Count word frequency in a paragraph.
paragraph = input("Enter Your Paragraph: ")

words = paragraph.lower().split()
freq = {}

for word in words:
    freq[word] = freq.get(word, 0) +1

print("Words Frequency:", freq)


# Find the first non-repeating character.
text = input("Enter Text: ")

count = {}

for char in text:
    count[char] = count.get(char, 0) + 1

for char in text:
    if count[char] == 1:
        print("First Non-Repeating Character:", char)
        break
else:
    print("No non-repeating character found.")


# Find the most frequent element in a list.
lis = ["Apple", 20, "Banana", True, "Mango", 20, "Carrot", "Parrot", "Apple", "Mango", "Apple"]

frequency = {}

for item in lis:
    frequency[item] = frequency.get(item, 0) + 1

most_frequent = max(frequency, key=frequency.get)

print("Most frequent element:", most_frequent)
print("Frequency:", frequency[most_frequent])



# Group words by their length.
words = ["apple", "cat", "banana", "dog", "grape"]

groups = {}

for word in words:
    length = len(word)

    if length not in groups:
        groups[length] = []

    groups[length].append(word)

print(groups)


# Merge dictionaries and sum common keys.
dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 5, "c": 15, "d": 40}

merged = dict1.copy()

for key, value in dict2.items():
    merged[key] = merged.get(key, 0) + value

print(merged)


# Create a nested dictionary for employees.
employees = {
    101: {
        "Name": "Rahul",
        "Department": "HR",
        "Salary": 35000
    },
    102: {
        "Name": "Lokesh",
        "Department": "IT",
        "Salary": 50000
    },
    103: {
        "Name": "Ankush",
        "Department": "Sales",
        "Salary": 42000
    }
}

for emp_id, details in employees.items():
    print(emp_id, details)


# Flatten a nested list.
nested = [[1, 2], [3, 4], [5, 6], [7, 8]]

flat = []

for sublist in nested:
    for item in sublist:
        flat.append(item)

print(flat)


# Build a mini inventory management system.
inventory = {
    "Pen": 20,
    "Book": 10,
    "Pencil": 30
}

# Add a new item
inventory["Eraser"] = 15

# Update quantity
inventory["Pen"] += 5

# Remove an item
inventory.pop("Book")

# Display inventory
for item, quantity in inventory.items():
    print(f"{item}: {quantity}")
