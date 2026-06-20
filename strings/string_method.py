# Count the occurrence of a character in a string.
word = input("Enter Word: ")
char = input("Enter Character to Count: ")

print(f"'{char}' occurs {word.count(char)} times in '{word}'")


# Find the index of a substring.
word1 = input("Enter String: ")
sub = input("Enter Substring: ")

index = word1.find(sub)

print("Index:", index)


# Replace once word with another in a string.
text = input("Enter String: ")
old_word = input("Word to Replace: ")
new_word = input("New word: ")

result = text.replace(old_word, new_word)

print("Updating String:", result)


# Remove leading and trailing spaces.
txt = input("Enter String: ")

print("After Remove Space:", txt.strip())


# Split a sentence into words.
sentence = input("Enter Sentence: ")

words = sentence.split()

print("Words:", words)


# Join a list of words into a sentence.
words1 = input("Enter words separated by Spaces: ").split()

sentence = " ".join(words1)

print("Joined Sentence:", sentence)


# Check whether a string starts with a specific word.
str1 = input("Enter String: ")
word = input("Enter Starting Words: ")

print(str1.startswith(word))


# Check whether a string ends with a specific word.
text1 = input("Enter String: ")
word1 = input("Enter Ending Word: ")

print(text1.endswith(word1))


# Convert a string to title case.
title_word = input("Enter Title: ")

print("Title Case:", title_word.title())


# Swap uppercase letters to lowercase and vice versa.
text2 = input("Enter Text: ")

print("Swapped Case:", text2.swapcase())