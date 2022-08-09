# Lists let us group Similar things together, so we can perform operaations on them.
# To organise information and access it we use Lists
# Lists are mutable in python(we can add or modify)


#list of numbers
numbers = [1,2,3]

#list of Strings
pizza_toppings = ["cheese", "pepperoni", "mozerella"]

#mixed list
mixed_list = [1, "cheese", 2, "pepperoni"]

#list of lists
list_of_lists = [ [ 1, 2 ], [ 12, 14 ] ]

# To access individual Element of a list we use index.
print(pizza_toppings[1])
print(pizza_toppings[-1])
print(len(pizza_toppings))
print(len(list_of_lists), list_of_lists[1])

# To try mutable lists (adding new element in list)
# We use 'insert' function to add an item at a specific position
pizza_toppings.append("chicken")
pizza_toppings.insert(1, "mushrooms")
print(pizza_toppings)

# To remove an item we use del function
del pizza_toppings[2]
print(pizza_toppings)

# To delete from the end of list we use pop
pizza_toppings.pop()
print(pizza_toppings)

# To delete specific element we use remove
pizza_toppings.remove("mushrooms")
print(pizza_toppings)
