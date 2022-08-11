#To print the initials of given names
first_name = input("Enter your first name: ")
middle_name=  input("Enter your middle name: ")
last_name= input ("Enter your last name: ")
print ("Your initials are ",first_name[0],middle_name[0],last_name[0])


#To print different info from the given Code
product_code = str(input ("Enter the product code: "))
print ("Country code: ",product_code[0:3])
print("Product code: ",product_code[4:9])
print("Batch number: ",product_code[-5:])
