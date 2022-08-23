

height = float (input ("Enter your Height in meters: "))
weight = float (input("Enter your Weight in Kgs: "))

#BMI = weight / (height * height) or
BMI = weight / (height **2)

print("Your BMI is: ",round(BMI,2))

if (BMI <= 18.5):
    classification = "Under weight"
elif (BMI >18.5 and BMI<= 24.9):
    classification = "Normal weight"
elif (BMI >24.9 and BMI<= 29.9):
    classification = "Over weight"
else:
    classification = "Obesity"

print("The classification of your BMI is: ", classification)
