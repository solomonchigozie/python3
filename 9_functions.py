def hello(name, age):
    print("hello "+name+", you are "+str(age)+" years old.")
hello("John", 40)


def change(value):
    value = 209
val = 1
change(val)
print(val)
    
def hello_two(name):
    if not name:
        return
    print('Hello '+name+'!')
hello_two(False)

age = 8
def test():
    print(age)
print(age)
test()

def talk(phrase):
    def say(word):
        print(word)
    
    words = phrase.split(' ')
    for word in words:
        say(word)

talk('I am going to buy the milk')

# closures
def count():
    count = 0

    def increment():
        nonlocal count
        count = count + 1 
        print(count)
    increment() 
count()


def counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1 
        return count 
    return increment 
increment = counter()

print(increment())
print(increment())
print(increment())