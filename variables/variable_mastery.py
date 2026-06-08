# Student Information System

student_name = input("Enter your name: ")
marks = int(input("Enter your marks: "))

total_marks = 500
percentage = (marks / total_marks) * 100

print("\n----- STUDENT REPORT -----")
print("Name:", student_name)
print("Marks:", marks)
print("Total Marks:", total_marks)
print("Percentage:", round(percentage, 2), "%")


# Bank Interest Calculator
principal = float(input("Enter Amount: "))
rate = float(input("Enter Rate % : "))
time = float(input("Enter Time: "))

interest = (principal * rate * time) / 100

print("\n----- INTEREST REPORT -----")
print("Principal:", principal)
print("Rate:", rate, "%")
print("Time:", time, "years")
print("Interest:", interest)


# Restaurant Bill Calculator
bill = float(input("Enter Bill Amount: "))
gst = 18

gst_amount = bill * gst / 100
final_bill = bill + gst_amount

print("----- BILL REPORT -----")

print("Food Bill:", bill)
print("GST:", round(gst_amount, 2))
print("Final Bill:", round(final_bill, 2))


# Fuel Consumption Calculator
distance = float(input("Enter Distance Travel: "))
fuel = float(input("Enter Fuel used: "))

mileage = distance / fuel

print("----- FUEL REPORT -----")

print("Distance:", distance)
print("Fuel Used:", fuel)
print("Mileage:", mileage)


# EMI Calculator
loan_amount = float(input("Enter Loan Amount: "))
months = int(input("Enter Number of Months: "))

emi = loan_amount / months

print("\n----- EMI REPORT -----")
print("Loan Amount:", loan_amount)
print("Duration:", months, "months")
print("Monthly EMI:", round(emi, 2))

# Profit & Loss Calculator
cost = int(input("Enter Cost Price: "))
sell = int(input("Enter Selling price: "))

if cost < sell:
    print("Profit:", sell - cost)
elif sell < cost:
    print("Loss:", cost - sell)
else:
    print("No profit no loss")

# Marks Percentage System
student_marks = int(input("Enter Student Marks: "))
total_marks = int(input("Enter Total Marks: "))

percentage = (student_marks / total_marks) * 100

print("Percentage:", percentage)

# Temperature Converter
temp = float(input("Enter Temperature in Celsius: "))

fahrenheit = (temp * 9 / 5) + 32

print("Temperature in Fahrenheit:", fahrenheit)


# Currency Converter
inr = float(input("Enter Amount in INR: "))

usd_rate = 83  # Example exchange rate

usd = inr / usd_rate

print("Amount in USD:", round(usd, 2))

# Personal Expense Tracker
food = float(input("Enter Food Expense: "))
travel = float(input("Enter Travel Expense: "))
shopping = float(input("Enter Shopping Expense: "))

total_expense = food + travel + shopping

print("\n----- EXPENSE REPORT -----")
print("Food:", food)
print("Travel:", travel)
print("Shopping:", shopping)
print("Total Expense:", total_expense)