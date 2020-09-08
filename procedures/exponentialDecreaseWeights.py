import random
from time import time
from copy import deepcopy


def timeit(func):
	def wrapper(*args, **kwargs):
		t1 = time()
		print("In function {} {}".format(func.__name__, args))
		val = func(*args, **kwargs)
		t2 = time()
		# print("function {} took {}".format(func.__name__, (t2-t1)))
		return val
	return wrapper


def isFull(board):
        for i in range(0,4):
            for j in range(0,4):
                if (board[i][j] == 0):
                    return False

def addNewTile(board):
	new_tile_selection = [2,2,2,2,2,2,2,2,2,4]
	index = random.randint(0,9)
	x = -1
	y = -1
	while isFull(board) == False:
		x = random.randint(0,3)
		y = random.randint(0,3)
		if (board[x][y] == 0):
			board[x][y] = new_tile_selection[index]
		break

@timeit
def keyPressed(board,keysym,weights,depth):
	
	minscore = 0
	for idx in range(0,1):
		score = 0
		shift = 0
		if keysym == 'Down':
		    for j in range(0,4):
		        shift = 0
		        for i in range(3,-1,-1):
		            if board[i][j] == 0:
		                shift += 1
		            else:
		                if i - 1 >= 0 and board[i-1][j] == board[i][j]:
		                    board[i][j] *= 2
		                    #score += board[i][j]
		                    board[i-1][j] = 0
		                elif i - 2 >= 0 and board[i-1][j] == 0 and board[i-2][j] == board[i][j]:
		                    board[i][j] *= 2
		                    #score += board[i][j]
		                    board[i-2][j] = 0
		                elif i == 3 and board[2][j] + board[1][j] == 0 and board[0][j] == board[3][j]:
		                    board[3][j] *= 2
		                    #score += board[3][j]
		                    board[0][j] = 0
		                if shift > 0:
		                    board[i+shift][j] = board[i][j]
		                    board[i][j] = 0
		    addNewTile(board) 
		elif keysym == 'Right':
		    for i in range(0,4):
		        shift = 0
		        for j in range(3,-1,-1):
		            if board[i][j] == 0:
		                shift += 1
		            else:
		                if j - 1 >= 0 and board[i][j-1] == board[i][j]:
		                    board[i][j] *= 2
		                    #score += board[i][j]
		                    board[i][j-1] = 0
		                elif j - 2 >= 0 and board[i][j-1] == 0 and board[i][j-2] == board[i][j]:
		                    board[i][j] *= 2
		                    #score += board[i][j]
		                    board[i][j-2] = 0
		                elif j == 3 and board[i][2] + board[i][1] == 0 and board[0][j] == board[3][j]:
		                    board[i][3] *= 2
		                    #score += board[i][3]
		                    board[i][0] = 0
		                if shift > 0:
		                    board[i][j+shift] = board[i][j]
		                    board[i][j] = 0
		    addNewTile(board) 
		elif keysym == 'Left':
		    for i in range(0,4):
		        shift = 0
		        for j in range(0,4):
		            if board[i][j] == 0:
		                shift += 1
		            else:
		                if j + 1 < 4 and board[i][j+1] == board[i][j]:
		                    board[i][j] *= 2
		                    #score += board[i][j]
		                    board[i][j+1] = 0
		                elif j + 2 < 4 and board[i][j+1] == 0 and board[i][j+2] == board[i][j]:
		                    board[i][j] *= 2
		                    #score += board[i][j]
		                    board[i][j+2] = 0
		                elif j == 0 and board[i][1] + board[i][2] == 0 and board[i][3] == board[i][0]:
		                    board[i][0] *= 2
		                    #score += board[i][0]
		                    board[i][3] = 0
		                if shift > 0:
		                    board[i][j-shift] = board[i][j]
		                    board[i][j] = 0
		    addNewTile(board) 
		elif keysym == 'Up':
		    for j in range(0,4):
		        shift = 0
		        for i in range(0,4):
		            if board[i][j] == 0:
		                shift += 1
		            else:
		                if i + 1 < 4 and board[i+1][j] == board[i][j]:
		                    board[i][j] *= 2
		                    #score += board[i][j]
		                    board[i+1][j] = 0
		                elif i + 2 < 4 and board[i+1][j] == 0 and board[i+2][j] == board[i][j]:
		                    board[i][j] *= 2
		                    #score += board[i][j]
		                    board[i+2][j] = 0
		                elif i == 0 and board[1][j] + board[2][j] == 0 and board[3][j] == board[0][j]:
		                    board[0][j] *= 2
		                    #score += board[0][j]
		                    board[3][j] = 0
		                if shift > 0:
		                    board[i-shift][j] = board[i][j]
		                    board[i][j] = 0
		    addNewTile(board)
		#score = 0
		if depth == 0:
			score = ComputeStateScore(board,weights)
		if depth !=0:
			move = ['Up','Left','Right','Down']
			maxscore = 0
			for elem in move:
				score = keyPressed(board,elem,weights,depth-1)
				if maxscore < score:
					maxscore = score 
			score = maxscore

		print("Score",score)
		if idx == 0:
			minscore = score
		elif minscore > score:
			minscore = score

	print("Returning from function keyPressed {} depth {} score {}".format(board, depth,score))
	return minscore


	

def ComputeStateScore(board,weights):
	score = 0;
	for x in range(0,3):
		for y in range(0,3):
			score += (weights[x][y]*board[x][y])
	return score

@timeit
def algo(org_board=None):
	board = deepcopy(org_board)
	weights = [ [1000,10,10,1000] , 
				[10,1,1,10], 
				[10,1,1,10], 
				[1000,10,10,1000] ]
	sum_weights = 0;

	lines = None
	'''for x in range(0,3):
		for y in range(0,3):
			weights[x][y] = 100.0/((2**x+2**y))
			sum_weights  += weights[x][y]

	for x in range(0,3):
		for y in range(0,3):
			weights[x][y]=weights[x][y]*100/sum_weights '''
	#bias = [0.49,0.005,0.49,0.005]
	bias  = [0.25,0.25,0.25,0.25] 		
	move = ['Up','Left','Right','Down']

	scoreArray = [0,0,0,0]
	cummscore  = [0,0,0,0] 
	sum_score  = 0;

	for index in range(0,3):
		scoreArray[index]=keyPressed(board,move[index],weights,2)
		sum_score += scoreArray[index]
		if index == 0:
			cummscore[index] = scoreArray[index]
		cummscore[index] = cummscore[index-1] + scoreArray[index]

	for index in range(0,3):
		scoreArray[index] = scoreArray[index]/sum_score;
		cummscore[index]  = cummscore[index]/sum_score;		

	#with open(moveMetaFile,'r') as f:
	#	lines = f.read_lines()

	#print(lines)
	print("Probability 0 ",cummscore[0],cummscore[1],cummscore[2],"1")

	randnum  = random.random()

	if randnum>=0 and randnum <= cummscore[0]:
		return "Up";

	if randnum>=cummscore[0] and randnum<=cummscore[1]:
		return "Left";

	if randnum>=cummscore[1] and randnum<=cummscore[2]:
		return "Right";

	if randnum>=cummscore[2] and randnum<=1:
		return "Down";
