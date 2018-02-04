if True:
    print('Condition was true')

# ==, <=, >=, !=
# Object Identity:      is

language = 'Python'

if language == 'Python':
    print('Language is python')
else:
    print('No match')

if language == 'Python':
    print('Language is python')
elif language == 'Java':
    print('Language is Java')
elif language == 'C++':
    print('Language is C++')
else:
    print('No match')


# Python has no switch case statement... if elif else will do

# Boolean operations we can use
# and or not

user = 'Admin'
logged_in = True

if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad creds')


# not used to switch a boolean
if not logged_in:
    print('Please log in')
else:
    print('Logged in')

# two objects can be equal but not the same in memory
a = [1,2,3]
b = [1,2,3]

print(a == b)
print(a is b)

print(id(a))
print(id(b))

# conditions evaluating to false
# False Values:
# False
# None
# Zero of any numeric type
# An empty sequence e.g. '', (), []
# An empty mapping e.g. {}

condition = False

if condition:
    print('Evaluated to tru')
else:
    print('Evaluated to false')


condition = 0

if condition:
    print('Evaluated to tru')
else:
    print('Evaluated to false')


condition = ()

if condition:
    print('Evaluated to tru')
else:
    print('Evaluated to false')



condition = ''

if condition:
    print('Evaluated to tru')
else:
    print('Evaluated to false')