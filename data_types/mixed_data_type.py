# Count vowels in a string.
string = input("Enter a String: ").lower()

vowels = "aeiou"
count = 0
for char in string:
    if char in vowels:
        count += 1

print("Count of Vowels:", count)

# Count frequency of each character.
freq = {}

for char in string:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print("Frequency:", freq)


# Count frequency of each word.
sentence = input("Enter a Sentence: ")
words = sentence.split()
freq = {}

for word in words:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
print("Frequency of Word:", freq)


# Find duplicate elements in a list.
lst = list(map(int, input("Enter List Elements: ").split()))

duplicates = []

for item in lst:
    if lst.count(item) > 1 and item not in duplicates:
        duplicates.append(item)

print("Duplicate Elements:", duplicates)


# Find unique elements in a list.
list1 = list(map(int, input("Enter List elements with duplicate: ").split()))
unique = []

for item in list1:
    if item not in unique:
        unique.append(item)

print("Unique Elements:", unique)


# Store student marks in a dictionary and calculate average.
marks = {
    "math": 85,
    "science": 90,
    "english": 86
}

total = sum(marks.values())
average = total / len(marks)

print("Average marks:", average)


# Find common elements among three lists.
lis1 = [1,2,3,4,5]
lis2 = [2,3,4,5,6]
lis3 = [3,4,5,6,7]

common = []
for item in lis1:
    if item in lis2 and item in lis3:
        common.append(item)
print("Common Elements:", common)


# Convert list of strings into integers.
string_list = ["10", "20", "30", "40", "50"]

int_list = []
for item in string_list:
    int_list.append(int(item))

print("Integers List:", int_list)


# Separate even and odd numbers from a list.
numbers = list(map(int,input("Enter a List Numbers: ").split()))

even = []
odd = []

for num in numbers:
    if num % 2 == 0:
        even.append(num)
    else:
        odd.append(num)

print("Even:", even)
print("Odd:", odd)


# Create a dictionary where keys are numbers and values are squares.
n = int(input("Enter a number: "))
square_dict = {}

for i in range(1, n + 1):
    square_dict[i] = i ** 2

print("Keys Square Values:", square_dict)