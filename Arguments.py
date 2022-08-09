#SPECIAL FUNCTIONS IN PY

#Default Argument
def default(x,y=10):
    print("x: ",x)
    print("y: ",y)
    return
    #default(10)
    #default(30,50) #the y value will be replaced with 50
default(10,"abc") #the y value is replaced with "abc"

#Required Arguments
def  req(x,y):
    print(x,y)
    return
req(10,2.3)

#Function Arguments
def keyword(name, age):
    print("name: ", name)
    print("age: ",age)
    return
keyword(age= 21,name= "annie")

#Variable Arguments
def variable (*arr):
    print(arr)
    return
#variable ()
#variable (10,20)
variable(10,'g',2,'abdgjkn',2.34)

#2nd program
def vary (*arr):
    print("count: ",len(arr))
    print("first ele: ",arr[0])
    print("last ele: ",arr[len(arr)-1])
    print("last ele: ",arr[-1])
    return
vary(10,20,30,40,50,60)

#3rd Program
def var(*arr):
    print("using for range: ")
    for i in range(len(arr)):
        print(arr[i])
        for j in range (len(arr)-1):
            print(arr[j])
    return
var(10,20,30,40,50)
    
