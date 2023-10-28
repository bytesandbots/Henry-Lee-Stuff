import random
from Henry_turtle_hangman import *
wordbank = ["car", "pizza", "taco", "building", "computer"]
randomword = random.choice(wordbank)
mask = "*"* len(randomword)
print(mask)
clear()
penup()
goto(0,0)
setheading(0)
pendown()
drawing()
lost = 0
done = False
doneLetters = []
while(True):
    letter = input("What's a letter in the word?")
    if (len(letter) == 0):
        print("Please enter something")
        continue
    if (len(letter) > 1):
        print("Please enter only one letter")
        continue
    if letter.isdigit():
        print("Please enter a letter")
        continue
    if not(ord(letter) >= 65 and ord(letter) <= 90):
       pass
    if not(ord(letter) >= 97 and ord(letter) <= 122):
        print("Please enter a word")
        continue
    if (letter in doneLetters):
        print("You already wrote this letter")
        continue
    doneLetters.append(letter)
    if(letter in randomword):
        print("Correct")
        temp = ""
        count = 0
        for let in randomword:
            if(let == letter):
                temp += let
            else:
                temp += mask [count]
            count = count+1
        mask = temp
        print(mask)
        if (mask == randomword):
            print("Congratulations, you won!")
            done = True
                
    else:
        print("Incorrect")
        lost += 1
        if (lost==1):
            head()
        if (lost == 2):
            leftArm()
        if (lost == 3):
            rightArm()
        if (lost == 4):
            torso()
        if (lost == 5):
            leftLeg()
        if (lost == 6):
            rightLeg()
            print("You lost")
            done = True

    if (done == True):
        again = input("Would you like to play again?")
        if (again == "Yes"):
            randomword = random.choice(wordbank)
            mask = "*"* len(randomword)
            print(mask)
            clear()
            penup()
            goto(0,0)
            setheading(0)
            pendown()
            drawing()
            lost = 0
            done = False
        if (again == "No"):
            break

