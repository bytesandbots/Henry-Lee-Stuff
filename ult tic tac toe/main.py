## we need to implement a variable or property to store last move
## your next move is determined by your opponents last move
## Henry, if you could, please bring a notebook with you so you can keep track of notes you take

from board import Board
import random
import os

import os
clear = lambda: os.system('cls')
clear()
firstMove = True
largeBoard = Board("main")
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
    print("Computer just played!!\n")
    print(f"      Board {smallBoard}")
    print(smallBoards[smallBoard])
    if smallBoards[smallBoard].check(randBox, "O"):
        print(f"Computer won {smallBoard}")
        largeBoard.fill(smallBoard, "O")
    smallBoard = randBox
    if largeBoard.check(randBox, "O"):
        print("Computer won the game")
        
def playerPlay():
    global smallBoard, firstMove
    if smallBoards[smallBoard].checkWin() == "X" or smallBoards[smallBoard].checkWin() == "O":
        print(f"       Main Board")
        print(largeBoard)
        print("Enter a board number from 0-8")
        userInput = input()
        while not checkInput(userInput):
            print("Enter a board number from 0-8")
            userInput = input()
        smallBoard = int(userInput)
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
        print("The box you chose is already filled\nChoose another number to fill")
        userInput = int(input())
        while not checkInput(userInput):
            print("Choose a number to fill")
            userInput = int(input())
    if smallBoards[smallBoard].check(userInput, "X"):
        print(f"Player won Board {smallBoard}")
        largeBoard.fill(smallBoard, "X")
        print(largeBoard)
    smallBoard = userInput
    if largeBoard.check(userInput, "X"):
        print("Player won the game!")
        
print("User is X. Computer is O.")
while largeBoard.checkWin() == False:
    if firstMove:
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
        if previousMove == "O":
            playerPlay()
            previousMove = "X"
            #clear()
        else:
            print("Computer turn to fill")
            computerPlay()
            previousMove = "O"
            #clear()
        
    
