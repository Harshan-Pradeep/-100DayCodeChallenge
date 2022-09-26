#Tip calculator

#Greeting
print("Welcome to the tip calculator.")

#Take input from user
totalBill=float(input("What was the total bill? $ "))
tipPercentage=int(input("What percentage tip would you like ti give 10, 12 or 15? "))
totalPerson=int(input("How many people to split the bill? "))

#calcualtion part
billWithTip=(totalBill*(tipPercentage/100))+totalBill
personPayment=round(billWithTip/totalPerson , 2)

# print output
print(f"Each person should pay: ${personPayment}")