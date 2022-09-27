#Write a program that tests the compatibility between two people,To write this code I am going to use the super scientific method recommended by BuzzFeed.

#Greeting
print("Welcome to the Love Calculator!")

#Take inputs
name1=input("What is your name? ").lower()
name2=input("What is their name? ").lower()

#Concatinate two names to easy to find letter cound
name=name1+name2

#Find letter count
true=name.count("t")+name.count("r")+name.count("u")+name.count("e")
love=name.count("l")+name.count("o")+name.count("v")+name.count("e")

score=int(str(true)+str(love))


#check they are belong to which category
if(score<10 or score>90):
    print(f"Your score is {score} , you go together like coke and mentos.")
elif(40<score<50):
    print(f"Your score is {score} , your are alright together.")
else:
    print(f"Your score is {score}.")
    

