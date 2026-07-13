# Find the second largest among three numbers.
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))

if (a > b and a < c) or (a < b and a > c):
    print("Second Largest Number:", a)
elif (b > a and b < c) or (b < a and b > c):
    print("Second Largest Number:", b)
else:
    print("Second Largest Number:", c)

# Check whether a year is a century leap year.
year = int(input("Enter Years: "))

if year % 400 == 0:
    print("Century Leap year")
else:
    print("Not a Century Leap Year")


# Determine salary after bonus and tax deduction.
salary = float(input("Enter Salary: "))

if salary <= 30000:
    bonus = salary * 0.20
elif salary <= 50000:
    bonus = salary * 0.10
else:
    bonus = salary * 0.05

gross = salary + bonus
tax = gross * 0.10
net_salary = gross - tax

print("Bonus:", bonus)
print("Tax:", tax)
print("Net Salary:", net_salary)


# Determine election eligibility and category.
age = int(input("Enter Your Age: "))

if age < 18:
    print("Not Eligible")
elif age < 60:
    print("eligible Adult Voter")
else:
    print("Elibible Senior Citizen Voter")


# Create a menu-driven calculator.
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter Choice: "))

num1 = float(input("Enter First Number: "))
num2 = float(input("Enter Second Number: "))

if choice == 1:
    print("Result:", num1 + num2)
elif choice == 2:
    print("Result:", num1 - num2)
elif choice == 3:
    print("Result:", num1 * num2)
elif choice == 4:
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Division by Zero not possible")
else:
    print("Invalid Choice")

# Check triangle validity and type.
x = int(input("Enter Side 1: "))
y = int(input("Enter Side 2: "))
z = int(input("Enter Side 3: "))

if x + y > z and x + z > y and y + z > x:
    print("Valid Triangle") 

    if x == y == z:
        print("Equilateral Triangle")
    elif x == y or y == z or x == z:
        print("Isosceles Triangle")
    else:
        print("Scalene Triangel")
else:
    print("Invalid Triangle")


# Determine student rank based on marks.
marks = float(input("Enter Marks: "))

if marks >= 90:
    print("Rank: Outstanding")
elif marks >= 75:
    print("Rank: First Class")
elif marks >= 60:
    print("Rank: Second Class")
elif marks >= 40:
    print("Rank: Pass")
else:
    print("Fail")


# Create a discount engine for an e-commerce site.
amount = float(input("Enter Purchase Amount: "))

if amount >= 10000:
    discount = 20
elif amount >= 5000:
    discount = 15
elif amount >= 2000:
    discount = 10
else:
    discount = 5

discount_amount = amount * discount / 100
final_amount = amount - discount_amount

print("Discount =", discount, "%")
print("Final Amount =", final_amount)


# Simulate a simple bank account system.
balance = 10000

print("1. Deposit")
print("2. Withdraw")
print("3. Check Balance")

choice = int(input("enter Choice: "))

if choice == 1:
    amount= float(input("Enter Deposit Amount: "))
    balance += amount
    print("Current Balance:", balance)

elif choice == 2:
    amount = float(input("Enter Withdrawal Amount: "))
    if amount <= balance:
        balance -= amount
        print("Current Balance:", balance)
    else:
        print("Insufficient Balance")
elif choice == 3:
    print("Current Balance:", balance)
else:
    print("Invalid Choice")


# Create a complete grading and report card system.
hindi = int(input("Enter Hindi Marks: "))
english = int(input("Enter English Marks: "))
maths = int(input("Enter Math Marks: "))
science = int(input("Enter Science Marks: "))
sanskrit = int(input("Enter Sanskrit Marks: "))

total_marks = hindi + english + maths + science + sanskrit
percentage = total_marks / 5

print("Total Marks:", total_marks)
print("Percentage:", percentage)

if percentage >= 90:
    grade = "A+"
elif percentage >= 80:
    grade = "A"
elif percentage >= 60:
    grade = "B"
elif percentage >= 40:
    grade = "C"
else:
    grade = "F"

print("Grade:", grade)

if percentage >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")
