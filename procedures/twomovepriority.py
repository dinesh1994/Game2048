import random
def algo(board=None):
	move = ['Up','Right','Down','Left']

	randnum  = random.random()

	if randnum>=0 and randnum <= 0.49:
		return "Up";

	if randnum>=0.49 and randnum<=0.98:
		return "Left";

	if randnum>=0.98 and randnum<=0.99:
		return "Right";

	if randnum>=0.99 and randnum<=1:
		return "Down";
