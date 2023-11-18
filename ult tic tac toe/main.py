from board import Board
import random
def checkInput(number):
    if number >= 0 and number < 9:
        return True
    else:
        return False
firstMove = True
largeBoard = Board()
smallBoards = [Board(), Board(), Board(), Board(), Board(), Board(), Board(), Board(), Board()]
while largeBoard.checkWin() == False:
    print("User is X. Computer is O.")
    if firstMove:
       numAsk = random.randint(0,0)
       firstMove = False
       if numAsk == 0:
           player = "X"
           print(f"       Main Board")
           largeBoard.printBoard()
           print("Enter a board number from 0-8")
           userInput = int(input())
           while not checkInput(userInput):
               print("Choose a available box")
           smallBoard = userInput
           print(f"        Board {smallBoard}")
           smallBoards[smallBoard].printBoard()
           print("Which AVAILABLE box, do you want to go in?")
           spot = userInput = int(input())
           while not smallBoards[smallBoard].fill(spot, player) or not checkInput(userInput):
                userInput = int(input())
                if checkInput(userInput):
                    spot = userInput
                else:
                    continue
                    
       else:
           player = "O"
           print("The computer is playing first")
           print(f"       Main Board")
           largeBoard.printBoard()
           smallBoard = random.randint(0,8)
           print(f"        Board {smallBoard}")
           smallBoards[smallBoard].printBoard()
           ## computer needs to choose a box to fill in the small board
        
        
       

