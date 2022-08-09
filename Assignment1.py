# To create a simple Calculator
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation=str(input("Enter the operation to perform: "))

if  "add" in operation:
    print(" The sum of  a and b is:", num1+num2)
    
elif  "sub" in operation:
    print(" The subraction of a and b is:", num1-num2)
    
elif  "mul" in operation:
    print(" The multiplication of a and b is:", num1*num2)

else:
    print(" The division of a and b is:", num1/num2)

