from Game2048withGUI import Game
from importlib import import_module

class Player:
	algoModule = None
	def __init__(self,algo):
		#try:
		self.algoModule = import_module('procedures.{}'.format(algo))
		#except Exception as e:
		#	print(str(e))


	def NextMove(self,board):
		move = self.algoModule.algo(board)
		return move
		


class GameSim(Game):

	def keyPressed(self,keysym):
		shift = 0
		if keysym == 'Down':
		    for j in range(0,4):
		        shift = 0
		        for i in range(3,-1,-1):
		            if self.board[i][j] == 0:
		                shift += 1
		            else:
		                if i - 1 >= 0 and self.board[i-1][j] == self.board[i][j]:
		                    self.board[i][j] *= 2
		                    self.score += self.board[i][j]
		                    self.board[i-1][j] = 0
		                elif i - 2 >= 0 and self.board[i-1][j] == 0 and self.board[i-2][j] == self.board[i][j]:
		                    self.board[i][j] *= 2
		                    self.score += self.board[i][j]
		                    self.board[i-2][j] = 0
		                elif i == 3 and self.board[2][j] + self.board[1][j] == 0 and self.board[0][j] == self.board[3][j]:
		                    self.board[3][j] *= 2
		                    self.score += self.board[3][j]
		                    self.board[0][j] = 0
		                if shift > 0:
		                    self.board[i+shift][j] = self.board[i][j]
		                    self.board[i][j] = 0
		    self.printboard()
		    self.addNewTile() 
		    self.isOver()
		elif keysym == 'Right':
		    for i in range(0,4):
		        shift = 0
		        for j in range(3,-1,-1):
		            if self.board[i][j] == 0:
		                shift += 1
		            else:
		                if j - 1 >= 0 and self.board[i][j-1] == self.board[i][j]:
		                    self.board[i][j] *= 2
		                    self.score += self.board[i][j]
		                    self.board[i][j-1] = 0
		                elif j - 2 >= 0 and self.board[i][j-1] == 0 and self.board[i][j-2] == self.board[i][j]:
		                    self.board[i][j] *= 2
		                    self.score += self.board[i][j]
		                    self.board[i][j-2] = 0
		                elif j == 3 and self.board[i][2] + self.board[i][1] == 0 and self.board[0][j] == self.board[3][j]:
		                    self.board[i][3] *= 2
		                    self.score += self.board[i][3]
		                    self.board[i][0] = 0
		                if shift > 0:
		                    self.board[i][j+shift] = self.board[i][j]
		                    self.board[i][j] = 0
		    self.printboard()
		    self.addNewTile() 
		    self.isOver()
		elif keysym == 'Left':
		    for i in range(0,4):
		        shift = 0
		        for j in range(0,4):
		            if self.board[i][j] == 0:
		                shift += 1
		            else:
		                if j + 1 < 4 and self.board[i][j+1] == self.board[i][j]:
		                    self.board[i][j] *= 2
		                    self.score += self.board[i][j]
		                    self.board[i][j+1] = 0
		                elif j + 2 < 4 and self.board[i][j+1] == 0 and self.board[i][j+2] == self.board[i][j]:
		                    self.board[i][j] *= 2
		                    self.score += self.board[i][j]
		                    self.board[i][j+2] = 0
		                elif j == 0 and self.board[i][1] + self.board[i][2] == 0 and self.board[i][3] == self.board[i][0]:
		                    self.board[i][0] *= 2
		                    self.score += self.board[i][0]
		                    self.board[i][3] = 0
		                if shift > 0:
		                    self.board[i][j-shift] = self.board[i][j]
		                    self.board[i][j] = 0
		    self.printboard()
		    self.addNewTile() 
		    self.isOver()
		elif keysym == 'Up':
		    for j in range(0,4):
		        shift = 0
		        for i in range(0,4):
		            if self.board[i][j] == 0:
		                shift += 1
		            else:
		                if i + 1 < 4 and self.board[i+1][j] == self.board[i][j]:
		                    self.board[i][j] *= 2
		                    self.score += self.board[i][j]
		                    self.board[i+1][j] = 0
		                elif i + 2 < 4 and self.board[i+1][j] == 0 and self.board[i+2][j] == self.board[i][j]:
		                    self.board[i][j] *= 2
		                    self.score += self.board[i][j]
		                    self.board[i+2][j] = 0
		                elif i == 0 and self.board[1][j] + self.board[2][j] == 0 and self.board[3][j] == self.board[0][j]:
		                    self.board[0][j] *= 2
		                    self.score += self.board[0][j]
		                    self.board[3][j] = 0
		                if shift > 0:
		                    self.board[i-shift][j] = self.board[i][j]
		                    self.board[i][j] = 0
		    self.printboard()
		    self.addNewTile() 
		    self.isOver()
		self.scorestring.set(str(self.score))
		if self.score > self.highscore:
		    self.highscore = self.score
		    self.highscorestring.set(str(self.highscore))	    
		    
	def Simulate(self):
		player = Player('exponentialDecreaseWeights')
		print(self.board)
		move = player.NextMove(self.board)
		self.keyPressed(move)
		self.after(10000,self.Simulate)	





if __name__ == "__main__":
    app = GameSim()
    #app.bind_all('<Key>', app.Simulate)
    app.wm_title("2048")
    app.minsize(420,450)
    app.maxsize(420,450)
    app.Simulate()	
    app.mainloop()
