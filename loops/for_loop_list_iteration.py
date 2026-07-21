# Print all elements of a list.
list1 = list(map(int, input("Enter List elements separated by space: ").split()))

for i in list1:
    print(i)


# Find sum of all elements.
list2 = list(map(int, input("Enter List elements: ").split()))

total = 0
for i in list2:
    total += i

print("Sum:", total)

# Find largest elements.
list3 = list(map(int, input("Enter List elements: ").split()))

largest = list3[0]

for i in list3:
    if i > largest:
        largest = i

print("Largest Elements:", largest)


# Find smallest element.
list4 = list(map(int, input("Enter List elements: ").split()))

smallest = list4[0]
for i in list4:
    if i < smallest:
        smallest = i

print("Smallest Element:", smallest)


# Count even numbers in a list.
list5 = list(map(int, input("Enter List elements: ").split()))

even = 0
for i in list5:
    if i % 2 == 0:
        even += 1

print("Even Occurs:", even)


# Count odd numbers in a list.
list6 = list(map(int, input("Enter List elements: ").split()))

odd = 0
for i in list6:
    if i %2 != 0:
        odd += 1

print("Odd Occurs:", odd)


# Find second largest number.
list7 = list(map(int, input("Enter List Elements: ").split()))

largest = second = float('-inf')
for i in list7:
    if i > largest:
        second = largest
        largest = i
    elif i > second and i != largest:
        second = i

print("Second Largest:", second)


# Print elements in reverse order.
list8 = list(map(int, input("Enter list elements: ").split()))

for i in range(len(list8) -1, -1, -1):
    print(list8[i], end=" ")


# Create a new list containing squares of all elements.
list9 = list(map(int, input("Enter List elements: ").split()))

square = []
for i in list9:
    square.append(i * i)

print("Squares:", square)


# Find duplicate elements.
lis = list(map(int, input("Enter list elements: "). split()))

duplicate = []
for i in lis:
    if lis.count(i) > 1 and i not in duplicate:
        duplicate.append(i)

print("Duplicate Elements:", duplicate)