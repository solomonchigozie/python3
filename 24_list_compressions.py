numbers = [1,2,3,4,5,6,7]

numbers_power_2  = [n**2 for n in  numbers]

print(numbers_power_2)

# with loops
numbers_power_3 = []
for n in numbers:
    numbers_power_3.append(n**2)

# with map
numbers_power_4 = list(map(lambda n: n**2, numbers))

# the loop is easily done wit list compressions
