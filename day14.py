from getpass import getpass as input
print("Game of Rock x Paper x Scissors")
player1 = input ("Player 1 Chose (r)ock, (p)aper or (s)cissors: ")
player2 = input ("Player 2 Chose (r)ock, (p)aper or (s)cissors: ")
if player1 == "r":
    if player2 == "r":
        print ("Rock vs Rock - A tie!")
    elif player2 == "p":
        print ("Rock vs Paper - Player 2 wins!")
    elif player2 == "s":
        print ("Rock vs Scissors - Player 1 wins!")
    else:
        print("Something went wrong... :/")
elif player1 == "p":
    if player2 == "r":
        print ("Paper vs Rock - Player 1 wins!")
    elif player2 == "p":
        print ("Paper vs Paper - A tie!")
    elif player2 == "s":
        print ("Paper vs Scissors - Player 2 wins!")
    else:
        print("Something went wrong... :/")
elif player1 == "s":
    if player2 == "r":
        print ("Scissors vs Rock - Player 2 wins!")
    elif player2 == "p":
        print ("Scisssors vs Paper - Player 1 wins!")
    elif player2 == "s":
        print ("Scissors vs Scissors - A tie!")
    else:
        print("Something went wrong... :/")
else:
    print("Something went wrong... :/")
