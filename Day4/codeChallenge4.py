import random
#Write a program for Rock Paper Scissor game to play with computer.

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

print("----This is Rock Paper Scissor game----")

handSignal=[rock,paper,scissor]

#Get hand signal input from user
userHandSignal=int(input("What do you choose? Type 0 for Rock , 1 for Paper or 2 for Scissor :"))



#Check whether input is correct or incorrect
if(userHandSignal<3):
    #print user hand signal
    print(f"Your Hand Signal\n {handSignal[userHandSignal]}")

    #Generate computer hand signal
    computerHandSignal=random.choice(handSignal)

    #print computer generated hand signal
    print(f"Computer Hand Signal\n {computerHandSignal}")

    # check where user win scenarios

    if((userHandSignal==0 and computerHandSignal==handSignal[2]) or (userHandSignal==2 and computerHandSignal==handSignal[1]) or (userHandSignal==1 and computerHandSignal==handSignal[0])  ):
        print("You Win!")

    # check where round draw scenarios
    elif((userHandSignal==0 and computerHandSignal==handSignal[0]) or (userHandSignal==1 and computerHandSignal==handSignal[1]) or (userHandSignal==2 and computerHandSignal==handSignal[2])):
        print("Round Draw!")

    else:
        print("You Lose!")
else:
    print("You entered wrong input!")
    



