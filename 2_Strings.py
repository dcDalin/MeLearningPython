# No need for semi colons, python uses white spaces
# making it a clean language

# variables are usually lowercase, common convention
# should be as descriptive as possible <- just convention

message = 'hello world'
message2 = "hello world"
print(message)
print(message2)

# Escape single quote with backslash
message3 = 'Bobby\'s World'
print(message3)
# Use doubel quotes on string containing double quotes
message4 = "Bobby's World"
print(message4)

# Print multiple lines
message5 = '''This is multiple 
line 
sentence '''
print(message5)

# Number of characters in string
print(len(message))

# Access string character using square brackets
# Find index
print(message[0])

# Index error thrown case you access an index that doesn't exist

# Access range of characters
# 0 is the starting point and inclusive, second index is the ending point but not inclusive
print(message[0:5])

# Slicing strings
print(message[:5])
print(message[5:])

# Some methods of string data types
# Method, function belonging to an object

# lower case
print(message.lower())

# upper case
print(message.upper())

# count number of characters, takes in a string
print(message.count('Hello'))
print(message.count('l'))

# find index of certain characters
# return index where the word starts
# returns -1 case can't find string of characters
print(message.find('world'))

# Replace characters in our string with other string
# takes in two paramerters 
new_message = message.replace('World', 'Universe')
print(new_message)

# add multiple strings, and concatinate them
greeting = 'Hello'
name = 'Mike'
# use the + sign
message = greeting + name
print(message)

message = greeting + ', ' + name
print(message)

# Better to use a formatted string
message = '{}, {}. Welcome!'.format(greeting, name)

# f strings... from python 3.6 and above
message = f'{greeting}, {name}. Welcome!'

message = f'{greeting}, {name.upper()}. Welcome!'

print(message)

# prints out all the attributes and methods available to the type
print(dir(name))

# use help function
print(help(str))

print(help(str.lower))
