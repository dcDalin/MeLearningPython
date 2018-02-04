# ninjas = ['Scorpion', 'Sub Zero', 'Lui Kang']

# for ninja in ninjas:
#     print(ninja)

nums = [1,2,3,4,5]

# for num in nums:
#     print(num)

for num in nums:
    if num == 3:
        print('Found')
        break
    print (num)

for num in nums:
    if num == 3:
        print('Found')
        continue
    print (num)

# Loop within a loop

for num in nums:
    for letter in 'abc':
        print(num, letter)

# range is useful to run through a loop a certain number of times

for i in range(10):
    print(i)

for i in range(1, 11):
    print(i)

# While loop keeps going till condition is met or till we hit a break

x = 0

while x < 10:
    print(x)
    x += 1

while x < 10:
    if x == 5:
        break
    print(x)
    x += 1

# print infinate loop

while True:
    if x == 5:
        break
    x += 1

 