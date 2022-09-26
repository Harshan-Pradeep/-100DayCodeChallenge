#Create a program using maths and f-string that tells us how many days , weeks,months we have left if we live until 90 years old

#Take age as a input
age=int(input("What is your current age: "))

#caluclate years to live from this age to 90 years old
years=90-age

#caluclate months to live from this age to 90 years old
months=years*12

#caluclate weeks to live from this age to 90 years old
weeks=years*52

#caluclate dayss to live from this age to 90 years old
days=years*365

#print days,weeks,months and year to have live

print(f"You have {days} days,  {weeks} weeks, {months} months, {years} years left.")


