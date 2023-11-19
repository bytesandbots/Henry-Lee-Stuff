## we need to implement a variable or property to store last move
## your next move is determined by your opponents last move
## Henry, if you could, please bring a notebook with you so you can keep track of notes you take

from board import Board
import random

firstMove = True
largeBoard = Board()
smallBoards = [Board(), Board(), Board(), Board(), Board(), Board(), Board(), Board(), Board()]
previousMove = None
smallBoard = None
def checkInput(number):

    try:
        number = int(number)
    except ValueError:
        return False
        
    if  number >= 0 and number < 9:
        return True
    else:
        return False
def computerPlay():
    global smallBoard
    randBox = random.randint(0,8)
    while not smallBoards[smallBoard].fill(randBox, "O"):
        randBox = random.randint(0,8)
    smallBoard = randBox
def playerPlay():
    print(largeBoard)
    print(f"        Board {smallBoard}")
    print(smallBoards[smallBoard])
    print("Choose a box")
    userInput = input()
    while not checkInput(userInput):
        print("Choose a box")
        box = userInput = input()
    while not smallBoards[smallBoard].fill(userInput, "X"):
        print("Choose a box")
        userInput = input()
        while not checkInput(userInput):
            print("Choose a box")
            box = userInput = input()
print("User is X. Computer is O.")
while largeBoard.checkWin() == False:
    print("HHHHHH")
    if firstMove:
        ## Must be changed to (0,1) ## Can be possibly exchanged with bool(random.getrandbits(1))
       firstMove = False
       if bool(random.getrandbits(1)):
           player = previousMove = "X"
           print(f"       Main Board")
           print(largeBoard)
           print("Enter a board number from 0-8")
           userInput = input()
           while not checkInput(userInput):
               print("Enter a board number from 0-8")
               userInput = input()
           smallBoard = int(userInput) 
           print(f"        Board {smallBoard}")
           print(smallBoards[smallBoard])
           print("Which AVAILABLE box, do you want to go in?")
           spot = userInput = int(input())
           while not smallBoards[smallBoard].fill(spot, player):
                userInput = int(input())
                if checkInput(userInput):
                    spot = userInput
                    smallBoard = spot
                else:
                    continue
       else:
           player = previousMove = "O"
           print("The computer is playing first")
           print(f"       Main Board")
           print(largeBoard.printBoard)
           smallBoard = random.randint(0,8)
           print(f"        Board {smallBoard}")
           print(smallBoards[smallBoard])
           randBox = random.randint(0,8)
           smallBoards[smallBoard].fill(randBox, player)
           smallBoard = randBox
           ## computer needs to choose a box to fill in the small board
    else:
        if previousMove == "O":
            playerPlay()
            previousMove = "X"
        else:
            computerPlay()
            previousMove = "O"
        
        
       

