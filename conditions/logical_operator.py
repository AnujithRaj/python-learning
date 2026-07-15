# Check whether a number lies between 10 and 50.
number = int(input("Enter a Number: "))

if 10 <= number <= 50:
    print("This Number Lies between 10-50")
else:
    print("Number does not lie between 10 and 50.")


# Check whether a person is eligible for a loan: Age ≥ 21, Salary ≥ 25,000
age = int(input("Enter Your Age: "))
salary = int(input("Enter Your Salary: "))

if age >= 21 and salary >= 25000:
    print("You are eligible for Loan")
else:
    print("Not Eligible")


# Check whether a user can log in: Correct username, Correct password
username = input("Enter Your Username: ")
password = input("Enter Your Password: ")

confirm_username = input("Enter Your Confirm Username: ")
confirm_password = input("Enter Your Confirm Password: ")

if username == confirm_username and password == confirm_password:
    print("Login Successfully")
elif username != confirm_username and password == confirm_password:
    print("Invalid Username")
elif username == confirm_username and password != confirm_password:
    print("Invalid Password")
else:
    print("Invalid Username and Password")


# Check whether a number is divisible by both 2 and 3.
num = int(input("Enter a Number: "))

if num % 2 == 0 and num % 3 == 0:
    print("This Number Divisible by both 2 and 3")
else:
    print("Number is not divisible by both 2 and 3.")

    
# Check whether a person qualifies for a gym membership discount: Student OR Senior Citizen
age = int(input("Enter Your age: "))
membership = 1000
discount = 0

if age <= 24:
    print("Student: Qualifies for membership discount")
    discount = 0.20
elif age >= 50:
    print("Senior Citizen: Qualifies for membership discount")
    discount = 0.40
else:
    print("Not Eligible for Discount")

final_price = membership - (membership * discount)

print("Final Membership Price:", final_price)

# Check whether a student gets distinction: Marks ≥ 75 AND attendance ≥ 80%
marks = int(input("Enter Your Marks: "))
attendance = int(input("Enter Your Attendance %: "))

if marks >= 75 and attendance >= 80:
    print("Eligible for Distinction")
else:
    print("Not Eligible")
# Check whether a year is a leap year (complete logic).
year = int(input("Enter a Year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not Leap Year")


# Check whether a triangle is valid using three sides.
first_side = int(input("Enter First Side of Triangle: "))
second_side = int(input("Enter Second Side of Triangle: "))
third_side = int(input("Enter Third Side of Triangle: "))

if first_side + second_side > third_side and second_side + third_side > first_side and third_side + first_side > second_side:
    print("Valid Triangle")
else:
    print("Invalid Triangle")


# Check whether three angles form a valid triangle.
x = int(input("Enter First angles of Triangle: "))
y = int(input("Enter Second angles of Triangle: "))
z = int(input("Enter Third angles of Triangle: "))

if x > 0 and y > 0 and z > 0 and x + y + z == 180:
    print("Valid Triangle")
else:
    print("Invalid Triangle")


# Check whether a person can enter a club: Age ≥ 21, Membership available
age = int(input("Enter Your Age: "))
membership = input("Membership available Yes/No: ").lower()

if not (0 <= age <= 100):
    print("Invalid Age")
elif age >= 21 and membership == "yes":
    print("Eligible for Club Membership")
else:
    print("Not Eligible for Club Membership")