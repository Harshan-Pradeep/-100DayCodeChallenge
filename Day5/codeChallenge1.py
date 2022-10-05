#Write a program that calculates the average student height from a list of height.

sum=0
total=0

#Take Height as inputs.
studentHeights=input("Input a list of student heights: ").split(',')

#Convert inputed string heights into integers and calculate total of the height.
for studentHeight in range(len(studentHeights)):
    studentHeights[studentHeight]=int(studentHeights[studentHeight])
    sum+=studentHeights[studentHeight]
    
#Print heights list.
print(studentHeights)

#Calculate average.
average=sum/len(studentHeights)

#Print Average after converting float number to whole number.
print(f"Average of the height is {round(average)}")





