# Check whether a string is a palindrome.
string = input("Enter a String: ")

if string == string[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")


# Count the frequency of each character.
text = input("Enter a Text: ")
frequency = {}

for char in text:
    frequency[char] = frequency.get(char, 0) +1

print("Frequency:",frequency)


# Find the first non-repeating character.
for char in text:
    if text.count(char) == 1:
        print("First No-Repeating Character:", char)
        break
else:
    print("No Non-Repeating Character")


# Find the first repeating character.
seen = set()

for char in text:
    if char in seen:
        print("First Repeating Character:", char)
        break
    seen.add(char)
else:
    print("No Repeating Character")


# Remove all vowels from a string.
vowels = "aeiouAEIOU"
result = ""

for char in text:
    if char not in vowels:
        result += char
print("Without Vowels:", result)


# Remove all spaces from a string.
no_space = text.replace(" ", "")
print("Without Spaces:", no_space)


# Reverse each word in a sentence.
sentence = input("Enter Sentence: ")

words = sentence.split()
reverse_each = " ".join(word[::-1] for word in words)
print("Reverse Each Words In Sentence:", reverse_each)


# Reverse the order of words in a sentence.
reverse_order = " ".join(words[::-1])
print("Reverse Words Order:", reverse_order)


# Find the longest word in a sentence.
longest = max(words, key=len)
print("Longest Word:", longest)


# Find the shortest word in a sentence.
shortest = min(words, key=len)
print("Shortest Word:", shortest)