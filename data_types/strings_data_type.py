# Store your name and print it.
name = str(input("Enter Your Name: "))

print("Name:", name)


# Find the length of a string.
print("Length of String:", len(name))


# Convert a string to uppercase.
print("Name:",name.upper())


# Convert a string to lowercase.
print("Name:", name.lower())


# Print the first character of a string.
print("Frist Character:", name[0])


# Print the last character.
print("Last Character:", name[-1])


# Reverse a string.
print("Reverse String:", name[::-1])


# Count occurrences of a character.
char = input("Enter your Character: ")

print("Character Count:", name.count(char))


# Replace a word in a sentence.
sentence = input("Enter a sentence: ")

old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

print("Updated Sentence:", sentence.replace(old_word, new_word))


# Check whether a word exists in a string.
word = input("Enter word to search: ")

if word in sentence:
    print("Word Found")
else:
    print("Word Not Found")