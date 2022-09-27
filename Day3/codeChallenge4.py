#Create automatci pizza order program, Based on a user's order,work out thier final bill.

#Greeting
print("Welcome to the python pizza Deliveries!\n\n")

print("Small Pizza: $15\nMedium Pizza: $20\nLarge Pizza: $25\n\n\nPepperoni for small pizza: +$2\nPepperoni for medium or large pizza: +$3\n\n\nExtra xheese for any size pizza: +$1")

#Take inputs
size=input("What size pizza do you want? s , m , l : ")
add_pepperoni=input("Do you want pepperoni? y or n :")
extra_cheese=input("Do you want extra cheese? y or n :")
bill=0

if(size=="s"):
    bill=15
    if(add_pepperoni=="y"):
        bill+=2
    if(extra_cheese=="y"):
        bill+=1
    print(f"Your final bill is {bill}$")
elif(size=="m"):
    bill=20
    if(add_pepperoni=="y"):
        bill+=3
    if(extra_cheese=="y"):
        bill+=1
    print(f"Your final bill is {bill}$")
elif(size=="l"):
    bill=25
    if(add_pepperoni=="y"):
        bill+=3
    if(extra_cheese=="y"):
        bill+=1
    print(f"Your final bill is {bill}$")
else:
    print("You entered wrong input!")


