# Python Operators

a = 10
b = 3

# 1. Arithmetic Operators
print("Arithmetic Operators")

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Power:", a ** b)


# 2. Comparison Operators
print("Comparison Operators")

print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater Than:", a > b)
print("Less Than:", a < b)
print("Greater Than or Equal:", a >= b)
print("Less Than or Equal:", a <= b)


# 3. Assignment Operators
print("Assignment Operators")

x = 10

x += 5
print("After +=:", x)

x -= 3
print("After -=:", x)

x *= 2
print("After *=:", x)

x /= 2
print("After /=:", x)

x //= 2
print("After //=:", x)

x %= 3
print("After %=:", x)

x **= 2
print("After **=:", x)


# 4. Logical Operators
print("Logical Operators")

age = 20

print("AND:", age > 18 and age < 30)
print("OR:", age < 18 or age > 18)
print("NOT:", not(age > 18))


# 5. Identity Operators
print("Identity Operators")

list1 = [10, 20, 30]
list2 = list1
list3 = [10, 20, 30]

print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)
print("list1 is not list3:", list1 is not list3)


# 6. Membership Operators
print("Membership Operators")

numbers = [10, 20, 30, 40, 50]

print("20 in numbers:", 20 in numbers)
print("100 in numbers:", 100 in numbers)
print("100 not in numbers:", 100 not in numbers)


# 7. Bitwise Operators
print("Bitwise Operators")

x = 10
y = 5

print("Bitwise AND:", x & y)
print("Bitwise OR:", x | y)
print("Bitwise XOR:", x ^ y)
print("Bitwise NOT:", ~x)
print("Left Shift:", x << 1)
print("Right Shift:", x >> 1)