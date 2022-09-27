#Write a program taht works out whether if a given year is a leaf year or not.

year=int(input("Enter a year: "))

#check whether leap year or not
if(year%4==0):
    if(year%100==0):
        if(year%400==0):
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
