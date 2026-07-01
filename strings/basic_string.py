# Create a string containing your name and print it.
name = input("Enter Name: ")

print("Name:", name)


# Find the length of a string.
print("Length:", len(name))


# Access the first and last character of a string.
print("First Character:", name[0])
print("Last Character:", name[-1])


# Print each character of a string using indexing.
print("Character in String:")
for i in range(len(name)):
    print(name[i])


# Concatenate two strings.
surname = input("Enter Surname: ")

full_name = name + " " + surname
print("Full Name:", full_name)


# Repeat a string 5 times.
print("Repeated 5 Times:", name * 5)


# Check whether a character exists in a string.
char = input("Enter a character to search: ")

if char in name:
    print(char, "Exists in the string")
else:
    print(char, "Does not exist in the string")


# Take a string as input and print it in uppercase.
print("Uppercase:", name.upper())


# Take a string as input and print it in lowercase.
print("Lowercase:", name.lower())


# Reverse a string using slicing.
print("Reversed String:", name[::-1])