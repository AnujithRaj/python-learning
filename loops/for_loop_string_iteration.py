# Print each character of a string separately.
string = input("Enter a String: ")

for ch in string:
    print(ch)

# Count total characters in a string using a loop.
string = input("Enter a String: ")

count = 0
for ch in string:
    count += 1

print("Total Characters:", count)

# Count vowels in a string.
string = input("Enter a String: ").lower()

count = 0
for ch in string:
    if ch in "aeiou":
        count += 1

print("Total Vowels:", count)


# Count consonants in a string.
string = input("Enter a String: ").lower()

count = 0
for ch in string:
    if ch.isalpha() and ch not in "aeiou":
        count += 1

print("Total Consonants:", count)


# Count uppeercase and lowercase letters.
words = input("Enter a Words: ")

upper = 0
lower = 0
for word in words:
    if word.isupper():
        upper += 1

    elif word.islower():
        lower += 1
    else:   
        print("Invalid Letters")

print("Uppercase Letters:", upper)
print("lowercase Letters:", lower)


# Print characters at even indexes.
string = input("Enter a String: ")

for i in range(len(string)):
    if i % 2 == 0:
        print(string[i])


# Print characters at odd indexes.
string = input("Enter a String: ")

for i in range(len(string)):
    if i % 2 != 0:
        print(string[i])


# Reverse a string using a loop.
string = input("Enter a string: ")

reverse = ""
for ch in string:
    reverse = ch + reverse

print("Reverse String:", reverse)


# Check whether a string is palindrome.
string = input("Enter a String: ")

reverse = ""
for ch in string:
    reverse = ch + reverse

if string == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")


# Count occurrences of a specific characters.
string = input("Enter a String: ").lower()
target = input("Enter Character to Count: ")

count = 0
for ch in string:
    if ch == target:
        count += 1

print("Character Occurrences:", count)