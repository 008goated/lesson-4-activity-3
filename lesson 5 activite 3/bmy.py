hieght=float(input("enter your hieght in centimeters:"))
wieght=float(input("enter your weight in kgs"))
bmi=wieght/(hieght / 100)**2
print("your bmi is ",bmi)
if bmi <= 18.5:
    print ("you are under weight")
elif bmi <= 24.9:
    print("you are healthy")
elif bmi <= 29.9:
    print("you are over weight")
elif bmi <= 34.9:
    print("you are severly over weight")
elif bmi <= 39.9:
    print("then you are obease")
else:print("you are severly obease")