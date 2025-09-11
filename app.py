from enum import Enum

class MyEnum(Enum):
    """
    Enum Description: 
    """
    INACTIVE = 0
    ACTIVE = 1
    BLUE = "blue "

print(MyEnum.BLUE.value.upper())

print("""HELLO
WORD """)

print(len("name"))
name = "john"
print("me" in name) 

x1 = True
x2 = False 
print(all([x1, x2]))

ingredients_purchased = True
meal_cooked = False 

ready_to_serve = any([ingredients_purchased, meal_cooked])
print(ready_to_serve)


# complex numbers
num1 = complex(1,2)
num2 = 2+3j

print(num2.real, num2.imag)

