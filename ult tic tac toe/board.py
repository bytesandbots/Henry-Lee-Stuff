# we might be able to increase the readability of the code if you use a 2D areay to represent the eah row and column
# we'll talk about 2D arrays later.
class Board:
    def __init__(self):
        # I moved the properties into our initializer method since they are specific to each object of this class not to the class itself.
        self.box = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
        self.winner = ""
        self.board = r"""
       |       |       
   {}   |   {}   |   {}   
_______|_______|_______
       |       |       
   {}   |   {}   |   {}   
_______|_______|_______
       |       |       
   {}   |   {}   |   {}    
       |       |       

        """.format(self.box[0], self.box[1], self.box[2], self.box[3], self.box[4], self.box[5], self.box[6], self.box[7], self.box[8])
        
    def __str__(self):
        return self.board
    def fill(self, spot, player):
        print(self.box[spot], f"{spot}")
        print(self.board)
        if self.box[spot] == f"{spot}":
            
            self.box[spot] = player
            self.board = r"""
       |       |       
   {}   |   {}   |   {}   
_______|_______|_______
       |       |       
   {}   |   {}   |   {}   
_______|_______|_______
       |       |       
   {}   |   {}   |   {}    
       |       |       

        """.format(self.box[0], self.box[1], self.box[2], self.box[3], self.box[4], self.box[5], self.box[6], self.box[7], self.box[8])
            return True
        else:   
            return False

    def check(self, spot, player):
        if spot == 0:
            if self.box[1] == player:
                if self.box[2] == player:
                    return True
            if self.box[4] == player:
                if self.box[8] == player:
                    return True
            if self.box[3] == player:
                if self.box[6] == player:
                    return True
        elif spot == 1:
            if self.box[4] == player:
                if self.box[7] == player:
                    return True
            if self.box[0] == player:
                if self.box[2] == player:
                    return True
        elif spot == 2:
            if self.box[1] == player:
                if self.box [0] == player:
                    return True
            if self.box[5] == player:
                if self.box[8] == player:
                    return True
            if self.box[4] == player:
                if self.box[6] == player:
                    return True
        elif spot == 3:
            if self.box[0] == player:
                if self.box[6] == player:
                    return True
            if self.box[4] == player:
                if self.box[5] == player:
                    return True
        elif spot == 4:
            if self.box[3] == player:
                if self.box[5] == player:
                    return True
            if self.box[1] == player:
                if self.box[7] == player:
                    return True
            if self.box[0] == player:
                if self.box[8] == player:
                    return True
            if self.box[2] == player:
                if self.box[6] == player:
                    return True
        elif spot == 5:
            if self.box[2] == player:
                if self.box[8] == player:
                    return True
            if self.box[4] == player:
                if self.box[3] == player:
                    return True
        elif spot == 6:
            if self.box[3] == player:
                if self.box[0] == player:
                    return True
            if self.box[7] == player:
                if self.box[8] == player:
                    return True
            if self.box[4] == player:
                if self.box[2] == player:
                    return True
        elif spot == 7:
            if self.box[4] == player:
                if self.box[1] == player:
                    return True
            if self.box[6] == player:
                if self.box[8] == player:
                    return True
        elif spot == 8:
            if self.box[5] == player:
                if self.box[2] == player:
                    return True
            if self.box[7] == player:
                if self.box[6] == player:
                    return True
            if self.box[4] == player:
                if self.box[0] == player:
                    return True

        else:
            return False
    def checkWin(self):
        if self.winner == "":
            return False
        else:
            return self.winner
    def printBoard(self):
        print(self.board)




                
        
        

