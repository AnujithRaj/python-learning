# Convert "250" into an integer and multiply it by 5.
str1 = "250"

int1 = int(str1)

print(int1 * 5)


# Convert "12.5" into a float and add 10.
str2 = "12.5"

float1 =  float(str2)

print(float1 + 10)


# Convert 1234 into a string and find its length.
int_value = 1234

str_value = str(int_value)

print(str_value, len(str_value))


# Convert 5678 into a string and print each digit separately.
int_value1 = 5678

str_value1 = str(int_value1)

for digit in str_value1:
    print(digit)


# Convert "999" into an integer and subtract 100.
str_value2 = "999"
int_value2 = int(str_value2)

print(int_value2 - 100)


# Convert "45.67" into a float and round it to 1 decimal place.
float_str = "45.67"
float_val = float(float_str)

print(round(float_val, 1))


# Convert the string "0" into a boolean and observe the result.
zero_str = "0"

zero_bool = bool(zero_str)

print(zero_bool, type(zero_bool))


# Convert an empty string "" into a boolean.
emp_str = ""

bool_value = bool(emp_str)

print(bool_value, type(bool_value))


# Convert the string "False" into a boolean and check the output.
str_val = "False"

bool_val = bool(str_val)

print(bool_val, type(bool_val))


# Convert the string "True" into a boolean and check the output.
str_val1 = "True"

bool_val1 = bool(str_val1)

print(bool_val1, type(bool_val1))