# Argument without return and printing
def pizza_name(topping):
    print(f"{topping.title()} Pizza")
pizza_name("mozerella")

# Argument with 'topping' as return and storing in variable 'pizza'
def pizza_name(topping):
    return f"{topping.title()} Pizza"
pizza = pizza_name("mozerella")
print(pizza)

# Can you make a Function that accepts a name and age as arguments,
# and return a string formatted to display both?
# can you store that in a variable and then print the variable ?

def bd(name, age):
    return f"My name is {name.title()}. My age is {age}"
details = bd ("Rohith", 24)
print(details)

