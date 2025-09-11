condition = True

while condition == True:
    print('condition is true')
    condition = False

count = 0
while count < 10:
    print("the condition is true")
    count += 1
print("After the loop")

# for loop
items = [1,2,3,4]
for item in items:
    print(item)

for x in range(15):
    print(x)

# getting the index of the list
names = ["Jonh", "Mem", "Dodge"]
for index, item in enumerate(names):
    print(index, item)

# break and continue
for item in items:
    if item == 2:
        continue
    print(item)