# Store name, age, course, and marks. Print all
name = "Siddharth"
age = 24
course = "Data Science"
marks = 86

print(f"Student Name: {name}, Age: {age}, Course: {course}, Marks: {marks}")


# Store product name, price, and quantity. Calculate total cost.
product_name = "Chair"
price = 1000
quantity = 2

total_cost = price * quantity

print("Total Cost of Product:", total_cost)


# Store employee details and print them neatly.
emp_name = "Rohan"
age = 35
salary = 60000

print(f"Employee Name: {emp_name}, Age: {age}, Salary: {salary}")


# Store values of a, b, c. Calculate: a + b + c and a * b + c.
a = 20
b = 11
c = 30

sum_result = a + b + c
exp_result = a * b + c

print(f"Sum of a + b + c: {sum_result}")
print(f"Expression of a * b + c: {exp_result}")


# Calculate average of three numbers.
num1 = int(input("Enter First Numbers: "))
num2 = int(input("Enter Second Numbers: "))
num3 = int(input("Enter Third Numbers: "))

avg = (num1 + num2 + num3) / 3

print("Average of Numbers:", avg)

# Calculate Maximum among three numbers.
maximum = max(num1, num2, num3)

print("Maximum Number is:", maximum)

# Calculate minimum among three numbers.
minimum = min(num1, num2, num3)

print("Minimum Number is:", minimum)

# Calculate profit/losss using cost price and selling price.
cost_price = 500
sell_price = 620

if sell_price > cost_price:
    print("Profit:", sell_price - cost_price)
elif cost_price > sell_price:
    print("Loss:", cost_price - sell_price)
else:
    print("NO Profit NO Loss")


# Calculate speed using distane and time.
distance = int(input("Enter Distance in Meters: "))
time = int(input("Enter Time in Minutes: "))

speed = distance / time

print("Speed: ", speed, "m/min")


# Calculate BMI using weight and height.
weight = float(input("Enter Weight (kg): "))
height = float(input("Enter Height (m): "))

bmi = weight / (height * height)

print("BMI:", round(bmi, 20))
