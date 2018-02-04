# Allow us to work with key value pairs
# associative arrays in PHP for example

student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
print(student)
print(student['name'])


# keys can be almost any data type
car = {1: 'Toyota'}

# throws an error if key doesn't exist
# better to return none or default value
# use dictionary get method

print(student.get('name')) # isntead of brackets

print(student.get('phone')) # returns none

pritn(student.get('phone', 'Not Found')) # default value case not found


# add new keys and values

student['phone'] = '8239923828'

# if key exists doing the above updates the value


# update values using update method, update several

student.update({'name': 'Thut', 'age': 34})


# delete specific key and value
# use del key word

del student['age'] # age key deleted

# remove using pop method, will remove then return the removed value
# allows us to get the removed value in a variable

age = student.pop('age')
print(age) # prints popped key 

# how many keys we got in the dictionary
print(len(student))

print(student.keys()) # print all keys

print(student.values()) # prints all values

print(student.item()) # prints keys and value pairs



# loop through keys and values
for key in student:
    print(key) # prints out only keys

# print keys and values
for key, value in student.items():
    print(key, value)