# Take two numbers and print:
number1 = int(input("Enter First Number: "))
number2 = int(input("Enter Second Number: "))

print(f"First Number: {number1}, Second Number: {number2}")


# Print multiplication table of a given number using formatted output.
number = int(input("Enter Number: "))

for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")


# Take name and score and print:
name = input("Enter Your Name: ")
score = int(input("Enter Your Score: "))

print(f"Name: {name}, Score: {score}")


# Take item name, quantity, and price and print a formatted invoice.
item_name = input("Enter Item Name: ")
quantity = int(input("Enter Quantity: "))
price = float(input("Enter Price per Item: "))

total = quantity * price

print("\n----- Invoice -----")
print(f"Item Name : {item_name}")
print(f"Quantity  : {quantity}")
print(f"Price     : ₹{price}")
print(f"Total     : ₹{total}")
print("-------------------")



# Take width and height and print area with proper labels.
width = int(input("Enter Width: "))
height = int(input("Enter Height: "))

area = width * height

print(f"Width: {width}")
print(f"Height: {height}")
print(f"Area: {area}")