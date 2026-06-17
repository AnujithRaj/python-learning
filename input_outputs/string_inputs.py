# Take first name and last name separately and print full name.
f_name = str(input("Enter Your First Name: "))
l_name = str(input("Enter Your Last Name: "))

full_name = f_name + " " + l_name
print("Full Name:", full_name)


# Take a sentence and print it.
sentence = input("Enter a Sentence: ")

print("Sentence: ", sentence)


# Take a word and print its length.
words = input("Enter Words: ")

print("Word Length:", len(words))


# Take a word and print it in uppercase.
print("Uppercase: ", words.upper())


# Take a word and print it in lowercase.
print("Lowercase:", words.lower())


# Take a word and print the first character.
print("First Character:", words[0])


# Take a word and print the last character.
print("Last Character:", words[-1])