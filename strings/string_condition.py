str1 = input("Enter String:")

# Check whether a string is empty.
if len(str1) > 0:
    print("String length:", len(str1))
else:
    print("Empty")

# Check whether a string contains only alphabets.
if str1.isalpha():
    print("Only Alphabets")
else:
    print("Does not contain only Alphabets")

# Check whether a string contains only digits.
if str1.isdigit():
    print("Only Digits")
else:
    print("Does not contain only digits")


# Check whether a string contains only alphanumeric characters.
if str1.isalnum():
    print("Onlu Alphanumeric Characters")
else:
    print("Does Not Alphanumeric")


# Count uppercase and lowercase letters separately.
upper = 0
lower = 0

for ch in str1:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1


# Check whether a string contains spaces.
if " " in str1:
    print("String Contains Spaces")
else:
    print("String does not contain spaces")


# Find the number of vowels in a string.
vowels = 0
for ch in str1.lower():
    if ch in "aeiou":
        vowels += 1
print("Number of vowels:", vowels)


# Find the number of consonants in a string.
consonants = 0
for ch in str1.lower():
    if ch.isalpha() and ch not in "aeiou":
        consonants += 1

print("Number of consonants:", consonants)


# Find the number of digits in a string.
digits = 0
for ch in str1:
    if ch.isdigit():
        digits += 1
print("Number of digits:", digits)


# Find the number of special characters in a string.
special = 0
for ch in str1:
    if not ch.isalnum() and not ch.isspace():
        special += 1
print("Number of special Characters:", special)