#Write a program that calculates the highest score from a list of scores.

scoreList=input("Input a list of scores: ").split(',')

#Initialize heighestScore varibale as 0
heighestScore=0

#Use for loop for find highest score with go through the list
for score in range(len(scoreList)):
    if heighestScore< int(scoreList[score]):
        heighestScore=int(scoreList[score])

#Print height score
print(f"The heighest score is {heighestScore}")