# Electricity bill calculator.
units = float(input("Enter Electricity Units: "))
per_units_rate = 9

electric_bill = units * per_units_rate

print(f"Electricity Bill: ₹{electric_bill:.2f}")


# Income tax calculator.
income = float(input("Enter Your annual income: "))

if income <= 250000:
    tax = 0
elif income <= 500000:
    tax = income * 0.05
elif income <= 1000000:
    tax = income * 0.20
else:
    tax = income * 0.30

print(f"Income Tax: ₹{tax:.2f}")

# BMI category checker.
weight = float(input("Enter Your body weight (Kg): "))
height = float(input("Enter height (m): "))

bmi = weight / (height ** 2)

print(f"BMI: {bmi:.2f}")

if bmi < 18.5:
    print("Category: Under weight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")


# Blood pressure category checker.
systolic = int(input("Enter Systolic BP: "))
diastolic = int(input("Enter Diastolic BP: "))

if systolic < 120 and diastolic < 80:
    print("Normal")
elif systolic < 130 and diastolic < 80:
    print("Elevated")
elif systolic < 140 or diastolic < 90:
    print("High Blood Pressure Stage 1")
else:
    print("High Blood Pressure Stage 2")


# Train ticket fare calculator.
distance = float(input("Enter distance in Km: "))
rate = 2.5

fare = distance * rate

print(f"Train Fare: ₹{fare:.2f}")


# Mobile recharge plan recommender.
budget = int(input("Enter Your  Recharge Budget: "))

if budget >= 500:
    print("Recommended Plan: Unlimited Calls + 3GB/day + OTT")
elif budget >= 300:
    print("Recommended Plan: Unlimited Calls + 2GB/day")
elif budget >= 200:
    print("Recommended Plan: Unlimited Calls + 1GB/day")
else:
    print("Recommended Plan: Talktime Pack")


# Restaurant bill with discount.
bill = float(input("Enter Restaurant Bill: "))

if bill >= 2000:
    discount = 0.20
elif bill >= 1000:
    discount = 0.10
else:
    discount = 0

total_bill = bill - (bill * discount)

print("Discount:", discount * 100, "%")
print(f"Total Restaurant Bill: ₹{total_bill:.2f}")


# Parking fee calculator.
hours = int(input("Enter parking hours: "))
parking_rate = 30

fee = hours * parking_rate

print(f"Total Parking Fee: ₹{fee:.2f}")


# Movie ticket booking system.
tickets = int(input("Enter Number of Tickets: "))
ticket_price = 250

total_price = tickets * ticket_price

print(f"Total Amount: ₹{total_price:.2f}")


# E-commerce discount calculator.
amount = float(input("Enter purchase amount: "))

if amount >= 5000:
    discount = 0.25
elif amount >= 3000:
    discount = 0.15
elif amount >= 1000:
    discount = 0.10
else:
    discount = 0

final_price = amount - (amount * discount)

print("Discount:", discount * 100, "%")
print(f"Final Amount: ₹{final_price:.2f}")