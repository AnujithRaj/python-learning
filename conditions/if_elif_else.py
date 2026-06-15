# Find the largest among three numbers.
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))
num3 = int(input("Enter Third Number: "))

if num2 <= num1 >= num3:
    print("Largest Number:", num1)
elif num1 <= num2 >= num3:
    print("Largest Number:", num2)
else:
    print("Largest Number: ", num3)


# Grade a student: 90–100 → A, 80–89 → B, 70–79 → C, Below 70 → Fail
marks = int(input("Enter Marks: "))

if marks < 0 or marks > 100:
    print("Invalid Marks")
elif marks >= 90:
    print("A Grade")
elif marks >= 80:
    print("B Grade")
elif marks >= 70:
    print("C Grade")
else:
    print("Fail")


# Determine traffic signal action: Red → Stop, Yellow → Wait, Green → Go
signal = input("Enter Signal Light: ").lower()

if signal == "red":
    print("Stop")
elif signal == "yellow":
    print("Wait")
elif signal == "green":
    print("Go")
else:
    print("Invalid Signal")


# Categorize age: Child, Teenager, Adult, Senior Citizen
age = int(input("Enter Age: "))

if 0 <= age <= 12:
    print("Child")
elif 13 <= age <= 17:
    print("Teenager")
elif 18 <= age <= 59:
    print("Adult")
elif age >= 60:
    print("Senior Citizen")
else:
    print("Invalid Age")
    

# Create a simple calculator using operators (+, -, *, /).
fnum = float(input("Enter First Number: "))
snum = float(input("Enter Second Number: "))
operator = input("Enter Operator (+, -, *, /): ")

if operator == "+":
    print("Result:", fnum + snum)
elif operator == "-":
    print("Result:", fnum - snum)
elif operator == "*":
    print("Result:", fnum * snum)
elif operator == "/":
    if snum != 0:
        print("Result:", fnum / snum)
    else:
        print("Division by zero is not allowed")
else:
    print("Invalid Operator")


# Check whether a number is: Positive, Negative, Zero
number = int(input("Enter Number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# Assign employee bonus based on years of service.
years = int(input("Enter Years of Service: "))
salary = float(input("Enter Salary: "))

if years >= 10:
    bonus = salary * 0.20
elif years >= 5:
    bonus = salary * 0.10
else:
    bonus = salary * 0.05

print("Bonus Amount:", bonus)


# Determine season based on month number.
month = int(input("Enter Month Number (1-12): "))

if month in [12, 1, 2]:
    print("Winter")
elif month in [3, 4, 5]:
    print("Spring")
elif month in [6, 7, 8]:
    print("Summer")
elif month in [9, 10, 11]:
    print("Autumn")
else:
    print("Invalid Month")


# Determine weekday/weekend based on day name.
day = input("Enter Day Name: ").lower()

if day in ["saturday", "sunday"]:
    print("Weekend")
elif day in ["monday", "tuesday", "wednesday", "thursday", "friday"]:
    print("Weekday")
else:
    print("Invalid Day")

# Find the greatest among four numbers.
number1 = int(input("Enter First Number: "))
number2 = int(input("Enter Second Number: "))
number3 = int(input("Enter Third Number: "))
number4 = int(input("Enter Fourth Number: "))

if number1 >= number2 and number1 >= number3 and number1 >= number4:
    print("Greatest Number:", number1)
elif number2 >= number1 and number2 >= number3 and number2 >= number4:
    print("Greatest Number:", number2)
elif number3 >= number1 and number3 >= number2 and number3 >= number4:
    print("Greatest Number:", number3)
else:
    print("Greatest Number:", number4)