# Integer -> whole number, float -> decimal

num = 3
num2 = 3.123

# in built function type shows type
print(type(num))
print(type(num2))

# Arithmetic

# Addition          3 + 2 = 5
# Subtraction       3 - 2 = 1
# Multiplication    3 * 2 = 6
# Division          3 / 2 = 1.5
# Floor Division    3 // 2 = 1
# Exponent          3 ** 2 = 9
# Modulus           3 % 2 = 1

# Order of operations work as usual

num = 1
num = num + 1
num += 1
num *= 10
print(num)


# absolute value, removes negative
print(abs(-3))

# rounds up
print(round(3.23))

# round to number of decimal places
print(round(3.71, 1))

# comparison operators ==, !=, >, <, >=, <=
# comparison operators return a boolean
# single equal is assignment

num1 = 2
num2 = 3
print(num1 == num2) # prints false


# variables that look like numbers but they actually strings
num1 = '100'
num2 = '200'

print(num1 + num2) # prints 100200
# addings strings just concatinates

# casting -> change from string to integers
num1 = int(num1)
num2 = int(num2)

print(num1 + num2) # prints 300