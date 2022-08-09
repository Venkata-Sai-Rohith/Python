# With no Arguments
def say_hello():
    print("hello")
say_hello()

# Argument with a return value 
def say_hello(name):
    print(f"hello {name}")
say_hello("rohith")

# Declaring Multiple arguments with return value
def name_age(name, age):
    print(f"My name is {name}. My age is {age}")
name_age("Rohith", 24)

def arguments(integer):
    print(f"Square of  {integer} is {integer*integer}")
arguments(5)
