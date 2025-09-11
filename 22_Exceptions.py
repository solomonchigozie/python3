"""Exception handling are for handling errors"""

# try:
#     result = 2/0
# except Exception as e:
#     raise e
# else:
#     #no exceptions were raised
# finally:
#     #do something in any case

# result = 2/0
# print(result)

try:
    result = 2/0
except ZeroDivisionError:
    print("cannot divide by zero!")
finally:
    result =1

print(result)


#you can raise exception
# raise Exception("An error!")

try:
    raise Exception("An error!")
except Exception as e:
    print(e)
# end try


#defin exception class extending from exception
class DogNotFoundException(Exception):
    pass

try:
    raise DogNotFoundException()
except DogNotFoundException:
    print("Dog not found!")
# end try
