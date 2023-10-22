import random
import math
num = (23, 23, 45)


volume = float("14.24")
print(volume)
#num = [42,22,5,7,92,54,75]
#num2 = [32,48,21,44,63,52]
#def plusOne(list):
#    index = 0
#    while index < len(list):
#        list[index] = list[index] + 1
#        index = index+1
#    print(list)
    
#def findValue(list, int):
#    for item in list:
#        if item == int:
#            return("Int was found")
#    return "int was not found"

#print(findValue(num, 42))

computer = {
    "Storage": 1,
    "Memory": 16,
    "CPU":"Intel",
    "hasWebcam" : False}

def printDictionary(dictionary):
    for item in dictionary:
        print(item)

        
printDictionary(computer)


def cube(number):
    return number*number*number
print(cube(4))

#def areaOfRec(side1,side2):
#    return side1*side2
#print(areaOfRec(4,5))

def surArea(len):
    return len*len*6

def volume(len):
    return cube(len)
print(volume(5))

def areaOfCircle(radius):
    area = radius*radius*math.pi
    return math.floor(area)
print(areaOfCircle(4))

def roundedNum(decimal):
    return math.ceil(decimal)
print(roundedNum(4.5643))

def volumeRect(width,height,length):
    volume = width*height*length
    return math.floor(volume)
print(volumeRect(4.5,3.3,6.5))

def oddOrEven(number):
    end = number%2
    if end == 1:
        return ("Number is odd")
    else:
        return "Number is even"


# def plusTwo(num):
 #    return num = num +2

plusTwo = lambda num: num+2
print(plusTwo(4))
        


    
