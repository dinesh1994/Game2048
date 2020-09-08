import random

def algo(moveMetaFile, board=None):
	lines = None
	with open(moveMetaFile,'r') as f:
		lines = f.read_lines()

	print(lines)

	randnum  = random.random()

	if randnum>=0 and randnum <= 0.49:
		return "Up";

	if randnum>=0.49 and randnum<=0.98:
		return "Left";

	if randnum>=0.98 and randnum<=0.99:
		return "Right";

	if randnum>=0.99 and randnum<=1:
		return "Down";
