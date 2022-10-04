import random
#Write a  code for virtual coin toss program.It will randomly tell the user "Heads" or "Tails".

randomSide=random.randint(0,1)
if(randomSide==1):
    print(f"Heads")
else:
    print(f"Tails")