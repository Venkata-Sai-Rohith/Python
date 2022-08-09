#Expected Output
# Welcome to Julie's Pizzeria
#Our available toppings are
# Cheese (free)
# Pepperoni($1 Extra)

pizza_toppings = ["cheese","pepperoni"]

def format_topping(topping):
    if topping =="cheese":
        return f"{topping.title()} (Free)"
    else:
        return f"{topping.title()} ($1 Extra)"

def print_menu(toppings):
    print("Welcome to julie's pizzeria")
    print("Our available toppings are: ")
    for topping in toppings:
        print(format_topping(topping))

print_menu(pizza_toppings)
