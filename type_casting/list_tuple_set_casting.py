# Convert a list into a tuple.
list1 = input("Enter list elements: ").split()

tup1 = tuple(list1)
print("Tuple:", tup1)
print(type(tup1))


# Convert a tuple into a list.
lis1 = list(tup1)

print("List:", lis1)
print(type(lis1))


# Convert a list with duplicate values into a set.
lis2 = input("Enter List elements with duplicate values: ").split()

set1 = set(lis2)

print("Set:", set1)
print(type(set1))


# Convert a set into a list.
list_from_set = list(set1)

print("List from Set:", list_from_set)
print(type(list_from_set))


# Convert a string "python" into a list.
str1 = "Python"
list_from_string = list(str1)

print("List from String:", list_from_string)
print(type(list_from_string))


# Convert a string "python" into a tuple.
tuple_from_string = tuple(str1)

print("Tuple from String:", tuple_from_string)
print(type(tuple_from_string))


# Convert a string "python" into a set.
set_from_string = set(str1)

print("Set from String:", set_from_string)
print(type(set_from_string))


# Convert a tuple into a set.
set_from_tuple = set(tup1)

print("Set from Tuple:", set_from_tuple)
print(type(set_from_tuple))


# Convert a set into a tuple.
tuple_from_set = tuple(set1)

print("Tupe from Set:", tuple_from_set)
print(type(tuple_from_set))


# Convert a list into a string (using join()).
list3 = ["I", "love", "Python"]

string_from_list = " ".join(list3)

print("String from List:", string_from_list)
print(type(string_from_list))