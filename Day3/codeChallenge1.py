# Write a program that works out whether if a given number is an odd or even number.

#Take a number as a user input
number=int(input("Enter a number: "))

#Check whether if a given number is an odd or even number. 
if (number%2==0):
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")
