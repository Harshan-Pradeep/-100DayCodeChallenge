#Write a program which will mark a spot with and X.The map is made 3 rows of blank squares.
#The program allow to enter the position of the treasure using two-digit system.The first digit is the vertical column number and the second digit is the horizontal row number.

#rows of the map
row1=["⬜","⬜","⬜"]
row2=["⬜","⬜","⬜"]
row3=["⬜","⬜","⬜"]

#nested lists
map=[row1,row2,row3]

print(f"{row1}\n{row2}\n{row3}\n")

#take two integers to determine as position
position=input("Enter two digit for verticle and horizontal, Where do you want to put the treasure? ")

positionY=int(position[0])-1

#If condition will check what is the row and then chanage emoji to 'X' after check column
if(position[1]=="1"):
    row1[int(position[0])-1]="X"
    print(f"{row1}\n{row2}\n{row3}\n")
elif(position[1]=="2"):
    row2[int(position[0])-1]="X"
    print(f"{row1}\n{row2}\n{row3}\n")
elif(position[1]=="3"):
    row3[int(position[0])-1]="X"
    print(f"{row1}\n{row2}\n{row3}\n")
else:
    print("Wrong input!")

#Another method of doing this challenge
#rows of the map
row1=["⬜","⬜","⬜"]
row2=["⬜","⬜","⬜"]
row3=["⬜","⬜","⬜"]

#nested lists
map=[row1,row2,row3]

print(f"{row1}\n{row2}\n{row3}\n")

#take two integers to determine as position
position=input("Enter two digit for verticle and horizontal, Where do you want to put the treasure? ")
map[int(position[1])-1][int(position[0])-1]="X"
print(f"{row1}\n{row2}\n{row3}\n")


