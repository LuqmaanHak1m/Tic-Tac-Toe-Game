from array import *

class Map():
    def __init__(self):
        self.array = [[0,0,0], [0,0,0], [0,0,0]]

        self.x = len(self.array[0])
        self.y = self.x

class TicTacToe():
    def __init__(self):
        # 2D-Array
        self.map = Map()

        # Symbol
        self.player = "X"

    def switchPlayer(self):
        if self.player == "X":
            self.player = "O"
        else: self.player = "X"

    def updateMap(self, x, y, player):
        if self.isUpdateable(x, y):
            self.map.array[x][y] = player
            self.switchPlayer()
        else:
            print("You can't park there sir.")
            

    def isUpdateable(self, x, y) -> bool:
        if self.map.array[x][y] != 0:
            return False
        else: return True

    def playGame(self):
            gameOver = False

            while gameOver == False:
                x, y = self.takeInput()
                self.updateMap(x, y, self.player)
                gameOver = self.checkGameOver()

            self.drawBoard()
                
            if self.player == "X":
                print("Player O has won the game!!!")
            else:
                print("Player X has won the game!!!")

    def takeInput(self):
        valid = False
        
        while not valid:
            self.drawBoard()
            try:
                userInputX = int(input("\nPlace your marker\nType in the x co-ordinate (0-2): "))
                userInputY = int(input("Type in the y co-ordinate (0-2): "))
                if 0 <= userInputX < self.map.x and 0 <= userInputY < self.map.y:
                    valid = True
                else:
                    print("\nPlease enter coordinates within the limits (0-2)")
            except ValueError:
                print("\nPlease enter valid integers")
        
        return userInputY, userInputX

    def checkGameOver(self) -> bool:
        # Check rows and columns
        for i in range(3):
            if self.map.array[i][0] == self.map.array[i][1] == self.map.array[i][2] != 0:
                return True
            if self.map.array[0][i] == self.map.array[1][i] == self.map.array[2][i] != 0:
                return True

        # Check diagonals
        if self.map.array[0][0] == self.map.array[1][1] == self.map.array[2][2] != 0:
            return True
        if self.map.array[2][0] == self.map.array[1][1] == self.map.array[0][2] != 0:
            return True
        
        return False
                
        

    def drawBoard(self):
        for row in self.map.array:
            line = "|"
            for col in row:

                if col == 0:
                    line += " "
                else:
                    line += str(col)

                line += "|"
            print(f"{line}\n-------")

        

game = TicTacToe()

game.playGame()