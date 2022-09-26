# BMI Calculator

#Take user inputs

height=float(input("Enter your height in m: "))
weight=float(input("Enter your weight in kg: "))


# Formula for BMI calculation

#BMI=weight/height^2
bmi=int(weight/(height**2))

#print output
print("Your BMI is: "+str(bmi))