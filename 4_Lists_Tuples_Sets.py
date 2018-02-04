# Lists and tuples allow us to work with sequential data
# Tuples is unordered collection of values with no duplicates

# Lists
courses = ['History', 'Math', 'Pysics', 'CompSci']
print(courses)

# Length of list
print(len(courses))

# Access values individually, using square brackets passing in location of value we want
# using index
print(courses[0])

# Last value from the list, using negative indexes... starts from the last
print(courses[-1])

# Flip, reverse the whole list
print(courses[::-1])

# Access range of values... slicing 
print(courses[0:2]) # Fist index is inclusive, the second is not -> 2 is not inclusive in this case

# same as
print(courses[:2])

# till the end
print(courses[1:])


# List methods
# Adding items to end of list using append method
courses.append('Art')
print(courses)

# Add to a specific location, use insert method... it takes in two methods -> index and value
courses.insert(0, 'Art')
print(courses) # inserts, doesn't overwrite

# Extend method... when we have multiple values we want to add to our list
# e.g. two lists

courses2 = ['Art', 'Education']

# using insert will add a list to another list
# extend method adds the individual elements

courses.extend(courses2)
print(courses)

# Remove values from list
# Using remove method

courses.remove('Math')
print(courses)

# using pop method
courses.pop() # removes last item

# pop returns removed value
popped = courses.pop()
print(popped)

# Sorting our list

# reverse our list
courses.reverse()

# sorting our list
courses.sort()

#strings sorted alphabetically, numbers sorted alphabetically

# sort in reverse
corses.sort(reverse=True)


# Sorted version of courses list without altering the original
# use the sorted function
sorted_courses = sorted(courses)
print(sorted_courses)


nums = [1,3,4,3,2,4,5]
print(min(nums)) # returns 1 as minimum value
print(max(nums))
print(sum(nums)) # prints sum of the entire list

print(courses.index('CompSci')) # finds the index of CompSci

print('Art' in courses) # returns boolean, if in the list or not

for item in courses:
    print(item)

for index, course in enumerate(courses, start=1):
    print(index, course)

# turning list into strings 
# use string method join
# turn list of courses to string 

course_str = ', '.join(courses)
print(course_str)

new_list = corse_str.split(', ')
print(new_list)






# Tuples
# We can't modify tuples, they are immutable... lists are mutable
# use parenthesis ()

tuple_1 = ('History', 'Math', 'Physics')
tuple_2 = tuple_1

# tuple doens't support item assignment







# Sets
# Values that are unordered and have no duplicates
# use curly braces

cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'CompSci'}
print(cs_courses) # don't care about order, gets rid of duplicates

# sets do membership tests more efficiently than tuples and lists
print('Math' in cs_courses)

# determine values that share or don't share with other sets

print(cs_courses.intersection(art_courses)))
.difference
.union











# Creating Empty lists
empty_list = []
empty_list = list()

# Empty Tuples 
empty_tuple = ()
empty_tuple = tuple()

# Empty Set
empty_set = {} # <-- This isn't right, it's a dictionary
empty_set = set()