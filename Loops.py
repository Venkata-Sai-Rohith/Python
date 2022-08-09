pizza_toppings=["cheese","pepperoni","mushrooms"]
for topping in pizza_toppings:
    message = f"i would like {topping} on my pizza"
    print(message)

my_numb = [1,2,3]
my_square_numbers = []
for number in my_numb:
    my_square_numbers.append(number**2)
print(my_square_numbers)

#To print even and odd
numb= [1,2,3,4,5,6,7,8,9,10]
for i in numb:
    if (i%2==1):
        print(f" {i} is odd")
    else:
        print(f" {i} is even")

#Using Ranges, python doesn't consider the last element in the range
for i in range(1,11):
    if (i%2==1):
        print(f"{i} is odd")
    else:
        print(f"{i} is even")

#Playing with else
toppings= ["cheese","pepperoni","mushroom","chicken"]
print("we have the following toppings: ")
for price in toppings:
    if  price == "cheese" or price =="mushroom":
        print(f"{price} is (free)")
    else:
        print(f"{price} is ($2.00)")
        
        
