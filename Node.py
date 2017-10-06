class Node:
	def __init__(self, currentState, action, parent, stepCost, pathCost):
		self.currentState = currentState
		self.parent = parent
		self.action = action
		self.stepCost = stepCost
		self.pathCost = pathCost
