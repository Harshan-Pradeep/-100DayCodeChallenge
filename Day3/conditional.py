# IF AND ELSE
# This code will check height of the person before ride the rollercoaster

#Take height from user
print("Welcome to the rollercoaster!")
height=int(input("What is your height in cm? "))

#check height is greater than 120cm using if else conditonals
if height>120:
    print("You can ride the rollercoaster!")
    
else:
    print("You can ride the rollercoaster!")

# NESTED IF ELSE AND ELIF
print("----------------------------------------------------------------------------------------------------------")


#Take height from user
print("Welcome to the rollercoaster!")
height=int(input("What is your height in cm? "))


#check height is greater than 120cm using if else conditonals
if height>120:
    bill=0
    print("You can ride the rollercoaster!")
    #Take age as a input to check age is greater than 18
    age=int(input("What is your age: "))

    if(age>=18):
        bill=12
        print("Adult ticket price 12$.")
    elif(age>=12):
        bill=7
        print("Youth ticket pricepay 7$.")
    else:
        bill=5
        print("Children ticket pricepay 5$.")
    wants_photo=input("Do you want a photo taken? y or n")

    if(wants_photo=="y"):
        bill+=3
    print(f"Your final bill is {bill}$")

    
else:
    print("You can ride the rollercoaster!")

