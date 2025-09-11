from functools import reduce

#map
numbers = [1,2,4]

def double(a):
    return a * 3

result = map(double, numbers)

print(list(result))


#same process using a lambda function'
double2 = lambda a: a * 3
# result2 = map(double2, numbers)

#expanding futher
result2 = map(lambda a: a * 3, numbers)
print(list(result2))


#filter
number = [1,2,4,5,6,7,8,9,10]
result3 = filter(lambda n: n%2 == 0, number)
print(list(result3))


#reduce
expenses= [
    ('Dinner', 80),
    ('Car', 120)
]

sum = reduce(lambda a,b: a[1] + b[1], expenses)
print(sum)