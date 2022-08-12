months = ("january","february","march","april","may","june","july","august","september","october","november","december")
birthday= input ("Type your birthday in the format DD-MM-YYYY: ")
index = int(birthday[3:5])-1
bd_month = months[index]

print ("you were born in", bd_month)


names =["manisha","manu","isha"]
new_name= input ("Enter your name ")
names.append(new_name)
print("Here's the list: ",names)


