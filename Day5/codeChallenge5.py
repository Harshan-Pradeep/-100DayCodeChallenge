#Write a program for random password generator
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

#calculate how many rest letters need.
restLetters=nr_letters-(nr_numbers+nr_symbols)

#Create a list for random password
password=[]

#new list for more randomize password
randomPassword=[]

#Choose random letters
for letter in range(0,restLetters):
    password.append((random.choice(letters)))

#Choose random symbols
for symbol in range(0,nr_symbols):
    password.append((random.choice(symbols)))

#Choose random numbers
for number in range(0,nr_numbers):
    password.append((random.choice(numbers)))

#Make password more randomize before created
#This job also can do with random.shuffle(password)
for passowordRand in range(0,nr_letters):
    randomPassword.append((random.choice(password)))
    password.remove(randomPassword[passowordRand])

#print password without list type
for item in randomPassword:
    print(item,end='')

#This work also can do with 
# passwordString=""
#for char in password:
#   password+=char
#print(f"Your password is: {password}")