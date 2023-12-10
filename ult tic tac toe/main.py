## we need to implement a variable or property to store last move
## your next move is determined by your opponents last move
## Henry, if you could, please bring a notebook with you so you can keep track of notes you take

from board import Board
import random

firstMove = True
largeBoard = Board("main", mainBoard = True)
smallBoards = [Board("0"), Board("1"), Board("2"), Board("3"), Board("4"), Board("5"), Board("6"), Board("7"), Board("8")]
previousMove = None
global smallBoard
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
    firstMove = smallBoards[smallBoard].check(randBox, "O")
    print("Computer just played!!\n")
    print("      Small Board", smallBoard)
    print(smallBoards[smallBoard])
    smallBoard = randBox
    if firstMove == True:
        print("Computer Won")
        largeBoard.fill(smallBoard, "O")
        print(largeBoard)
def playerPlay():
    global smallBoard, firstMove
    print(f"      Main Board")
    print(largeBoard)
    print(f"        Board {smallBoard}")
    print(smallBoards[smallBoard])
    print("Choose a number to fill")
    userInput = int(input())
    while not checkInput(userInput):
        print("Choose a number to fill")
        userInput = int(input())
    while not smallBoards[smallBoard].fill(userInput, "X"):
        print("smallBoard = ", smallBoard, " userInput = ", userInput) #delete before production
        print("The box you chose is already filled\nChoose another number to fill")
        userInput = int(input())
        while not checkInput(userInput):
            print("Choose a number to fill")
            userInput = int(input())
    win = smallBoards[smallBoard].check(userInput, "X")
    print("", flush=True) #needs to be fixed
    if(win == True):
        firstMove = True
        print("Player won")
        largeBoard.fill(smallBoard, "X", -1)
    smallBaord = userInput
print("User is X. Computer is O.")
while largeBoard.checkWin() == False:
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
           print("Which AVAILABLE box, do you want to fill?")
           spot = userInput = int(input())
           smallBoard = spot
           while not smallBoards[smallBoard].fill(spot, player):
                userInput = int(input())
                if checkInput(userInput):
                    spot = userInput
                    smallBoard = spot
                else:   
                    continue

           print("The next small board will be", smallBoard)
       else:
           player = previousMove = "O"
           print("The computer is playing first")
           print(f"       Main Board")
           print(largeBoard)
           smallBoard = random.randint(0,8)
           print(f"        Board {smallBoard}")
           print(smallBoards[smallBoard])
           randBox = random.randint(0,8)
           smallBoards[smallBoard].fill(randBox, player)
           print("Computer just played!")
           print(smallBoards[smallBoard])
           smallBoard = randBox
           ## computer needs to choose a box to fill in the small board
    else:
        print("", flush = True)
        if previousMove == "O":
            playerPlay()
            previousMove = "X"
        else:
            print("", flush = True)
            print("Computer turn to fill")
            computerPlay()
            previousMove = "O"
        
       

