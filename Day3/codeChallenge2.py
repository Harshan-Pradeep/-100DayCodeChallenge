# BMI Calculator upgdrade which is created in Day2.
#Today add interpretation of their BMI based on the BMI value

# BMI Calculator

#Take user inputs

height=float(input("Enter your height in m: "))
weight=float(input("Enter your weight in kg: "))


# Formula for BMI calculation

#BMI=weight/height^2
bmi=int(weight/(height**2))

#print output
print("Your BMI is: "+str(bmi))

#Interpretation based on thier BMI value

if(bmi<=18.5):
    print(f"Your BMI is {bmi} , you are Underweight")
elif(18.5<bmi<=25):
    print(f"Your BMI is {bmi} , you are Normal Weight")
elif(25<bmi<=30):
    print(f"Your BMI is {bmi} , you are Overweight")
elif(30<bmi>=35):
    print(f"Your BMI is {bmi} , you are Obese")
else:
    print(f"Your BMI is {bmi} , you are Clinically Obese")
