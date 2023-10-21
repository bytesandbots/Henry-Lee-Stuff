import random 
list = ["Sword", "Health Potion", "Old Boot"]
def Chest():
    item = random.randint(0,2)
    return item
def ItemFound(n):
    print(list[n])
num = Chest()
print(ItemFound(num))