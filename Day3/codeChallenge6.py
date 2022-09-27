#Treasure find game 

print("Welcome to Treasure Island.\nYour mission is to find the trasure.\n")
print('''                                   
    | |                                    
    | |_ _ __ ___  __ _ ___ _   _ _ __ ___ 
    | __| '__/ _ \/ _` / __| | | | '__/ _ }
    | |_| | |  __/ (_| \__ \ |_| | | |  __/
    \__|_|  \___|\__,_|___/\__,_|_|  \___|
''')

print("------------------------------------------------------------------------------------------------------------------------------------")

choosePath=input("Your are at a cross road.Where do yuo want to go? type 'left' or 'right' : ")

if(choosePath=="left"):
    chooseOption=input("You came to a lake.There is an island in the middle of the lake.type 'wait' for a boat.type 'swim' to swim across: ")
    if(chooseOption=="wait"):
        print("Now you came to the island.There is a Pyramid,To enter the pyramid and find tresuere you have 3 doors")
        chooseDoor=input("What is you choose door 'yellow' 'blue' 'red' : ")
        if(chooseDoor=="yellow"):
            print("------------------------------------------------------------------------------------------------------------------------------------")
            print("Congratulations! You found the treasure!\n")
        else:
            print("------------------------------------------------------------------------------------------------------------------------------------")
            print("You choose wrong door! GAME OVER!\n")
    else:
        print("------------------------------------------------------------------------------------------------------------------------------------")
        print("You choose wrong option! GAME OVER!\n")
else:
    print("------------------------------------------------------------------------------------------------------------------------------------")
    print("You choose wrong path! GAME OVER!\n")



