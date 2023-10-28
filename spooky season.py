##S = int(input("Input number:"))
##string = ""
##string += "Sp"
##for number in range(S):
##    string += "o"
##string += "ky"
##print(string)

##N = int(input("Write far how many times?"))
##starwars = ""
##starwars += "A long time ago in a galaxy "
##for num in range(N):
##    starwars += "far "
##starwars += "away..."
##print(starwars)

##first = int(input("Youngest Child age?"))
##second = int(input("Middle Child age?"))
##if first == second:
##    print(first)
##if first != second:
##    difference = second - first
##    third = difference + second
##    print(third)

##############C = int(input("Celsius to be convereted into Fahrenheit?"))
##############F = C*(9/5)+32
##############print(F)

A3 = int(input("Apple 3 point?"))
A2 = int(input("Apple 2 point?"))
A1 = int(input("Apple 1 point?"))
B3 = int(input("Banana 3 point?"))
B2 = int(input("Banana 2 point?"))
B1 = int(input("Banana 1 point?"))
appleTotal = A3*3 + A2*2 + A1
bananaTotal = B3*3 + B2*2 + B1
if appleTotal > bananaTotal:
         print("A")
if bananaTotal > appleTotal:
         print("B")
if bananaTotal == appleTotal:
         print("T")


