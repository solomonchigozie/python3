
class Animal:
    def walk(self):
        print("walking...")

class Dog(Animal):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print("wolf")

#instance of a class, which is an object
roger = Dog("roger", 8) 

print(type(roger)) ,

print( roger.name )
print( roger.age )

roger.bark()
roger.walk()
  