import math
# Take radius of a circle and print its area.
radius = float(input("Enter radius of Circle: "))

area = math.pi * radius ** 2
print("Area of Circle:", area)


# Take length and breadth of a rectangle and print area.
rec_length = float(input("Enter Length of Rectangle: ")) 
rec_breadth = float(input("Enter Breadth of Rectangle: "))

rectangle_area = rec_length * rec_breadth
print("Area of Rectangle:", rectangle_area)


# Take length and breadth and print perimeter.
rec_perimeter = 2 * (rec_length + rec_breadth)
print("Perimeter of rectangle:", rec_perimeter)


# Take principal, rate, and time and calculate simple interest.
principal = float(input("Enter Principal: "))
rate = float(input("Enter Rate %: "))
time = float(input("Enter Time: "))

si = (principal * rate * time) / 100
print("Simple Interest:", si)


# Take marks of 5 subjects and calculate total marks.
hindi = int(input("Enter Hindi Marks: "))
english = int(input("Enter English Marks: "))
maths = int(input("Enter Maths Marks: "))
science = int(input("Enter Science Marks: "))
sanskrit = int(input("Enter Sanskrit Marks: "))

total_marks = hindi + english + maths + science + sanskrit
print("Total Marks:", total_marks)


# Take marks of 5 subjects and calculate percentage.
percentage = total_marks / 5

print("Percentage:", percentage, "%")


# Take temperature in Celsius and convert to Fahrenheit.
celsius = float(input("Enter Temperature in Celsius: "))

fahrenheit = (celsius * 9/5 ) + 32
print("Temperature in Fahrenheit:", fahrenheit)


# Take distance in kilometers and convert to meters.
distance = float(input("Enter Distance in KMs: "))

meters = distance * 1000
print("Distance in Meters:", meters)


# Take minutes and convert to hours.
minutes = int(input("Enter Minutes: "))

hours = minutes / 60
print("Hours:", round(hours, 2))


# Take days and convert to years.
days = int(input("Enter Days: "))

years = days / 365
print("Years:", round(years, 2))
