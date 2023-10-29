playlist = ["A", "B", "C", "D", "E"]
while True:
    b = int(input("Button: "))
    n = int(input("Times: "))
    if b == 4 and n == 1:
        print(playlist)
        break
    elif b == 2:
        while(n > 0):
            playlist.insert(0, playlist[4])
            playlist.pop(5)
            n = n-1

    elif b == 1:
        while(n > 0):
            playlist.append(playlist[0])
            playlist.pop(0)
            n = n-1
    elif b == 3:
        while(n > 0):
            temp = playlist[0]
            playlist[0] = playlist[1]
            playlist[1] = temp
            n = n-1
    
    
        
    
