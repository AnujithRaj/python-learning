# Count the number of words in a sentence.
sentence = input("Enter a Sentence: ")

word_count = len(sentence.split())

print("Number of words:", word_count)


# Find the most frequent character.
text = input("Enter a String: ")

if not text:
    print("String is empty.")
else:
    freq = {}

    for char in text:
        freq[char] = freq.get(char, 0) + 1

    most_frequent = max(freq, key=freq.get)

    print("Most frequent Character:", most_frequent)
    print("Frequency:", freq[most_frequent])


# Find the least frequent character.
    least_frequent = min(freq, key=freq.get)

    print("Least frequent Character:", least_frequent)
    print("Frequency:", freq[least_frequent])


# Remove duplicate characters from a string.
str1 = input("Enter String: ")

result = ""
for ch in str1:
    if ch not in result:
        result += ch

print("String after removing duplicates:", result)


# Check whether two strings are anagrams.
string1 = input("Enter First String: ")
string2 = input("Enter Second String: ")

if sorted(string1.replace(" ", "").lower()) == sorted(string2.replace(" ", "").lower()):
    print("The strings are Anagrams")
else:
    print("The strings are not Anagrams")

# Check whether two strings are rotations of each other.
if len(string1) == len(string2) and string2 in (string1 + string1):
    print("The string are rotations of each other")
else:
    print("the strings are not rotations")


# Find all duplicate characters in a string.
text1 = input("Enter a string: ")

freq = {}
for i in text1:
    freq[i] = freq.get(i, 0) +1

print("Duplicate Characters:")

found = False
for i in freq:
    if freq[i] > 1:
        print(i, ":", freq[i])
        found = True

if not found:
    print("No duplicate Characters found")


# Find the second most frequent character.
text = input("Enter a String: ")

freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

if len(freq) < 2:
    print("Second most frequent character does not exist.")
else:
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)

    print("Second Most Frequent Character:", sorted_freq[1][0])
    print("Frequency:", sorted_freq[1][1])


# Print characters appearing only once.
text = input("Enter a String: ")

freq = {}

for ch in text:
    freq[ch] = freq.get(ch, 0) + 1

print("Characters appearing only once: ")

found = False
for ch in freq:
    if freq[ch] == 1:
        print(ch)
        found = True

if not found:
    print("No unique characters found")


# Compress a string (aaabbc → a3b2c1).
text = input("Enter a String: ")

if text == "":
    print("String is empty")
else:
    result = ""
    count = 1

    for i in range(1, len(text)):
        if text[i] == text[i - 1]:
            count += 1
        else:
            result += text[i - 1] + str(count)
            count = 1

    result += text[-1] + str(count)

    print("Compressed String:", result)