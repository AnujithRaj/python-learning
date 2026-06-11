# Convert integer to string.
int1 = 20
str1 = str(int1)
print(str1, type(str1))


# Convert string "100" to integer.
str2 = "100"
int2 = int(str2)
print(int2, type(int2))


# Convert float to integer.
float1 = 10.12
int3 = int(float1)
print(int3, type(int3))


# Convert integer to boolean.
int4 = 2
bool1 = bool(int4)
print(bool1, type(bool1))


# Convert empty string to boolean.
emp_str = ""
bool2 = bool(emp_str)
print(bool2, type(bool2))


# Convert non-empty string to boolean.
str3 = "Hello"
bool3 = bool(str3)
print(bool3, type(bool3))


# Convert list to tuple.
list1 = [1, 4, 6, 2, 5]
tuple1 = tuple(list1)
print(tuple1, type(tuple1))


# Convert tuple to list.
tuple2 = (5, 9, 4, 7, 1)
list2 = list(tuple2)
print(list2, type(list2))


# Convert set to list.
set1 = {4, 6, 9, 8, 2, 5}
list3 = list(set1)
print(list3, type(list3))


# Convert string "45.67" to float.
str4 = "45.67"
float2 = float(str4)
print(float2, type(float2))