import random
#Write a program which will select a random name from a list of names.The person selected will have to pay for everybody's food bill.

nameString=input("Give everybody's names, seperated by a comma. ")

#split function will remove given characters
names=nameString.split(", ")

#get the size of names list,len() function helps to to get size
lengthOfNames=len(names)

#get random number for choose a name 
randomChoice=random.randint(0,lengthOfNames-1)

#print random name with using random number
print(f"{names[randomChoice]} is goiong to buy the meal today!")

#using random.choice() we can do the same thing
# print(f"{random.choice(names)} is goiong to buy the meal today! ") 

