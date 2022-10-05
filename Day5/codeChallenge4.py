#Write a program that automatically prints the solution to the FizzBuzz game.
#The program should print each number from 1 to 100 in turn.
#When the number divisible by 3 - should print Fizz.
#When the number divisible by 5 - should print BUzz.
#When the number divisible by 3 and 5 both - should print FizzBuzz.

#use for loop for go through 1 to 100
for number in range(1,101):

#Check the number Fizz,Buzz,FizzBuzz or normal number.
    if ((number%3==0) and (number%5==0)):
        print("FizzBuzz")
    elif(number%3==0):
        print("Fizz")
    elif(number%5==0):
        print("Buzz")
    else:
        print(number)